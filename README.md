# PSYCH 755 Final Project

## Overview

For our final project, we practice looking at insurance data in preparation for our Capstone project. 

Our final project uses:

- Quarto
- Python & Jupyter notebooks
- R & RStudio
- SQL
- Neural Networks

## Files in this Repo

1. This README file!

2. Data folder with
    - 'insurance_claims.csv' : contains the primary dataset of our analysis
    - 'average_insurance_2015.csv' : contains extra insurance data added to the SQL database
    
3. 'build-insurance.py' : Python script for building SQL database

4. '755_final.qmd' : R/quarto notebook with our data analysis & neural network model fitting

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

This notebook will use R to fit a neural network to predict insurance fraud.

It requires installation of these R packages:

- tidyverse
- tidymodels
- xfun
- keras
- magrittr

It also sources functions from our machine learning professor's github.








