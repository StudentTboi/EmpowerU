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

        self.label1 = tk.Label(self, text=self.course.reading_materials)
        self.label1.pack(padx=10, pady=10)
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to course menu", command=self.return_to_menu)
        self.return_button.pack(padx=10, pady=10)

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
