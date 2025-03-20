'''
Delete operation module for Client Management System.
Handles deletion of client records.
'''

import tkinter as tk
from tkinter import ttk, messagebox
from database.db_config import execute_query

class DeleteDialog:
    '''Dialog window for deleting client records.'''
    
    def __init__(self, parent):
        '''
        Initialize the delete dialog.
        
        Args:
            parent: Parent tkinter window
        '''
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Delete Client Record")
        self.dialog.geometry("500x300")
        self.dialog.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        '''Create and place dialog widgets.'''
        # Search frame
        search_frame = ttk.LabelFrame(self.dialog, text="Find Record to Delete")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(search_frame, text="Enter Client ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = ttk.Entry(search_frame, width=10)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        find_btn = ttk.Button(search_frame, text="Find Client", command=self.find_client)
        find_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Client info frame
        self.info_frame = ttk.LabelFrame(self.dialog, text="Client Information")
        self.info_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Client info text
        self.info_text = tk.Text(self.info_frame, height=6, width=50, state="disabled")
        self.info_text.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.dialog)
        buttons_frame.pack(fill="x", padx=20, pady=10)
        
        self.delete_btn = ttk.Button(buttons_frame, text="Delete Client", 
                                    command=self.confirm_delete, state="disabled")
        self.delete_btn.pack(side="left", padx=10)
        
        cancel_btn = ttk.Button(buttons_frame, text="Cancel", command=self.dialog.destroy)
        cancel_btn.pack(side="right", padx=10)
        
        # Store client ID
        self.current_client_id = None
        self.client_data = None
    
    def find_client(self):
        '''Find and display client record for deletion.'''
        try:
            client_id = int(self.id_entry.get())
            
            # Query the database
            query = "SELECT * FROM patron WHERE PAT_ID = %s"
            result = execute_query(query, (client_id,), fetch=True)
            
            if not result:
                messagebox.showinfo("Not Found", f"No client found with ID: {client_id}")
                self.info_text.config(state="normal")
                self.info_text.delete(1.0, tk.END)
                self.info_text.config(state="disabled")
                self.delete_btn.config(state="disabled")
                return
            
            # Store client ID and data
            self.current_client_id = client_id
            self.client_data = result[0]
            
            # Display client info
            self.info_text.config(state="normal")
            self.info_text.delete(1.0, tk.END)
            
            # Format client info
            info = f"ID: {self.client_data[0]}\n"
            info += f"Name: {self.client_data[1]}\n"
            info += f"Balance: {self.client_data[2]}\n"
            info += f"Contact: {self.client_data[3]}\n"
            info += f"Preference: {self.client_data[4]}\n"
            info += f"Frequency: {self.client_data[5]}"
            
            self.info_text.insert(tk.END, info)
            self.info_text.config(state="disabled")
            
            # Enable delete button
            self.delete_btn.config(state="normal")
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid client ID")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def confirm_delete(self):
        '''Confirm and delete client record.'''
        if not self.current_client_id:
            return
            
        # Ask for confirmation
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Are you sure you want to delete client '{self.client_data[1]}' (ID: {self.current_client_id})?"
        )
        
        if not confirm:
            return
            
        try:
            # Execute delete query
            query = "DELETE FROM patron WHERE PAT_ID = %s"
            execute_query(query, (self.current_client_id,), commit=True)
            
            messagebox.showinfo("Success", "Client record deleted successfully")
            self.dialog.destroy()
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def run(self):
        '''Run the delete dialog.'''
        self.dialog.grab_set()  # Make this window modal
        self.dialog.wait_window()  # Wait until this window is closed

def delete_record(parent):
    '''
    Open the delete dialog.
    
    Args:
        parent: Parent tkinter window
    '''
    dialog = DeleteDialog(parent)
    dialog.run()