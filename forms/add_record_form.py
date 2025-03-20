'''
Add Record form module for the Client Management System.
Provides the UI for adding new client records.
'''

import tkinter as tk
import tkinter.messagebox as MessBox
from database.db_config import execute_query

class AddRecordForm:
    '''
    Form for adding new client records to the database.
    '''
    
    def __init__(self):
        '''Initialize the Add Record form.'''
        self.root = tk.Toplevel()
        self.root.geometry("600x350")
        self.root.title("Add New Client Record")
        self.root.resizable(False, False)
        
        # Create form fields
        self.create_widgets()
    
    def create_widgets(self):
        '''Create and place all form widgets.'''
        # Field labels and entries
        fields = [
            ("Enter Pat_ID:", "id"),
            ("Enter Pat_Name:", "name"),
            ("Enter Pat_Balance:", "balance"),
            ("Enter PAT_Contact:", "contact"),
            ("Enter PAT_Preference:", "preference"),
            ("Enter PAT_Frequency:", "frequency")
        ]
        
        self.entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            # Create label
            label = tk.Label(self.root, text=label_text, font=('Helvetica', 14, 'bold'))
            label.place(x=40, y=40 + i*40)
            
            # Create entry
            entry = tk.Entry(self.root, width=30)
            entry.place(x=200, y=40 + i*40)
            
            # Store entry reference
            self.entries[field_name] = entry
        
        # Add record button
        add_btn = tk.Button(self.root, text="Add Record", 
                           bg="#4CAF50", fg="black",
                           font=("Helvetica", 15), 
                           command=self.add_record)
        add_btn.place(x=200, y=290)
        
        # Cancel button
        cancel_btn = tk.Button(self.root, text="Cancel", 
                              bg="#f44336", fg="black",
                              font=("Helvetica", 15), 
                              command=self.root.destroy)
        cancel_btn.place(x=320, y=290)
    
    def add_record(self):
        '''Add a new record to the database.'''
        try:
            # Get values from entries
            pat_id = int(self.entries["id"].get())
            pat_name = self.entries["name"].get()
            pat_balance = float(self.entries["balance"].get())
            pat_contact = int(self.entries["contact"].get())
            pat_preference = self.entries["preference"].get()
            pat_frequency = int(self.entries["frequency"].get())
            
            # Validate inputs
            if not pat_name or not pat_preference:
                MessBox.showwarning("Validation Error", "All fields must be filled")
                return
            
            # Insert query
            query = '''
                INSERT INTO patron 
                (PAT_ID, PAT_NAME, PAT_BALANCE, PAT_CONTACT, PAT_PREFERENCE, PAT_FREQUENCY) 
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            params = (pat_id, pat_name, pat_balance, pat_contact, pat_preference, pat_frequency)
            
            # Execute query
            result = execute_query(query, params, commit=True)
            
            if result is not None:  # None means error occurred
                # Clear all entries
                for entry in self.entries.values():
                    entry.delete(0, 'end')
                    
                MessBox.showinfo("Success", "Record added successfully")
        
        except ValueError:
            MessBox.showerror("Input Error", "Please enter valid numeric values for ID, Balance, Contact and Frequency")
        except Exception as e:
            MessBox.showerror("Error", f"An error occurred: {str(e)}")
    
    def run(self):
        '''Run the Add Record form.'''
        self.root.grab_set()  # Make this window modal
        self.root.focus_set()
        self.root.wait_window()  # Wait until this window is closed