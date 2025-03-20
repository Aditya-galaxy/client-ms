'''
Login form module for the Client Management System.
Provides the user interface for authentication.
'''

import tkinter as tk
from tkinter import font

class LoginForm:
    '''
    Login form class that creates and manages the login window.
    '''
    
    def __init__(self, on_login_success):
        '''
        Initialize the login form.
        
        Args:
            on_login_success (function): Callback function to execute after successful login
        '''
        self.on_login_success = on_login_success
        
        # Create login window
        self.root = tk.Tk()
        self.root.title("Client Management - Login")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        
        # Configure styles
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        label_font = font.Font(family="Helvetica", size=14)
        entry_font = font.Font(family="Helvetica", size=14)
        
        # Create widgets
        self.create_widgets(title_font, label_font, entry_font)
        
    def create_widgets(self, title_font, label_font, entry_font):
        '''Create and place all widgets in the login form.'''
        # Title
        title_label = tk.Label(self.root, text='Client Management System', font=title_font)
        title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        
        # Username
        user_label = tk.Label(self.root, text='Username:', font=label_font)
        user_label.place(relx=0.3, rely=0.35, anchor=tk.E)
        
        self.user_entry = tk.Entry(self.root, font=entry_font, width=20)
        self.user_entry.place(relx=0.35, rely=0.35, anchor=tk.W)
        
        # Password
        pass_label = tk.Label(self.root, text='Password:', font=label_font)
        pass_label.place(relx=0.3, rely=0.45, anchor=tk.E)
        
        self.pass_entry = tk.Entry(self.root, font=entry_font, width=20, show="*")
        self.pass_entry.place(relx=0.35, rely=0.45, anchor=tk.W)
        
        # Login button
        login_btn = tk.Button(self.root, text="Login", 
                             bg="#4CAF50", fg="black", 
                             font=label_font,
                             width=14, 
                             command=self.verify_login)
        login_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    def verify_login(self):
        '''Verify login credentials.'''
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        # Simple hardcoded authentication (as per original code)
        # In a real application, this should be replaced with secure authentication
        if username == '1' and password == '2':
            self.root.destroy()
            self.on_login_success()
        else:
            error_label = tk.Label(self.root, text="Invalid username or password", 
                                 fg="red", font=("Helvetica", 14))
            error_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    
    def run(self):
        '''Run the login form main loop.'''
        self.root.mainloop()