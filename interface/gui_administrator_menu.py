"""
EmpowerU
This file contains the class definition for the AdministratorMenu class.
"""

# Third party imports
import tkinter as tk
from interface.gui_register_student_menu import RegisterStudents
from interface.gui_register_admin_menu import RegisterAdmins
from interface.gui_register_lecturer_menu import RegisterLecturers

class AdministratorMenu(tk.Frame):

    def __init__(self, master, administrator_user):
        """
        Constructor for the AdministratorMenu

        Parameter(s):
        - master: master widget of this widget instance
        - Administrator_user: an instance of the AdministratorUser class
                             representing the Administrator that has 
                             successfully logged in
        """
        super().__init__(master=master)
        self.master = master
        self.administrator_user = administrator_user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {administrator_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)

        self.register_student_btn = tk.Button(self, text="Register a student", command=self.show_register_student_frame)
        self.register_student_btn.pack(padx=10, pady=10)

        self.register_admin_btn = tk.Button(self, text="Register an admin", command=self.show_register_admin_frame)
        self.register_admin_btn.pack(padx=10, pady=10)

        self.register_lecturer_btn = tk.Button(self, text="Register a lecturer", command=self.show_register_lecturer_frame)
        self.register_lecturer_btn.pack(padx=10, pady=10)

        self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
        self.logout_btn.pack(padx=10, pady=10)

    def show_register_student_frame(self):
        """
        Method to handle the search lecturers functionality upon button click.
        """
        register_students = RegisterStudents(self.master, self, self.administrator_user)
        register_students.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_register_admin_frame(self):
        """
        Method to handle the search lecturers functionality upon button click.
        """
        register_admins = RegisterAdmins(self.master, self, self.administrator_user)
        register_admins.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_register_lecturer_frame(self):
        """
        Method to handle the search lecturers functionality upon button click.
        """
        register_lecturers = RegisterLecturers(self.master, self, self.administrator_user)
        register_lecturers.place(relx=.5, rely=.5, anchor=tk.CENTER)
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
        Method to show the Administrator menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the Administrator menu frame.
        """
        self.place_forget()


if __name__ == "__main__":
    # DO NOT MODIFY
    pass