import re
import sys
import pickle
import pandas as pd

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from sqlalchemy import create_engine as sqlalchemy_create_engine, inspect as sqlalchemy_inspect


class GetGlobalVariables:
    '''
    this class defines 4 global variables represeting:
        1. name of SQL databse
        2. name of table to store unfiltered data
        3. name of table to store filtered data
        4. starting substring of name of all the tables
        5. starting substring of name of all the models
        6. file extension of all the models
    '''
    sql_database_name = 'disaster_response.db'
    raw_data_table_name = 'disaster_response_unfiltered'
    data_table_name = 'disaster_response'
    table_name_startswith_substring = 'disaster_response_'
    classifier_name = 'RFC_'
    model_file_format = '.pickle'


def load_data(database_folder_path):
    '''
    the function loads data from various tables in SQL database into dataframes
    input parameters:
        1. database_folder_path: folder path to SQL database
    output variables:
        1. all_df_dict: dictionary of all dataframes with key representing table name from SQL database and value representing dataframe
        2. all_df_dict_counts: dictionary representing number of rows to keep in dataframe for 0 and 1 category to avoid imbalance in dataframe
    '''
    print(f'Creating SQL Engine to load data from Database:\n\t{database_folder_path}{GetGlobalVariables.sql_database_name}\n')
    sql_engine = sqlalchemy_create_engine('sqlite:///'+database_folder_path+GetGlobalVariables.sql_database_name)

    print('Reading data into Pandas DataFrame from Table:')
    all_df_dict = {}
    for table_name in sqlalchemy_inspect(sql_engine).get_table_names():
        if (table_name.startswith(GetGlobalVariables.table_name_startswith_substring)) and (table_name != GetGlobalVariables.raw_data_table_name):
            print(f'\t{table_name}')
            all_df_dict[table_name] = pd.read_sql_table(table_name, sql_engine)

    print('Data loaded successfully from SQL.\n')

    all_df_dict_counts = {}
    print('Fetching statistics to help creation of a balanced dataset for Category:')
    for table_name in all_df_dict.keys():
        category_column = table_name.replace(GetGlobalVariables.table_name_startswith_substring, '')
        print(f'\t{category_column}')
        temp_grouped_df = all_df_dict[table_name].groupby(category_column).agg({'message':'count'}).reset_index()
        num_messages_0 = temp_grouped_df[temp_grouped_df[category_column] == 0]['message'].values[0]
        num_messages_1 = temp_grouped_df[temp_grouped_df[category_column] == 1]['message'].values[0]
        
        if num_messages_0 < num_messages_1:
            if num_messages_1 < 1.25 * num_messages_0:
                all_df_dict_counts[category_column] = {0: num_messages_0, 1: num_messages_1}
            else:
                all_df_dict_counts[category_column] = {0: num_messages_0, 1: int(1.25 * num_messages_0)}
        else:
            if num_messages_0 < 1.25 * num_messages_1:
                all_df_dict_counts[category_column] = {0: num_messages_0, 1: num_messages_1}
            else:
                all_df_dict_counts[category_column] = {0: int(1.25 * num_messages_1), 1: num_messages_1}
    
    print('Statistics stored Successfully.\n')
    return all_df_dict, all_df_dict_counts


def get_dataframe_dictionary(database_folder_path):
    '''
    the function calls load_data function to load and create a balanced dataset
    input parameters:
        1. database_folder_path: folder path to SQL database
    output variables:
        1. all_df_dict: dictionary of all dataframes with key representing table name from SQL database and value representing dataframe
            with no class imbalance
    '''
    all_df_dict, all_df_dict_counts = load_data(database_folder_path)
    print(f'Creating a balanced dataset for Category:')
    for table_name in all_df_dict.keys():
        category_column = table_name.replace(GetGlobalVariables.table_name_startswith_substring, '')
        print(f'\t{category_column}')
        temp_df = all_df_dict[table_name]
        temp_df_0 = temp_df[temp_df[category_column] == 0].sample(n=all_df_dict_counts[category_column][0])
        temp_df_1 = temp_df[temp_df[category_column] == 1].sample(n=all_df_dict_counts[category_column][1])
        all_df_dict[table_name] = pd.concat([temp_df_0, temp_df_1], axis=0).sample(frac=1).reset_index(drop=True)

    print(f'Balanced dataset creation Successful.\n')
    return all_df_dict


def tokenize(text):
    '''
    the function tokenize, normalize, lemmatize, and perform URL replacement in the given text  
    input parameters:
        1. text: python string
    output variables:
        1. clean_tokens: list of tokens generated from the input text
    '''
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(tok).lower().strip() for tok in tokens]
    return clean_tokens


def build_model():
    '''
    the function initializes a scikit-learn pipeline and GridSearchCV
    input parameters: None
    output variables:
        1. cv: model pipeline
    '''
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('classifier', RandomForestClassifier())
    ])

    parameters = {
        'vectorizer__ngram_range': ((1, 1), (1, 2)),
        'classifier__n_estimators': [100, 200, 300],
        'classifier__min_samples_split': [3, 4, 5]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)
    return cv


def evaluate_model(model, X_test, y_test):
    '''
    the function predicts on test data and generates a classification report
    input parameters: 
        1. model: scikit-learn pipeline initialized with GridSearchCV
        2. X_test: features of test dataset 
        3. y_test: target of test dataset
    output variables: None
    '''
    y_pred = model.predict(X_test)
    print(f'\t\t\tClassification Report:\n{classification_report(y_test, y_pred)}\n')
    print(f'\t\t\tBest Parameters: {model.best_params_}')
    return None


def save_model(model, model_file_path):
    '''
    the function dumps the trained model at the provided local path
    input parameters: 
        1. model: scikit-learn pipeline initialized with GridSearchCV
        2. model_file_path: output file path of the model 
    output variables: None
    '''
    pickle.dump(model, open(model_file_path, 'wb'))
    print('\t\t\tModel saved Successfully.\n\n')
    return None


def main():

    if len(sys.argv) == 3:
        database_folder_path, model_folder_path = sys.argv[1:]

        if not database_folder_path.endswith('/'):
            database_folder_path += '/'

        if not model_folder_path.endswith('/'):
            model_folder_path += '/'

        all_df_dict = get_dataframe_dictionary(database_folder_path)

        print('Starting Model Training for Category:')
        for idx, table_name in enumerate(all_df_dict.keys()):
            category_name = table_name.replace(GetGlobalVariables.table_name_startswith_substring, '')
            print(f'\t{idx + 1}/{len(all_df_dict.keys())} - {category_name}')

            X, y = all_df_dict[table_name]['message'], all_df_dict[table_name][category_name]
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=70, test_size=0.3)
            print('\t\tTrain and Test Dataset created Successfull.')
            print(f'\t\t\tSamples in Train Dataset - {X_train.shape[0]}')
            print(f'\t\t\tSamples in Test Dataset - {X_test.shape[0]}')
            
            print('\t\tContructing Model')
            model = build_model()
            
            print('\t\tTraining Model')
            model.fit(X_train, y_train)
            
            print('\t\tEvaluating Model')
            evaluate_model(model, X_test, y_test)

            model_file_path = model_folder_path+GetGlobalVariables.classifier_name+category_name+GetGlobalVariables.model_file_format

            print(f'\t\tSaving Model to: {model_file_path}')
            save_model(model, model_file_path)
        print('\n\n\n=========================================Script Executed Successfully=========================================\n\n\n')

    else:
        print("Please provide the path to the folder in which the SQL Database 'disaster_response.db' is located as the first argument " \
              "and the folder path to which you want this script to save all the trained models to as the second argument." \
              "\nExample: python train_classifier.py ../database_folder/ ../model_folder/")


if __name__ == '__main__':
    print('\n\n\n=========================================Starting Script Execution=========================================\n\n\n')
    main()
