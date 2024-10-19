import tkinter as tk
from tkinter import ttk
import app.app_utils as util
from functools import partial

class Progress(tk.Frame):
    def __init__(self, master, menu, user):
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user

        self.user_detail_label = tk.Label(self, text=f" {user.first_name} {user.last_name}'s Progress")
        self.user_detail_label.grid(row=0, columnspan=2, padx=10, pady=10, sticky=tk.E)
        
        self.show_progress_detail()

        # Return to menu button
        self.return_button = tk.Button(self, text="Return to course menu", command=self.return_to_menu)
        self.return_button.grid(row=30, columnspan=2, padx=10, pady=10, sticky=tk.E)

    def show_progress_detail(self):
        for index,courses in enumerate(self.user.specialization):
            content_detail = tk.Label(master=self, text=f"{courses} content")
            content_detail.grid(row=index*2+1, column=0, padx=10, pady=10, sticky=tk.E)
            
            content_progress_bar = ttk.Progressbar(self)
            # Updating the progress bar
            content_progress_bar['value'] = 2/4*100
            # Adding the progress bar to the window
            content_progress_bar.grid(row=index*2+1, column=1, padx=10, pady=10, sticky=tk.E)

            quiz_detail = tk.Label(master=self, text=f"{courses} quiz")
            quiz_detail.grid(row=index*2+2, column=0, padx=10, pady=10, sticky=tk.E)

            quiz_progress_bar = ttk.Progressbar(self)
            # Updating the progress bar
            quiz_progress_bar['value'] = 1/5*100
            # Adding the progress bar to the window
            quiz_progress_bar.grid(row=index*2+2, column=1, padx=10, pady=10, sticky=tk.E)


    
    
    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.menu.place(relx=.5, rely=.5, anchor=tk.CENTER)
