# Disaster Response Message Classification Pipeline Project
Welcome to the repository of Second Project of Udacity's Data Scientist Nanodegree in collaboration with [Figure 8](https://appen.com).

## Project Overview

! [alt text]()
! [alt text]()

## Project Structure
- **_data_** - A sub-directory containing training dataset and cleaned and processed dataset.
    - _messages.csv_ - A CSV file that contains messages received via different platforms at time of disaster.
    - _categories.csv_ - A CSV file that contains categories to which each row in above CSV file belongs to.
    - _disaster_response.db_ - SQLite database that contains clean and processed data from the CSV files.
- **_plots_** - A sub-directory containing vizualizations describing training dataset.
    - _Distribution of Number of Categories to which a Message belongs.png_ - A BarChart depicting number of categories to which a message belongs.
    - _Number of Messages in different Categories.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset.
    - _Number of Messages in different Categories by Genre.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset by Genre (mode of receiving a message).
    - _Number of Messages received via different Genre.png_ - A BarChart depicting number of messages received via different Genre.
- **_models.zip_** - A zipped sub-directory containing 35 trained models for each of 35 categories in the training dataset.
- **_process_data.py_** - Python script that reads in data from CSV files, cleans the data, and loads the data into SQL database.
- **_train_classifier.py_** - Python Script that reads in data from SQL database, train and save a model for each of the 35 different categories.
- **_run.py_** - Python Script that deploys a dashboard constructed with Plotly Dash on a localhost.

## Required Packages
Following packages should be installed with Python 3.9.5 to successfully run this project
- [numpy](https://pypi.org/project/numpy/)
- [pandas](https://pypi.org/project/pandas/)
- [nltk](https://pypi.org/project/nltk/)
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)
- [dash](https://pypi.org/project/dash/)
- [dash-bootstrap-components](https://pypi.org/project/dash-bootstrap-components/)

## Running the project
1. Download all the files and directories available here to a directory on your local and maintain the same directory structure as in here.
2. Create a new sub-directory named **_models_** and unzip here **_models.zip_** storing all the models (having extension **_.pickle_**) within this newly created sub-directory.
3. Create and activate a virtual environment that satisfies all the above-mentioned requirements.
4. If you do not wish to create your own SQLite database and train your own models, you can simply run the project with the provided models and SQLite database entering the following command in the terminal after navigating to the project's main directory -  ```python run.py```
5. Or if you wish to create your own SQLite database and train all the models from scratch run the following commands in sequence in the terminal after navigating to project's directory - 
    - ```python process_data.py '/path_to_project_directory/data/messages.csv' '/path_to_project_directory/data/categories.csv' '/path_to_project_directory/data/'```
    - ```python train_classifier.py '/path_to_project_directory/data/' '/path_to_project_directory/models/'```
    - ```python run.py```
