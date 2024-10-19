"""
EmpowerU

This file contains the class definition for the CourseMaterials class.
"""

# Third party imports
import tkinter as tk
import app.app_utils as util
from functools import partial
from interface.gui_in_course import CourseMenu
from app.app_course import Course

class CourseMaterials(tk.Frame):

    def __init__(self, master, menu, user):
      
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {user.first_name}!")
        self.welcome_label.grid(row=1, columnspan=2, sticky=tk.S, padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.grid(row=2, columnspan=2, sticky=tk.S, padx=10, pady=10)

        self.show_materials()

        # Return to menu button
        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=10, column=1, padx=10, pady=10, sticky=tk.E)
            
    def show_materials(self):
        self.course_buttons = []
        for index,courses in enumerate(self.user.specialization):
            show_chosen_materials_with_user = partial(self.show_chosen_materials,courses)
            new_button = tk.Button(master=self, text=f"{courses}", command=show_chosen_materials_with_user)
            new_button.grid(row=index+3, column=0, padx=10, pady=10, sticky=tk.E)
            self.course_buttons.append(new_button)

    def show_chosen_materials(self, courses):
        if courses =="AI":
            self.show_course(Course("AI"))
        elif courses=="InfoSec":
            self.show_infosec_materials()
        elif courses=="PyLearn":
            self.show_pylearn_materials()

    def show_course(self, course):
        """
        Method to handle the course materials upon button click.
        """
        ai_materials = CourseMenu(self.master, self, self.user, course)
        ai_materials.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_menu(self):
        """
        Method to show the menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the menu frame.
        """
        self.place_forget()

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

