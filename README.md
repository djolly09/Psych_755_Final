# PSYCH 755 Final Project

## Authors

David Jolly, Lauren Khoury, Jake Murray

## Overview

For our final project, we familiarized ourselves with looking at insurance data in preparation for our Capstone project. 
We built a SQL database containing multiple sources of insurance data that we found.
With our main dataset, we fit a neural network to predict insurance fraud based on certain predictors.
Please view the rendered HTML file to see more about the project overview, research question, steps to answer the research question, and evaluation of our results. 

Our final project uses:

- Quarto
- Python
- R & RStudio
- SQL
- Neural Networks

## Files in this Repo

1. This README file!

2. Data folder with
    - 'insurance_claims.csv' : contains the primary dataset of our analysis
    - 'average_insurance_2015.csv' : contains extra insurance data added to the SQL database
    
3. 'build-insurance.py' : Python script for building SQL database

4. 'insurance.db' : the SQL database

5. '755_Final.qmd' : R/quarto notebook with our data analysis & neural network model fitting

6. '755_Final.html' : the rendered QMD 

## Using this Repo

### Getting Started

In order to interact with the files in this repository, complete the following steps.

1.  Clone this repository:

```         
git clone https://github.com/djolly09/Psych_755_Final.git
```

2. Navigate to the project folder. For example if you cloned into a github folder in Documents:

```
cd Documents/github/Psych_755_Final
```

### Building a SQL Database

After completing the steps above, you are ready to build a SQL database! 

1. Run this command to build the SQL database:

```
python build-insurance.py
```

### Exploring the SQL Database

After building the database, you can start exploring it.

1. Open SQLite interface:

```
sqlite3 insurance.db
```

2. View the tables (datasets in repo's data folder):

```
.tables
```

3. List the column names and data types in our main insurance claims table:

```
.schema insurance_claims
```

4. Return to system terminal:

```
.quit
```


### Fitting a Neural Network

This markdown notebook will use R to fit a neural network to predict insurance fraud. 
The notebook also conducts preliminary exploratory data analysis.

To run/render this notebook, installation of these R packages is required:

- tidyverse
- tidymodels
- xfun
- keras
- magrittr
- themis
- datadictionary

It also sources functions from our machine learning professor's GitHub.

View the rendered HTML to see the code, output, and text for each step of the coding process. 
Or render the QMD for yourself!








