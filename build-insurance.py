#!/usr/bin/env python3
"""
Creates and populates SQLite database with datasets for our project. 
Loads in datasets and creates corresponding tables in the insurance.db.
"""

import os
import sqlite3
import seaborn as sns
import pandas as pd
import sys

def get_user_confirmation(prompt):
    """Ask user for yes/no confirmation."""
    while True:
        response = input(prompt + " (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        if response in ['no', 'n']:
            return False
        print("Please answer 'yes' or 'no'")

def create_database():
    """Create a new SQLite database and populate it"""
    
    # Check if database exists and get confirmation before deleting
    if os.path.exists('insurance.db'):
        # Ask user if they wish to keep the existing database
        if not get_user_confirmation("Database 'insurance.db' already exists. Delete and recreate?"):
            print("Aborted. Existing database was not modified.")
            sys.exit(0)
        # Overwrite if user indicates no desire to keep existing database
        os.remove('insurance.db')
    
    # Create a connection to the new database
    conn = sqlite3.connect('insurance.db')
    
        # Load insurance claims
        try:
            print("\nLoading insurance claims dataset...")
            url = 'https://raw.githubusercontent.com/adamrossnelson/confident/refs/heads/main/data/complaints-bank.csv'
            insurance_claims_data = pd.read_csv(url,index_col = 0)
            insurance_claims_data = insurance_claims_data.dropna()  # Remove rows with missing values
            insurance_claims_data.to_sql('insurance_claims', conn, index = False) 
            print(f"✅ Successfully loaded insurance claims dataset with {len(insurance_claims_data)} rows")
        except Exception as e:
            print(f"❌ Error loading insurance claims dataset: {str(e)}")
            
    finally:
        conn.close()

if __name__ == '__main__':
    try:
        print("Starting database build process...")
        create_database()
        print("\nDatabase build process completed!")
    except Exception as e:
        print(f"\n❌ Critical Error: {str(e)}")
        if os.path.exists('insurance.db'):
            os.remove('insurance.db')
        exit(1)