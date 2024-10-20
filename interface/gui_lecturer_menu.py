"""
EmpowerU

This file contains the class definition for the LecturerMenu class.
"""

# Third party imports
import tkinter as tk
from interface.gui_course_materials import CourseMaterials
from interface.gui_student_progress import StudentProgress
from interface.gui_enroll_student import StudentEnroll

class LecturerMenu(tk.Frame):

    def __init__(self, master, lecturer_user):
        """
        Constructor for the AdministratorMenu

        Parameter(s):
        - master: master widget of this widget instance
        - Lecturer_user: an instance of the LecturerUser class
                             representing the Lecturer that has 
                             successfully logged in
        """
        super().__init__(master=master)
        self.master = master
        self.lecturer_user = lecturer_user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {lecturer_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)

        self.search_btn = tk.Button(self, text="Edit content", command=self.show_editor_frame)
        self.search_btn.pack(padx=10, pady=10)

        self.enroll_student_btn = tk.Button(self, text="Enroll students to units", command=self.show_enroll_studnet_units_frame)
        self.enroll_student_btn.pack(padx=10, pady=10)

        self.view_progress_btn= tk.Button(self, text="View Student's Progress", command=self.show_student_progress_frame)
        self.view_progress_btn.pack(padx=10,pady=10)

        self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
        self.logout_btn.pack(padx=10, pady=10)

    def show_student_progress_frame(self):
        """
        Method to handle the student's progress functionality upon button click.
        """
        show_students_progress = StudentProgress(self.master, self, self.lecturer_user)
        show_students_progress.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_enroll_studnet_units_frame(self):
        """
        Method to handle the students enrollment functionality upon button click.
        """
        show_students_progress = StudentEnroll(self.master, self, self.lecturer_user)
        show_students_progress.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_editor_frame(self):
        """
        Method to handle the search lecturers functionality upon button click.
        """
        edit_course = CourseMaterials(self.master, self, self.lecturer_user)
        edit_course.place(relx=.5, rely=.5, anchor=tk.CENTER)
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
        Method to show the Lecturer menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the Lecturer menu frame.
        """
        self.place_forget()


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
