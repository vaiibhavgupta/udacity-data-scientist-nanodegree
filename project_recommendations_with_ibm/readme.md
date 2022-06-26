# Recommendation Engine - IBM Watson Studio
Welcome to the repository of the third Project of Udacity's Data Scientist Nanodegree in collaboration with IBM Watson Studio.

## Project Overview
The objective of the project is to make article recommendations for users in IBM Watson Studio data platform based on the history of user-article interactions.

The Project Notebook if divided into following parts:
1. Exploratory Data Analysis
2. Rank Based Recommendations
3. User-User Based Collaborative Filtering
4. Content Based Recommendations (EXTRA - NOT REQUIRED)
5. Matrix Factorization
6. Extras

## Project Structure
- **_data_** - A sub-directory containing required data files.
    - _articles_community.csv_ - A CSV file that contains information regarding all the articles present in the dataset.
    - _user-item-interactions.csv_ - A CSV file that contains information regarding all interactions between all the users and all the articles.
    - _user_item_matrix.p.zip_ - A zipped pickle file that contain pre-generated user-item matrix for Matrix Factorization.
- **recommendations_with_ibm.html_** - HTML version of the Project Notebook.
- **recommendations_with_ibm.ipynb_** - Project Code Notebook.

## Required Packages
Following packages should be installed with Python 3.9.5 to successfully run this project
- [numpy](https://pypi.org/project/numpy/)
- [pandas](https://pypi.org/project/pandas/)
- [plotly](https://pypi.org/project/plotly/)

## Running the project
1. Download all the files and directories available here to a directory on your local and maintain the same directory structure as in here.
2. Unzip **user_item_matrix.p.zip** in the **/data** folder.
3. Create and activate a virtual environment that satisfies all the above-mentioned requirements.
4. Open and run the Notebook.
