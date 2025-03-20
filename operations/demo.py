'''
Display operation module for Client Management System.
Handles the display of client records.
'''

from database.db_config import execute_query
import tkinter as tk
from tkinter import ttk

def display_records():
    '''
    Fetch all records from the patron table.
    
    Returns:
        list: List of tuples containing patron records
    '''
    query = "SELECT * FROM patron"
    return execute_query(query, fetch=True)

def display_records_formatted(parent_frame):
    '''
    Display all records in a Treeview grid widget.
    
    Args:
        parent_frame: Tkinter Frame to place the Treeview in
    
    Returns:
        ttk.Treeview: The created Treeview widget
    '''
    # Clear any existing widgets in the frame
    for widget in parent_frame.winfo_children():
        widget.destroy()
    
    # Create a frame for the Treeview and scrollbar
    tree_frame = tk.Frame(parent_frame)
    tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Create scrollbar
    y_scrollbar = ttk.Scrollbar(tree_frame)
    y_scrollbar.pack(side="right", fill="y")
    
    # Create the Treeview widget
    tree = ttk.Treeview(tree_frame, yscrollcommand=y_scrollbar.set)
    tree.pack(fill="both", expand=True)
    
    # Configure the scrollbar
    y_scrollbar.config(command=tree.yview)
    
    # Define columns
    tree["columns"] = ("ID", "Name", "Balance", "Contact", "Preference", "Frequency")
    
    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hidden column
    tree.column("ID", width=50, anchor=tk.W)
    tree.column("Name", width=150, anchor=tk.W)
    tree.column("Balance", width=80, anchor=tk.E)
    tree.column("Contact", width=100, anchor=tk.W)
    tree.column("Preference", width=120, anchor=tk.W)
    tree.column("Frequency", width=80, anchor=tk.W)
    
    # Create headings
    tree.heading("#0", text="")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Balance", text="Balance")
    tree.heading("Contact", text="Contact")
    tree.heading("Preference", text="Preference")
    tree.heading("Frequency", text="Frequency")
    
    # Get records
    records = display_records()
    
    if not records:
        # Display a message if no records are found
        tree.insert("", tk.END, values=("No records found", "", "", "", "", ""))
        return tree
    
    # Insert records
    for record in records:
        tree.insert("", tk.END, values=record)
    
    return tree