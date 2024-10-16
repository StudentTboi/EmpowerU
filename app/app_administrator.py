import os

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
                
                admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return AdministratorUser(admin_id, first_name, last_name, date_of_birth, contact_num, contact_email, input_username, input_password)
                    else:
                        return None # or return, or break

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.import_all_data()

    def import_all_data(self):
        """
        Method to read all data by calling methods to read teachers data and students data.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.import_teachers_data()
        self.import_students_data()

    def import_teachers_data(self):
        """
        Method to read teachers data and store it into the receptionist's session.

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
                lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization = line.strip("\n").split(",")
                specialization_list = specialization.split("&")
                lecturer_obj = LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization_list)
                self.lecturers.append(lecturer_obj)

    def import_students_data(self):
        """
        Method to read students data and store it into the receptionist's session.

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
                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, enrolled_courses = line.strip("\n").split(",")
                enrolled_courses_list = enrolled_courses.split("&")
                student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, enrolled_courses_list)
                self.students.append(student_obj)

    def store_student_data(self, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Method to register the student in the system 
        and write the data of the new student into the file.

        Parameter(s):
        - first_name: str, student's first name
        - last_name: str, student's last name
        - date_of_birth: str, student's date of birthwdawd
        - contact_num: str, contact number of either student or contact person
sdqwd
        Returns:
        - bool: True if student data is stored from the system into the txt file, 
                False otherwise
        """

        # Create the Student object
        # Assume no skips in student ID
        student_id = "s" + str(len(self.students) + 1).zfill(4)
        student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        
        filepath = "./authenticate/students.txt"
        new_student_line = f"{student_id},{first_name},{last_name},{date_of_birth},{contact_num},{contact_email},{username},{password},\n"
        
        if util.append_to_file(filepath, new_student_line):
            self.students.append(student_obj)
            return True
        else:
            return False
