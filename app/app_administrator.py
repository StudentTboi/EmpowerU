import os
from ast import literal_eval
from app.app_user import User
from app.app_lecturer import LecturerUser
from app.app_student import StudentUser
import app.app_utils as util

class AdministratorUser(User):
    """
    Represents an administrator with methods for authentication, 
    and managing lecturer and student data.
    """

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Authenticates an admin by comparing input credentials with stored data.
        """
        admin_path = "./authenticate/admins.txt"
        lines = util.read_file(admin_path)
        if lines:
            for line in lines:
                if len(line) < 5:  # Skip invalid lines
                    print(f"WARNING: A line in {admin_path} is invalid")
                    continue
                admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password = line.strip("\n").split(";")
                
                if input_username == username and input_password == password:
                    return AdministratorUser(admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
            else:
                print(f"Please check if the file {admin_path} exists.")
        return None

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Initializes an AdministratorUser object and imports teacher and student data.
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.import_teacher_student_data()

    def import_admins_data(self):
        """
        Imports admins data into the admin's session.
        """
        self.admins = []
        admins_path = "./authenticate/admins.txt"
        lines = util.read_file(admins_path)
        if lines:
            for line in lines:
                if len(line)<6:
                    continue
                admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password = line.strip("\n").split(";")
                admin_obj = AdministratorUser(admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
                self.admins.append(admin_obj)


    def import_teacher_student_data(self):
        """
        Imports lecturer and student data into the admin's session.
        """
        self.import_lecturers_data()
        self.import_students_data()

    def import_lecturers_data(self):
        """
        Imports lecturer data from a file and stores it.
        """
        self.lecturers = []
        lecturers_path = "./authenticate/lecturers.txt"
        lines = util.read_file(lecturers_path)
        if lines:
            for line in lines:
                if len(line) < 6:
                    continue
                lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                lecturer_obj = LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
                self.lecturers.append(lecturer_obj)

    def import_students_data(self):
        """
        Imports student data from a file and stores it.
        """
        self.students = []
        students_path = "./authenticate/students.txt"
        lines = util.read_file(students_path)
        if lines:
            for line in lines:
                if len(line) < 6:
                    continue
                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                course_progress = literal_eval(course_progress)
                student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress)
                self.students.append(student_obj)

    def store_student_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Registers a new student and saves their data to a file.
        """
        student_id = "s" + str(len(self.students) + 1).zfill(4)
        student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        filepath = "./authenticate/students.txt"
        new_student_line = f"{student_id};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password},\n"
        
        if util.append_to_file(filepath, new_student_line):
            self.students.append(student_obj)
            return True
        return False

    def store_lecturer_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization):
        """
        Registers a new lecturer and saves their data to a file.
        """
        lecturer_id = "l" + str(len(self.lecturers) + 1).zfill(2)
        lecturer_obj = LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
        filepath = "./authenticate/lecturers.txt"
        new_lecturer_line = f"{lecturer_id};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password};{specialization}\n"
        
        if util.append_to_file(filepath, new_lecturer_line):
            self.students.append(lecturer_obj)
            return True
        return False

    def edit_student_data(self, student_to_edit, **kwargs):
        """
        Edits existing student data based on provided parameters.
        """
        filepath = "./authenticate/students.txt"
        for attr, value in kwargs.items():
            setattr(student_to_edit, attr, value)
        
        new_student_line = f"{student_to_edit.uid};{student_to_edit.first_name};{student_to_edit.last_name};{student_to_edit.date_of_birth};{student_to_edit.contact_num};{student_to_edit.contact_email};{student_to_edit.username};{student_to_edit.password};{student_to_edit.specialization};{student_to_edit.course_progress}\n"
        return util.overwrite_file_at_line(filepath, int(student_to_edit.uid[1:])-1, new_student_line)

    def edit_lecturer_data(self, lecturer_to_edit, **kwargs):
        """
        Edits existing lecturer data based on provided parameters.
        """
        filepath = "./authenticate/lecturers.txt"
        for attr, value in kwargs.items():
            setattr(lecturer_to_edit, attr, value)

        new_lecturer_line = f"{lecturer_to_edit.uid};{lecturer_to_edit.first_name};{lecturer_to_edit.last_name};{lecturer_to_edit.date_of_birth};{lecturer_to_edit.contact_num};{lecturer_to_edit.contact_email};{lecturer_to_edit.username};{lecturer_to_edit.password};{lecturer_to_edit.specialization}\n"
        return util.overwrite_file_at_line(filepath, int(lecturer_to_edit.uid[1:])-1, new_lecturer_line)
