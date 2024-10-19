"""
EmpowerU

This file contains the class definition for the StudentMenu class.
"""

# Third party imports
import tkinter as tk
from interface.gui_course_materials import CourseMaterials
from interface.gui_progress import Progress

class StudentMenu(tk.Frame):

    def __init__(self, master, student_user):
        """
        Constructor for the StudentMenu

        Parameter(s):
        - master: master widget of this widget instance
        - Studentr_user: an instance of the StudentUser class
                             representing the Student that has 
                             successfully logged in
        """
        super().__init__(master=master)
        self.master = master
        self.student_user = student_user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {student_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)

        self.search_btn = tk.Button(self, text="Progress Checker", command=self.show_progress_page)
        self.search_btn.pack(padx=10, pady=10)

        self.class_btn = tk.Button(self, text="Access Course materials", command=self.show_course_materials)
        self.class_btn.pack(padx=10, pady=10)

        self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
        self.logout_btn.pack(padx=10, pady=10)

    def show_progress_page(self):
        access_progress = Progress(self.master, self, self.student_user)
        access_progress.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()


    def show_course_materials(self):
        access_materials = CourseMaterials(self.master, self, self.student_user)
        access_materials.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def logout(self):
        """
        Method to handle the logout upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.hide_menu()
        self.master.show_homepage()

    def show_menu(self):
        """
        Method to show the Student menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the Student menu frame.
        """
        self.place_forget()


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
