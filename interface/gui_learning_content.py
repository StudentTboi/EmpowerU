import tkinter as tk
import app.app_utils as util
from functools import partial
from app.app_course import Course

class ReadingMaterialMenu(tk.Frame):
    def __init__(self, master, menu, user, course):
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user
        self.course = course

        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
 
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
                
        mylist = tk.Text(self)
        # scrollbar = tk.Scrollbar(mylist, orient=tk.VERTICAL, command=mylist.yview )
        # scrollbar.grid(row=0, column=1, sticky=tk.NS)
        # mylist.configure(yscrollcommand = scrollbar.set )
        mylist.grid(row=0, column=0, sticky="news")
        for line in course.reading_materials:
            mylist.insert(tk.END, line)
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to course menu", command=self.return_to_menu)
        self.return_button.grid(row=1, columnspan=2, sticky=tk.S, padx=10, pady=10)


    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.grid_forget()
        self.menu.place(relx=.5, rely=.5, anchor=tk.CENTER)