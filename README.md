# Client Management System

A simple client management system built with Python and MySQL. The application provides functionality to manage client records including adding, modifying, deleting, and searching records from the MySQL database. It also includes data visualization capabilities using charts.

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
- MySQL 8.0 or higher
- Required Python libraries:
  - mysql-connector-python
  - matplotlib
  - tkinter
  - python-dotenv

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Aditya-galaxy/client-management.git
   cd client_ms
   ```

2. Create and activate virtual environment:

   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up MySQL database:

   ```bash
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

5. Configure database connection:

   Create a `.env` file in the project root:

   ```bash
   touch .env
   ```

   Add database configuration to `.env`:

   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=Client_Management
   ```

## Usage

1. Ensure virtual environment is activated:

   ```bash
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   ```

2. Run the main application:

   ```bash
   python main.py
   ```

3. Login with default credentials:
   - Username: 1
   - Password: 2

## Project Structure

```
client_ms/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── main.py              # Application entry point
├── database/           # Database configuration
│   ├── __init__.py
│   └── db_config.py
├── forms/             # UI forms
│   ├── __init__.py
│   ├── login_form.py
│   └── add_record_form.py
└── operations/        # Core functionality
    ├── __init__.py
    ├── display.py
    ├── search.py
    ├── modify.py
    ├── delete.py
    └── graphs.py
```

## Development

1. To modify database configuration, edit `.env` file
2. For testing, use the provided dummy data or add your own records
3. Changes to UI can be made in respective form files
4. Core operations are modular and can be extended

## Troubleshooting

1. Database connection issues:

   - Verify MySQL is running
   - Check credentials in `.env` file
   - Ensure database and table exist

2. Package issues:

   - Verify virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

3. Display issues:
   - Check Tkinter installation
   - Verify Python version compatibility
