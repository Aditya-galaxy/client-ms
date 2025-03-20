'''
Graphs module for Client Management System.
Provides visualizations for client data.
'''

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database.db_config import execute_query

class GraphDialog:
    '''Dialog window for displaying data visualizations.'''
    
    def __init__(self, parent):
        '''
        Initialize the graph dialog.
        
        Args:
            parent: Parent tkinter window
        '''
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Client Data Visualization")
        self.dialog.geometry("800x600")
        
        self.create_widgets()
        self.load_data()
    
    def create_widgets(self):
        '''Create and place dialog widgets.'''
        # Graph type selection frame
        control_frame = ttk.LabelFrame(self.dialog, text="Graph Options")
        control_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(control_frame, text="Select Graph Type:").grid(row=0, column=0, padx=10, pady=10)
        
        # Change default value to "preference"
        self.graph_type = tk.StringVar(value="preference")
        
        # Radio buttons for graph types
        graph_types = [
            ("Client Preference", "preference"),
            ("Client Frequency", "frequency"),
            ("Client Balance", "balance")
        ]
        
        for i, (text, value) in enumerate(graph_types):
            ttk.Radiobutton(control_frame, text=text, value=value, 
                           variable=self.graph_type).grid(row=0, column=i+1, padx=10, pady=10)
        
        # Graph display frame
        self.graph_frame = ttk.LabelFrame(self.dialog, text="Graph")
        self.graph_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Generate button
        generate_btn = ttk.Button(control_frame, text="Generate Graph", command=self.generate_graph)
        generate_btn.grid(row=0, column=len(graph_types)+1, padx=10, pady=10)
        
        # Close button
        close_btn = ttk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        close_btn.pack(pady=10)
        
        # Store data
        self.client_data = None
    
    def load_data(self):
        '''Load client data from database.'''
        query = "SELECT * FROM patron"
        self.client_data = execute_query(query, fetch=True)
        
        # Generate initial graph
        if self.client_data:
            self.generate_graph()
        else:
            ttk.Label(self.graph_frame, text="No data available").pack(pady=50)
    
    def generate_graph(self):
        '''Generate and display graph based on selected type.'''
        if not self.client_data:
            return
            
        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Create figure and axis
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Extract data based on selected graph type
        graph_type = self.graph_type.get()
        
        if graph_type == "frequency":
            # Frequency graph with discrete x-axis
            ids = [str(client[0]) for client in self.client_data]  # Convert IDs to strings
            frequencies = [client[5] for client in self.client_data]
            
            ax.bar(ids, frequencies)
            ax.set_title('Client Visit Frequency')
            ax.set_xlabel('Client ID')
            ax.set_ylabel('Frequency')
            # Set x-axis ticks explicitly
            ax.set_xticks(range(len(ids)))
            ax.set_xticklabels(ids)
            
        elif graph_type == "balance":
            # Balance graph with discrete x-axis
            ids = [str(client[0]) for client in self.client_data]  # Convert IDs to strings
            balances = [client[2] for client in self.client_data]
            
            ax.bar(ids, balances, color='green')
            ax.set_title('Client Balance')
            ax.set_xlabel('Client ID')
            ax.set_ylabel('Balance')
            # Set x-axis ticks explicitly
            ax.set_xticks(range(len(ids)))
            ax.set_xticklabels(ids)
            
        elif graph_type == "preference":
            # Preference distribution
            preferences = {}
            for client in self.client_data:
                pref = client[4]
                if pref in preferences:
                    preferences[pref] += 1
                else:
                    preferences[pref] = 1
            
            labels = list(preferences.keys())
            counts = list(preferences.values())
            
            ax.pie(counts, labels=labels, autopct='%1.1f%%')
            ax.set_title('Client Preferences Distribution')
        
        # Add some padding to prevent label cutoff
        plt.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def run(self):
        '''Run the graph dialog.'''
        self.dialog.grab_set()  # Make this window modal
        self.dialog.wait_window()  # Wait until this window is closed

def show_graphs(parent):
    '''
    Open the graph dialog.
    
    Args:
        parent: Parent tkinter window
    '''
    dialog = GraphDialog(parent)
    dialog.run()