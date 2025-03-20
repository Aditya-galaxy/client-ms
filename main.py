'''
Client Management System
Main application module that integrates all components.

This application provides functionality to manage client records including:
- Display all records
- Add new records
- Search for specific records
- Modify existing records
- Delete records
- Visualize data with graphs
'''

import tkinter as tk
from tkinter import ttk, font

from forms import LoginForm, AddRecordForm
from operations import (
    display_records_formatted,
    search_record,
    modify_record,
    delete_record,
    show_graphs
)

class ClientManagementApp:
    '''Main application class for Client Management System.'''
    
    def __init__(self):
        '''Initialize the application.'''
        # Start with login form
        self.login()
    
    def login(self):
        '''Show login form and proceed if authentication successful.'''
        login_form = LoginForm(self.create_main_window)
        login_form.run()
    
    def create_main_window(self):
        '''Create the main application window after successful login.'''
        self.root = tk.Tk()
        self.root.title("Client Management System")
        self.root.geometry("1020x700")
        self.root.minsize(800, 600)
        
        # Configure styles
        self.configure_styles()
        
        # Create main layout
        self.create_layout()
        
        # Start the application
        self.root.mainloop()
    
    def configure_styles(self):
        '''Configure application styles.'''
        # Fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.menu_font = font.Font(family="Helvetica", size=12)
        self.content_font = font.Font(family="Helvetica", size=10)
        
        # Colors
        self.root.configure(bg="#f0f0f0")
    
    def create_layout(self):
        '''Create the main application layout.'''
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Menu frame (left side)
        menu_frame = ttk.LabelFrame(main_container, text="Menu")
        menu_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        # Content frame (right side)
        content_frame = ttk.Frame(main_container)
        content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Create menu buttons
        self.create_menu(menu_frame)
        
        # Create content area
        self.create_content_area(content_frame)
    
    def create_menu(self, parent):
        '''
        Create menu buttons in the left panel.
        
        Args:
            parent: Parent frame to place menu buttons
        '''
        # Menu options
        menu_options = [
            ("Display Records", self.display_records),
            ("Add Record", self.add_record),
            ("Search Records", self.search_records),
            ("Modify Record", self.modify_record),
            ("Delete Record", self.delete_record),
            ("Show Graphs", self.show_graphs),
            ("Exit", self.root.destroy)
        ]
        
        # Create buttons
        for text, command in menu_options:
            btn = ttk.Button(parent, text=text, command=command, width=20)
            btn.pack(pady=5, padx=10)
    
    def create_content_area(self, parent):
        '''
        Create the content area on the right side.
        
        Args:
            parent: Parent frame to place content
        '''
        # Title
        title_label = ttk.Label(parent, text="Client Management System", font=self.title_font)
        title_label.pack(pady=10)
        
        # Output text area
        self.output_area = tk.Text(parent, height=35, width=80, font=self.content_font)
        self.output_area.pack(fill="both", expand=True, pady=10)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.output_area, command=self.output_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.output_area.config(yscrollcommand=scrollbar.set)
        
        # Welcome message
        welcome_msg = "*"
        welcome_msg += "*"
        
        self.output_area.insert("1.0", welcome_msg)
    
    def display_records(self):
        '''Display all client records.'''
        display_records_formatted(self.output_area)
    
    def add_record(self):
        '''Open form to add a new record.'''
        add_form = AddRecordForm()
        add_form.run()
    
    def search_records(self):
        '''Open dialog to search for records.'''
        search_record(self.root)
    
    def modify_record(self):
        '''Open dialog to modify a record.'''
        modify_record(self.root)
    
    def delete_record(self):
        '''Open dialog to delete a record.'''
        delete_record(self.root)
    
    def show_graphs(self):
        '''Open dialog to show data visualizations.'''
        show_graphs(self.root)

if __name__ == "__main__":
    # Start the application
    app = ClientManagementApp()