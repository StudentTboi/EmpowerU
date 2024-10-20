import os

from ast import literal_eval

from app.app_user import User
from app.app_lecturer import LecturerUser
from app.app_student import StudentUser
import app.app_utils as util

class AdministratorUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        admin_path = "./authenticate/admins.txt"
        lines = util.read_file(admin_path)
        if lines:
            for line in lines:
                if len(line)<5: #Checking if line is invalid
                    print(f"WARNING: A line in {admin_path} is invalid")
                    continue
                
                admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password = line.strip("\n").split(";")
                
                if input_username == username:
                    if input_password == password:
                        return AdministratorUser(admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, input_username, input_password)
                    else:
                        return None # or return, or break

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.import_teacher_student_data()

    def import_teacher_student_data(self):
        """
        Method to read all data by calling methods to read teachers data and students data.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.import_lecturers_data()
        self.import_students_data()

    def import_lecturers_data(self):
        """
        Method to read lecturers data and store it into the admin's session.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.lecturers = []
        lecturers_path = "./authenticate/lecturers.txt"
        lines = util.read_file(lecturers_path)
        if lines:
            for line in lines:
                if len(line)<6:
                    continue
                lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                lecturer_obj = LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
                self.lecturers.append(lecturer_obj)

    def import_students_data(self):
        """
        Method to read students data and store it into the admin's session.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.students = []
        students_path = "./authenticate/students.txt"
        lines = util.read_file(students_path)
        if lines:
            for line in lines:
                if len(line)<6:
                    continue
                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                course_progress = literal_eval(course_progress)
                student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress)
                self.students.append(student_obj)

    def import_admins_data(self):
        """
        Method to read admins data and store it into the admin's session.

        Parameter(s):
        (None)

        Returns:
        (None)
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

    def store_student_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Method to register the student in the system 
        and write the data of the new student into the file.

        Parameter(s):
        - first_name: str, student's first name
        - last_name: str, student's last name
        - date_of_birth: str, student's date of birthwdawd
        - contact_num: str, contact number of either student or contact person
        Returns:
        - bool: True if student data is stored from the system into the txt file, 
                False otherwise
        """

        # Create the Student object
        # Assume no skips in student ID
        student_id = "s" + str(len(self.students) + 1).zfill(4)
        student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        
        filepath = "./authenticate/students.txt"
        new_student_line = f"{student_id};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password},\n"
        
        if util.append_to_file(filepath, new_student_line):
            self.students.append(student_obj)
            return True
        else:
            return False

    def store_lecturer_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization):
        """
        Method to register the student in the system 
        and write the data of the new student into the file.

        Parameter(s):
        - first_name: str, student's first name
        - last_name: str, student's last name
        - date_of_birth: str, student's date of birthwdawd
        - contact_num: str, contact number of either student or contact person
        Returns:
        - bool: True if student data is stored from the system into the txt file, 
                False otherwise
        """

        # Create the Student object
        # Assume no skips in student ID
        lecturer_id = "l" + str(len(self.lecturers) + 1).zfill(2)
        lecturer_obj = LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
        filepath = "./authenticate/lecturers.txt"
        new_lecturer_line = f"{lecturer_id};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password};{specialization}\n"
        
        if util.append_to_file(filepath, new_lecturer_line):
            self.students.append(lecturer_obj)
            return True
        else:
            return False

    def store_admin_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Method to register the student in the system 
        and write the data of the new student into the file.

        Parameter(s):
        - first_name: str, student's first name
        - last_name: str, student's last name
        - date_of_birth: str, student's date of birthwdawd
        - contact_num: str, contact number of either student or contact person
        Returns:
        - bool: True if student data is stored from the system into the txt file, 
                False otherwise
        """

        # Create the Student object
        # Assume no skips in student ID
        self.import_admins_data()
        
        admin_id = "a" + str(len(self.admins) + 1).zfill(2)
        admin_obj = AdministratorUser(admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        
        filepath = "./authenticate/admins.txt"
        new_admin_line = f"{admin_id};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password},\n"
        
        if util.append_to_file(filepath, new_admin_line):
            self.admins.append(admin_obj)
            return True
        else:
            return False
    
    def edit_admin_data(self, admin_to_edit, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        filepath = "./authenticate/admins.txt"
        new_admin_line = f"{admin_to_edit.uid};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password}\n"
        
        return util.overwrite_file_at_line(filepath, int(admin_to_edit.uid[1:])-1,new_admin_line)

    def edit_student_data(self, student_to_edit, first_name=None, last_name=None, date_of_birth=None, contact_num=None, contact_email=None, username=None, password=None, specialization=[], course_progress=[0,0,0,0,0,0]):
        filepath = "./authenticate/students.txt"
        if first_name == None:
            first_name = student_to_edit.first_name
        if last_name == None:
            last_name = student_to_edit.last_name
        if date_of_birth == None:
            date_of_birth = student_to_edit.date_of_birth
        if contact_num == None:
            contact_num = student_to_edit.contact_num
        if contact_email == None:
            contact_email = student_to_edit.contact_email
        if username == None:
            username = student_to_edit.username
        if password == None:
            password = student_to_edit.password
        if specialization == []:
            specialization = student_to_edit.specialization
        if course_progress == [0,0,0,0,0,0]:
            course_progress = student_to_edit.course_progress

        student_to_edit.first_name = first_name
        student_to_edit.last_name = last_name
        student_to_edit.date_of_birth = date_of_birth
        student_to_edit.contact_num = contact_num
        student_to_edit.contact_email = contact_email
        student_to_edit.username = username
        student_to_edit.password = password
        student_to_edit.specialization = specialization
        student_to_edit.course_progress = course_progress
        
        new_student_line = f"{student_to_edit.uid};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password};{specialization};{course_progress}\n"
        
        return util.overwrite_file_at_line(filepath, int(student_to_edit.uid[1:])-1,new_student_line)

    def edit_lecturer_data(self, lecturer_to_edit, first_name=None, last_name=None, date_of_birth=None, contact_num=None, contact_email=None, username=None, password=None, specialization=[]):
        if first_name == None:
            first_name = lecturer_to_edit.first_name
        if last_name == None:
            last_name = lecturer_to_edit.last_name
        if date_of_birth == None:
            date_of_birth = lecturer_to_edit.date_of_birth
        if contact_num == None:
            contact_num = lecturer_to_edit.contact_num
        if contact_email == None:
            contact_email = lecturer_to_edit.contact_email
        if username == None:
            username = lecturer_to_edit.username
        if password == None:
            password = lecturer_to_edit.password
        if specialization == []:
            specialization = lecturer_to_edit.specilization

        lecturer_to_edit.first_name = first_name
        lecturer_to_edit.last_name = last_name
        lecturer_to_edit.date_of_birth = date_of_birth
        lecturer_to_edit.contact_num = contact_num
        lecturer_to_edit.contact_email = contact_email
        lecturer_to_edit.username = username
        lecturer_to_edit.password = password
        lecturer_to_edit.specialization = specialization
        
        filepath = "./authenticate/lecturers.txt"
        new_lecturer_line = f"{lecturer_to_edit.uid};{first_name};{last_name};{date_of_birth};{contact_num};{contact_email};{username};{password};{specialization}\n"
        
        return util.overwrite_file_at_line(filepath, int(lecturer_to_edit.uid[1:])-1,new_lecturer_line)