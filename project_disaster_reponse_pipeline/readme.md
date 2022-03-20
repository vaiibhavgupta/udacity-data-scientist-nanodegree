# Disaster Response Message Classification Pipeline Project
This Directory contains following sub-Directories and Scripts related to Project 2 - Disaster Response Message Classification Pipeline Project - of Udacity's Data Scientist Nanodegree.
- **_data_** - Directory containing training dataset and cleaned and processed dataset.
    - _messages.csv_ - A CSV file that contains messages received via different platforms at time of disaster. Provided by [Figure 8](https://appen.com).
    - _categories.csv_ - A CSV file that contains categories to which each row in above CSV file belongs to. Provided by [Figure 8](https://appen.com).
    - _disaster_response.db_ - SQLite database that contains clean and processed data from the CSV files.
- **_plots_** - Directory containing vizualizations describing training dataset.
    - _Distribution of Number of Categories to which a Message belongs.png_ - A BarChart depicting number of categories to which a message belongs.
    - _Number of Messages in different Categories.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset.
    - _Number of Messages in different Categories by Genre.png_ - A BarChart depicting number of messages in each of the 35 categories in the dataset by Genre (mode of receiving a message).
    - _Number of Messages received via different Genre.png_ - A BarChart depicting number of messages received via different Genre.
- **_models.zip_** - Zipped directory containing 35 trained models for each of 35 categories in the training dataset.
- **_process_data.py_** - Python script that reads in data from CSV files, cleans the data, and loads the data into SQL database.
- **_train_classifier.py_** - Python Script that reads in data from SQL database, train and save a model for each of the 35 different categories.
- **_run.py_** - Python Script that deploys a dashboard constructed with Plotly Dash on a localhost.

## Dataset
1. [calendar data](https://www.kaggle.com/airbnb/boston?select=calendar.csv)
    - Dataset contains the price and availability of all the listings in Boston on a daily level between Sept 6, 2016 to Sept 5, 2017.
2. [listings data](https://www.kaggle.com/airbnb/boston?select=listings.csv)
    - Dataset contains detailed information related to all the listings in Boston between Sept 6, 2016 to Sept 7, 2017.

## Required Python Packages
Python packages required to run the notebook are
- Numpy
- Pandas
- Seaborn

## How to use the Ipython Notebook 
1. Download the notebook into a folder in your local system.
2. Download both the datasets to the same folder where you have downloaded the notebook.
3. Create a virtual environment and install above-mentioned python packages.
4. Activate the virtual environment and start the notebook.

## Blog
The blog related to this project can be found [here](https://medium.com/@vaibhavgupta.1apr/looking-to-invest-in-airbnb-real-estate-in-boston-give-this-article-and-data-science-a-chance-to-1108202fc49d)
