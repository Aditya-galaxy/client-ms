# Client Management System

A simple client management system built with Python and MySQL. The application provides functionality to manage client records using CRUD operations to the MySQL database. It also includes data visualization capabilities using charts.

## Features

- Secure login system
- Display all client records
- Add new client records
- Search for specific client records
- Modify existing client information
- Delete client records
- Visualize client data with graphs

## Requirements

- Python 3.10 or higher
- MySQL
- Required Python libraries:
  - mysql-connector-python
  - matplotlib
  - tkinter
  - python-dotenv

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/Aditya-galaxy/client-management.git
   cd client-management
   ```

2. Install required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up MySQL database:

   ```
   mysql -u root -p
   ```

   In MySQL console:

   ```sql
   CREATE DATABASE Client_Management;
   USE Client_Management;
   CREATE TABLE patron (
       PAT_ID INT PRIMARY KEY,
       PAT_NAME VARCHAR(50),
       PAT_BALANCE FLOAT,
       PAT_CONTACT INT,
       PAT_PREFERENCE VARCHAR(50),
       PAT_FREQUENCY INT
   );
   ```

4. Configure database connection in .env file or add details to `database/db_config.py`

## Usage

Run the main application:

```
python3 main.py
```

Login with default credentials:

- Username: 1
- Password: 2

## Project Structure

- `main.py`: Entry point of the application
- `database/`: Database configuration and connection management
- `forms/`: UI forms including login and record adding forms
- `operations/`: Core functionality modules (display, search, modify, delete, graphs)
