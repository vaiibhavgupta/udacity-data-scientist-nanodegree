# Disaster Response Message Classification Pipeline Project
Welcome to the repository of second Project of Udacity's Data Scientist Nanodegree in collaboration with [Figure 8](https://appen.com).

## Project Overview
The project helps in classifying messages into 36 pre-defined categories that helps in sorting and sending out these messages to appropriate relief teams and agencies. The project deals with real-world data, collected by [Figure 8](https://appen.com), as these messages were sent out during a disaster.

We kick-start the project off by building an ETL pipeline that loads the training data from CSV files, cleans the data, and loads the processed data into an SQLite database. We then use this SQLite database to perform some EDA and train a ```RandomForestClassifier``` for each of the 36 pre-defined categories present in the training data.

Training a separate model for each category helps us in two ways:
1. Dealing with the imbalance present at the dataset level -
    - Since the project deals with MultiLabel MultiOutput Classification, let's say we have 1000 messages in Category A, 200 messages in Category B, and 3000 messages in Category C. When we train a separate model for each category, we will filter out messages for that particular category only and our model will not be affected by the imbalanced dataset.
2. Dealing with the imbalance present at the category level -
    - Further, let's say in category A, we have 800 samples having the target value of ```1``` and 200 samples having the target value of ```0```. Now, we can further undersample these 800 samples to make them comparable to their counterpart of 200 samples.

Following are the two screenshots from the Web App - 
![ClassifyMessages.jpeg](https://github.com/vaiibhavgupta/udacity_data_scientist_nanodegree/blob/main/project_disaster_reponse_pipeline/app%20screenshots/Classify%20Messages.jpeg)
![VizualizeData.jpeg](https://github.com/vaiibhavgupta/udacity_data_scientist_nanodegree/blob/main/project_disaster_reponse_pipeline/app%20screenshots/Vizualize%20Data.jpeg)

## Project Structure
- **_data_** - A sub-directory containing training dataset and cleaned and processed dataset.
    - _messages.csv_ - A CSV file that contains messages received via different platforms at time of disaster.
    - _categories.csv_ - A CSV file that contains categories to which each row in above CSV file belongs to.
    - _disaster_response.db_ - SQLite database that contains clean and processed data from the CSV files.
    - _process_data.py_ - Python script that reads in data from CSV files, cleans the data, and loads the data into SQL database. 
- **_models_** - A sub-directory containing model zipped file and model training python script.
    - _models.zip_ - A zipped sub-directory containing 35 trained models for each of 35 categories in the training dataset.
    - _train_classifier.py_ - Python Script that reads in data from SQL database, train and save a model for each of the 35 different categories.
- **_plots_** - A sub-directory containing vizualizations describing training dataset.
    - _Distribution of Number of Categories to which a Message belongs.png_ - A BarChart depicting number of categories to which a message belongs.
    - _Number of Messages in different Categories.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset.
    - _Number of Messages in different Categories by Genre.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset by Genre (mode of receiving a message).
    - _Number of Messages received via different Genre.png_ - A BarChart depicting number of messages received via different Genre.
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
4. Run the following commands in sequence in the terminal after navigating to the project folder - 
    1. ```python data/process_data.py data/messages.csv data/categories.csv data/```
    2. ```python models/train_classifier.py data/ models/```
    3. ```python run.py```
