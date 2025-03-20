'''
Modify operation module for Client Management System.
Handles modification of client records.
'''

import tkinter as tk
from tkinter import ttk, messagebox
from database.db_config import execute_query

class ModifyDialog:
    '''Dialog window for modifying client records.'''
    
    def __init__(self, parent):
        '''
        Initialize the modify dialog.
        
        Args:
            parent: Parent tkinter window
        '''
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Modify Client Record")
        self.dialog.geometry("700x500")
        self.dialog.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        '''Create and place dialog widgets.'''
        # Search frame for finding the record to modify
        search_frame = ttk.LabelFrame(self.dialog, text="Find Record")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(search_frame, text="Enter Client ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = ttk.Entry(search_frame, width=10)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        find_btn = ttk.Button(search_frame, text="Find Client", command=self.find_client)
        find_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Modification frame
        self.modify_frame = ttk.LabelFrame(self.dialog, text="Modify Client Details")
        self.modify_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Fields for modification
        self.fields = {
            "name": "Client Name",
            "balance": "Balance",
            "contact": "Contact",
            "preference": "Preference",
            "frequency": "Frequency"
        }
        
        self.entries = {}
        row = 0
        
        for field_key, field_label in self.fields.items():
            ttk.Label(self.modify_frame, text=f"{field_label}:").grid(row=row, column=0, padx=10, pady=10, sticky="w")
            entry = ttk.Entry(self.modify_frame, width=30)
            entry.grid(row=row, column=1, padx=10, pady=10)
            self.entries[field_key] = entry
            row += 1
        
        # Initially disable modification fields
        for entry in self.entries.values():
            entry.config(state="disabled")
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.dialog)
        buttons_frame.pack(fill="x", padx=20, pady=10)
        
        save_btn = ttk.Button(buttons_frame, text="Save Changes", command=self.save_changes)
        save_btn.pack(side="left", padx=10)
        
        cancel_btn = ttk.Button(buttons_frame, text="Cancel", command=self.dialog.destroy)
        cancel_btn.pack(side="right", padx=10)
        
        # Store client ID
        self.current_client_id = None
    
    def find_client(self):
        '''Find and load client record for modification.'''
        try:
            client_id = int(self.id_entry.get())
            
            # Query the database
            query = "SELECT * FROM patron WHERE PAT_ID = %s"
            result = execute_query(query, (client_id,), fetch=True)
            
            if not result:
                messagebox.showinfo("Not Found", f"No client found with ID: {client_id}")
                return
            
            # Store client ID and populate fields
            self.current_client_id = client_id
            client_data = result[0]
            
            # Enable and populate fields
            field_mapping = {
                "name": 1,  # Index of PAT_NAME in query result
                "balance": 2,  # Index of PAT_BALANCE in query result
                "contact": 3,  # Index of PAT_CONTACT in query result
                "preference": 4,  # Index of PAT_PREFERENCE in query result
                "frequency": 5   # Index of PAT_FREQUENCY in query result
            }
            
            for field_key, data_index in field_mapping.items():
                self.entries[field_key].config(state="normal")
                self.entries[field_key].delete(0, tk.END)
                self.entries[field_key].insert(0, client_data[data_index])
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid client ID")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def save_changes(self):
        '''Save modified client record to database.'''
        if not self.current_client_id:
            messagebox.showwarning("Error", "No client record loaded")
            return
        
        try:
            # Get updated values
            updates = {}
            conversion_funcs = {
                "name": str,
                "balance": float,
                "contact": int,
                "preference": str,
                "frequency": int
            }
            
            for field, entry in self.entries.items():
                value = entry.get()
                if value:  # Only update non-empty fields
                    updates[field] = conversion_funcs[field](value)
            
            if not updates:
                messagebox.showinfo("No Changes", "No fields were modified")
                return
            
            # Build update query
            field_mapping = {
                "name": "PAT_NAME",
                "balance": "PAT_BALANCE",
                "contact": "PAT_CONTACT",
                "preference": "PAT_PREFERENCE",
                "frequency": "PAT_FREQUENCY"
            }
            
            set_clauses = []
            params = []
            
            for field, value in updates.items():
                set_clauses.append(f"{field_mapping[field]} = %s")
                params.append(value)
            
            # Add client ID to params
            params.append(self.current_client_id)
            
            query = f"UPDATE patron SET {', '.join(set_clauses)} WHERE PAT_ID = %s"
            
            # Execute update
            execute_query(query, params, commit=True)
            
            messagebox.showinfo("Success", "Client record updated successfully")
            self.dialog.destroy()
        
        except ValueError as ve:
            messagebox.showerror("Input Error", "Please check the input values: " + str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def run(self):
        '''Run the modify dialog.'''
        self.dialog.grab_set()  # Make this window modal
        self.dialog.wait_window()  # Wait until this window is closed

def modify_record(parent):
    '''
    Open the modify dialog.
    
    Args:
        parent: Parent tkinter window
    '''
    dialog = ModifyDialog(parent)
    dialog.run()