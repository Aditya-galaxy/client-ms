'''
Search operation module for Client Management System.
Handles the search functionality for client records.
'''

import tkinter as tk
from tkinter import ttk, messagebox
from database.db_config import execute_query

class SearchDialog:
    '''Dialog window for searching client records.'''
    
    def __init__(self, parent):
        '''
        Initialize the search dialog.
        
        Args:
            parent: Parent tkinter window
        '''
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Search Client Records")
        self.dialog.geometry("600x500")
        self.dialog.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        '''Create and place search dialog widgets.'''
        # Search options
        search_frame = ttk.LabelFrame(self.dialog, text="Search Criteria")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        # Search by options
        ttk.Label(search_frame, text="Search by:").grid(row=0, column=0, padx=5, pady=5)
        
        self.search_by = ttk.Combobox(search_frame, values=["ID", "Name", "Preference"])
        self.search_by.grid(row=0, column=1, padx=5, pady=5)
        self.search_by.current(0)  # Default to ID
        
        ttk.Label(search_frame, text="Search value:").grid(row=1, column=0, padx=5, pady=5)
        self.search_value = ttk.Entry(search_frame, width=30)
        self.search_value.grid(row=1, column=1, padx=5, pady=5)
        
        # Search button
        search_btn = ttk.Button(search_frame, text="Search", command=self.perform_search)
        search_btn.grid(row=1, column=2, padx=10, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(self.dialog, text="Search Results")
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Treeview for results
        columns = ("ID", "Name", "Balance", "Contact", "Preference", "Frequency")
        self.tree = ttk.Treeview(results_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Pack tree and scrollbar
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        
        # Close button
        close_btn = ttk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        close_btn.pack(pady=10)
    
    def perform_search(self):
        '''Execute search based on selected criteria and value.'''
        search_type = self.search_by.get()
        search_val = self.search_value.get()
        
        if not search_val:
            messagebox.showwarning("Input Error", "Please enter a search value")
            return
        
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            # Build query based on search type
            if search_type == "ID":
                query = "SELECT * FROM patron WHERE PAT_ID = %s"
                params = (int(search_val),)
            elif search_type == "Name":
                query = "SELECT * FROM patron WHERE PAT_NAME LIKE %s"
                params = (f"%{search_val}%",)
            elif search_type == "Preference":
                query = "SELECT * FROM patron WHERE PAT_PREFERENCE LIKE %s"
                params = (f"%{search_val}%",)
            
            # Execute search
            results = execute_query(query, params, fetch=True)
            
            # Display results
            if not results:
                messagebox.showinfo("Search Results", "No matching records found")
            else:
                for row in results:
                    self.tree.insert("", "end", values=row)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid ID number")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def run(self):
        '''Run the search dialog.'''
        self.dialog.grab_set()  # Make this window modal
        self.dialog.wait_window()  # Wait until this window is closed

def search_record(parent):
    '''
    Open the search dialog.
    
    Args:
        parent: Parent tkinter window
    '''
    dialog = SearchDialog(parent)
    dialog.run()