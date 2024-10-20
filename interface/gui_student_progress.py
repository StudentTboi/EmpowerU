"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the SearchTeachers class.
"""

# Third party imports
import tkinter as tk
import app.app_utils as util
from functools import partial
from interface.gui_progress import Progress

class StudentProgress(tk.Frame):
    def __init__(self, master, menu, user):
        """
        Constructor for the SearchTeachers class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.menu = menu
        self.user = user
        
        # Instrument label widget
        self.view_label = tk.Label(master=self, text="View student information:")
        self.view_label.grid(row=1, columnspan=2, sticky=tk.S, padx=10, pady=10)

        self.show_student_list()
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=10, column=1, padx=10, pady=10, sticky=tk.E)
        
    def show_student_list(self):
        self.student_buttons = []
        for index,student in enumerate(self.user.students):
            show_edit_student_info_with_student = partial(self.show_chosen_student_info, student)
            new_button = tk.Button(master=self, text=f"{student.first_name} {student.last_name}", command=show_edit_student_info_with_student)
            new_button.grid(row=index+2, column=0, padx=10, pady=10, sticky=tk.E)
            self.student_buttons.append(new_button)

    def show_chosen_student_info(self, student_to_show):
        view_student_progress = Progress(self.master, self.menu, student_to_show)
        view_student_progress.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    
    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.administrator_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)

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
