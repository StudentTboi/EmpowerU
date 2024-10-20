import os

from ast import literal_eval

from app.app_user import User
from app.app_student import StudentUser
import app.app_utils as util

class LecturerUser(User):

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a lecturer user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of LecturerUser corresponding to the username if successful,
          None otherwise
        """
        lecturer_path = "./authenticate/lecturers.txt"
        if os.path.exists(lecturer_path):
            with open(lecturer_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()

            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                if len(line)<5: #Checking if line is invalid
                    print(f"WARNING: A line in {lecturer_path} is invalid")
                    continue
                
                lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization = line.strip("\n").split(";")
                specialization = literal_eval(specialization)

                if input_username == username:
                    if input_password == password:
                        return LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {lecturer_path} exists.")
          
    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization):
        """
        Constructor for the LecturerUser class
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.specialization = specialization
        self.import_students_data()

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

if __name__ == "__main__":
    pass
