import os
from ast import literal_eval
from app.app_user import User
from app.app_student import StudentUser
import app.app_utils as util

class LecturerUser(User):
    """
    Represents a lecturer user in the system, responsible for authentication
    and managing student data.

    Attributes:
    - uid (str): Unique identifier for the lecturer.
    - first_name (str): Lecturer's first name.
    - last_name (str): Lecturer's last name.
    - date_of_birth (str): Lecturer's date of birth.
    - contact_num (str): Lecturer's contact number.
    - contact_email (str): Lecturer's email address.
    - username (str): Lecturer's username.
    - password (str): Lecturer's password.
    - specialization (list): Lecturer's areas of specialization.
    - students (list): List of students associated with the lecturer.
    """

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Authenticates a lecturer based on the provided username and password.

        Parameters:
        - input_username (str): The lecturer's username.
        - input_password (str): The lecturer's password.

        Returns:
        - LecturerUser: An instance of LecturerUser if authentication succeeds, 
                        None otherwise.
        """
        lecturer_path = "./authenticate/lecturers.txt"
        lines = util.read_file(lecturer_path)
        if lines:
            for line in lines:
                if len(line) < 5:  # Checking if the line is invalid
                    print(f"WARNING: A line in {lecturer_path} is invalid")
                    continue

                lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization = line.strip("\n").split(";")
                specialization = literal_eval(specialization)

                if input_username == username and input_password == password:
                    return LecturerUser(lecturer_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization)
        else:
            print(f"Please check if the file {lecturer_path} exists.")
        return None

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization):
        """
        Initializes the LecturerUser object with provided details and loads associated students.

        Parameters:
        - uid (str): Unique identifier for the lecturer.
        - first_name (str): Lecturer's first name.
        - last_name (str): Lecturer's last name.
        - date_of_birth (str): Lecturer's date of birth.
        - contact_num (str): Lecturer's contact number.
        - contact_email (str): Lecturer's email address.
        - username (str): Lecturer's username.
        - password (str): Lecturer's password.
        - specialization (list): Lecturer's areas of specialization.
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.specialization = specialization
        self.import_students_data()

    def import_students_data(self):
        """
        Loads the list of students associated with the lecturer from a file.
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
