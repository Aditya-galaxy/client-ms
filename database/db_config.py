'''
Database configuration module for the Client Management System.
Contains the database connection parameters and utility functions.
'''

import os
from dotenv import load_dotenv
import mysql.connector as rt
import tkinter.messagebox as MessBox

# Load environment variables
load_dotenv()

# Database configuration using environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'Client_Management')
}

def get_connection():
    '''
    Establishes and returns a connection to the MySQL database.
    
    Returns:
        connection: MySQL connection object
    '''
    try:
        conn = rt.connect(**DB_CONFIG)
        return conn
    except rt.Error as err:
        MessBox.showerror("Database Connection Error", f"Failed to connect to database: {err}")
        return None

def execute_query(query, params=None, fetch=False, commit=False):
    '''
    Executes a SQL query with optional parameters.
    
    Args:
        query (str): SQL query to execute
        params (tuple, optional): Parameters for the query
        fetch (bool): Whether to fetch results
        commit (bool): Whether to commit the transaction
    
    Returns:
        List of query results if fetch=True, else None
    '''
    conn = get_connection()
    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        result = None
        if fetch:
            result = cursor.fetchall()
        
        if commit:
            conn.commit()
        
        return result
    except rt.Error as err:
        MessBox.showerror("Database Error", f"Error executing query: {err}")
        return None
    finally:
        cursor.close()
        conn.close()