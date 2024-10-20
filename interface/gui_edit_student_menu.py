"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the SearchTeachers class.
"""

# Third party imports
import tkinter as tk
import app.app_utils as util
from functools import partial

class EditStudents(tk.Frame):
    def __init__(self, master, administrator_menu, administrator_user):
        """
        Constructor for the SearchTeachers class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.administrator_menu = administrator_menu
        self.administrator_user = administrator_user
        
        # Instrument label widget
        self.instrument_label = tk.Label(master=self, text="Edit student information:")
        self.instrument_label.grid(row=1, columnspan=2, sticky=tk.S, padx=10, pady=10)

        self.show_student_list()
        self.show_editables()
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=10, column=1, padx=10, pady=10, sticky=tk.E)
        
    def show_student_list(self):
        self.student_buttons = []
        for index,student in enumerate(self.administrator_user.students):
            show_edit_student_info_with_student = partial(self.show_edit_student_info, student)
            new_button = tk.Button(master=self, text=f"{student.first_name} {student.last_name}", command=show_edit_student_info_with_student)
            new_button.grid(row=index+2, column=0, padx=10, pady=10, sticky=tk.E)
            self.student_buttons.append(new_button)

    def show_editables(self):
        # First name label widget
        self.firstname_label = tk.Label(master=self, text="First name:")
        self.firstname_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)
        # First name variable and entry widget
        self.firstname_var = tk.StringVar(master=self)
        self.firstname_entry = tk.Entry(master=self, textvariable=self.firstname_var)
        self.firstname_entry.grid(row=2, column=2, padx=10, pady=10, sticky=tk.E)

        # Last name label widget
        self.lastname_label = tk.Label(master=self, text="Last name:")
        self.lastname_label.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)
        # Last name variable and entry widget
        self.lastname_var = tk.StringVar(master=self)
        self.lastname_entry = tk.Entry(master=self, textvariable=self.lastname_var)
        self.lastname_entry.grid(row=3, column=2, padx=10, pady=10, sticky=tk.E)

        # Date of birth label widget
        self.dob_label = tk.Label(master=self, text="Date of birth:")
        self.dob_label.grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)
        # Date of birth variable and entry widget
        self.dob_var = tk.StringVar(master=self)
        self.dob_entry = tk.Entry(master=self, textvariable=self.dob_var)
        self.dob_entry.grid(row=4, column=2, padx=10, pady=10, sticky=tk.E)

        # Contact number label widget
        self.contact_num_label = tk.Label(master=self, text="Contact number:")
        self.contact_num_label.grid(row=5, column=1, padx=10, pady=10, sticky=tk.E)
        # Contact number variable and entry widget
        self.contact_num_var = tk.StringVar(master=self)
        self.contact_num_entry= tk.Entry(master=self, textvariable=self.contact_num_var)
        self.contact_num_entry.grid(row=5, column=2, padx=10, pady=10, sticky=tk.E)
        
        # Contact email label widget
        self.contact_email_label = tk.Label(master=self, text="Contact email:")
        self.contact_email_label.grid(row=6, column=1, padx=10, pady=10, sticky=tk.E)
        # Contact email variable and entry widget
        self.contact_email_var = tk.StringVar(master=self)
        self.contact_email_entry= tk.Entry(master=self, textvariable=self.contact_email_var)
        self.contact_email_entry.grid(row=6, column=2, padx=10, pady=10, sticky=tk.E)
        
        # Username label widget
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=7, column=1, padx=10, pady=10, sticky=tk.E)
        # Username variable and entry widget
        self.username_var = tk.StringVar(master=self)
        self.username_entry= tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=7, column=2, padx=10, pady=10, sticky=tk.E)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=8, column=1, padx=10, pady=10, sticky=tk.E)
        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry= tk.Entry(master=self, textvariable=self.password_var)
        self.password_entry.grid(row=8, column=2, padx=10, pady=10, sticky=tk.E)

        # Alert variable and label widget
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var)
        self.alert_label.grid(row=9, columnspan=3, sticky=tk.S, padx=10, pady=10)

    def show_edit_student_info(self, student_to_edit):
        if hasattr(self, 'edit_button'):
            self.edit_button.destroy()

        self.firstname_var.set(student_to_edit.first_name)
        self.lastname_var.set(student_to_edit.last_name)
        self.dob_var.set(student_to_edit.date_of_birth)
        self.contact_num_var.set(student_to_edit.contact_num)
        self.contact_email_var.set(student_to_edit.contact_email)
        self.username_var.set(student_to_edit.username)
        self.password_var.set(student_to_edit.password)
        
        # Button to login
        self.edit_button = tk.Button(master=self, text="Edit", command= lambda: self.edit_student(student_to_edit))
        self.edit_button.grid(row=10, column=0, padx=10, pady=10, sticky=tk.E)

    def edit_student(self, student_to_edit):
        """
        Handles the registration process of a student into the management system.
        The system should prompt the user for
            - the student's first name,
            - the student's last name,
            - the student's date of birth in DD/MM/YYYY format,
            - the contact number (of the student or the contact person)

        Parameters:
        receptionist: an instance of the Receptionist class

        Returns:
        (None)
        """
        if not util.is_valid_first_name(self.firstname_var.get()):
            self.alert_var.set("Invalid first name!")
            self.firstname_entry.delete(0,"end")
        elif not util.is_valid_date_format(self.dob_var.get()):
            self.alert_var.set("Invalid date of birth!")
            self.dob_entry.delete(0,"end")
        elif not util.is_valid_contact_number(self.contact_num_var.get()):
            self.alert_var.set("Invalid contact number!")
            self.contact_num_entry.delete(0,"end")
        elif self.administrator_user.edit_student_data(student_to_edit, self.firstname_var.get(), self.lastname_var.get(), self.dob_var.get(), self.contact_num_var.get(), self.contact_email_var.get(), self.username_var.get(), self.password_var.get()):
            self.alert_var.set("Successfully edited student information")
            self.firstname_entry.delete(0,"end")
            self.lastname_entry.delete(0,"end")
            self.dob_entry.delete(0,"end")
            self.contact_num_entry.delete(0,"end")
            self.contact_email_entry.delete(0,"end")
            self.username_entry.delete(0,"end")
            self.password_entry.delete(0,"end")
            self.edit_button.destroy()
        else:
            self.alert_var.set("ERROR")
    
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

if __name__ == "__main__":
    # DO NOT MODIFY
    pass