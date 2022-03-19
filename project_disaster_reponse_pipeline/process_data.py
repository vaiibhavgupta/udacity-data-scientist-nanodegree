import sys
import pandas as pd
from sqlalchemy import create_engine as sqlalchemy_create_engine


class GetGlobalVariables:
    '''
    this class defines 4 global variables represeting:
        1. name of SQL databse
        2. name of table to store unfiltered data
        3. name of table to store filtered data
        4. starting substring of name of all the tables
    '''
    sql_database_name = 'disaster_response.db'
    raw_data_table_name = 'disaster_response_unfiltered'
    data_table_name = 'disaster_response'
    table_name_startswith_substring = 'disaster_response_'


def load_data(messages_file_path, categories_file_path):
    '''
    the function loads the messages and categories dataset and returns a merged dataframe
    input parameters:
        1. messages_file_path: file path of messages.csv
        2. categories_file_path: file path of categories.csv
    output variables:
        1. df: merged dataframe consisting of messages and categories dataframes 
    '''
    print(f"Reading messages data into Pandas DataFrame from:\n\t{messages_file_path}\n")
    messages = pd.read_csv(messages_file_path)

    print(f"Reading categories data into Pandas DataFrame from:\n\t{categories_file_path}\n")
    categories = pd.read_csv(categories_file_path)

    print('Merging messages and categories dataframe.\n')
    df = pd.merge(left=messages, right=categories, left_on='id', right_on='id', how='inner')
    return df


def clean_data(df):
    '''
    the function loads the merged dataframe, performs data cleaning and returns the cleaned dataframe
    input parameters:
        1. df: merged dataframe consisting of messages and categories dataframes 
    output variables:
        1. df: cleaned dataframe
    '''
    print('Cleaning and Generating new Features using the data in the merged DataFrame:')

    categories = df['categories'].str.split(';', expand=True)
    categories.columns = categories.iloc[0].apply(lambda x: x.split('-')[0]).unique().tolist()
    categories = categories.apply(lambda x: x.str[-1].astype(int))
    print('\tCreated mulitple new Features from categories column and thus deleting it.')

    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    print(f'\tFound {df.duplicated().sum()} duplicates in dataframe. Now reducing them to', end=' ')
    df.drop_duplicates(inplace=True)
    print(f'{df.duplicated().sum()} duplicates.')

    categories_sum = df.select_dtypes(int).sum()
    all_zero_or_one_col_list = categories_sum[(categories_sum == 0) | (categories_sum == len(df))].index.tolist()
    df.drop(all_zero_or_one_col_list, axis=1, inplace=True)
    print(f'\tDeleted columns - {all_zero_or_one_col_list} as they contain all 0s or all 1s.')

    print("\tReplacing 2s with 1s for 'related' column on assumption - Mistake in Data Entry as 2 lies near 1 on keyboard.\n")
    df.loc[df['related'] == 2, 'related'] = 1
    df.reset_index(drop=True)
    return df


def save_data(df, table_name, sql_engine):
    '''
    the function loads the merged dataframe, performs data cleaning and returns the cleaned dataframe
    input parameters:
        1. df: merged dataframe consisting of messages and categories dataframes 
    output variables:
        1. df: cleaned dataframe
    '''
    df.to_sql(table_name, sql_engine, index=False)
    print(f'\t Data saved Successfully into -  {table_name}.')
    return None


def save_data_into_sql_db(df, sql_engine):
    '''
    the function saves dataframe into SQL table
    input parameters:
        1. df: cleaned dataframe
        2. sql_engine: sqllchemy engine 
    output variables: None
    '''
    save_data(df, GetGlobalVariables.raw_data_table_name, sql_engine)

    df = df.drop(['id', 'original', 'genre'], axis=1)
    save_data(df, GetGlobalVariables.data_table_name, sql_engine)
    save_data(df[['message', 'related']], f'{GetGlobalVariables.table_name_startswith_substring}related', sql_engine)

    df = df[df['related'] == 1].reset_index(drop=True)
    df.drop('related', axis=1, inplace=True)
    for col in df.select_dtypes(int):
        save_data(df[['message', col]], f'{GetGlobalVariables.table_name_startswith_substring}{col}', sql_engine)
    
    return None


def main():
    if len(sys.argv) == 4:
        messages_file_path, categories_file_path, database_folder_path = sys.argv[1:]

        if not database_folder_path.endswith('/'):
            database_folder_path += '/'

        df = load_data(messages_file_path, categories_file_path)
        df = clean_data(df)

        sql_engine = sqlalchemy_create_engine('sqlite:////'+database_folder_path+GetGlobalVariables.sql_database_name)
        print(f'Engine created for Database {GetGlobalVariables.sql_database_name}:')

        save_data_into_sql_db(df, sql_engine)

        print('\n\n\n=========================================Script Executed Successfully=========================================\n\n\n')
    else:
        print("Please provide the filepaths of the messages and categories datasets as the first and second argument respectively and "\
              "the path to the folder in which you want this script to store cleaned data in SQL Database - 'disaster_response.db'."\
              "\nExample: python process_data.py ../disaster_messages.csv ../disaster_categories.csv ../database_folder/")


if __name__ == '__main__':
    print('\n\n\n=========================================Starting Script Execution=========================================\n\n\n')
    main()