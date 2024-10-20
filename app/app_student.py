import os
from ast import literal_eval
from app.app_user import User
import app.app_utils as util

class StudentUser(User):
    """
    Represents a student user, extends the base User class.

    Attributes:
    - specialization (list): The student's specialization areas.
    - course_progress (list): Progress in various courses.
    """
    
    @staticmethod
    def authenticate(input_username, input_password):
        """
        Authenticates a student by checking their credentials from a file.

        Parameters:
        - input_username (str): The username entered by the student.
        - input_password (str): The password entered by the student.

        Returns:
        - StudentUser: If authentication is successful, an instance of StudentUser is returned.
        - None: If authentication fails, returns None.
        """
        student_path = "./authenticate/students.txt"
        lines = util.read_file(student_path)
        if lines:
            for line in lines:
                # Skip invalid lines
                if len(line) < 6:
                    continue

                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                course_progress = literal_eval(course_progress)
                
                if input_username == username and input_password == password:
                    return StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, input_username, input_password, specialization, course_progress)
        else:
            print(f"Please check that the file '{student_path}' exists.")
        return None
    
    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization=[], course_progress=[0, 0, 0, 0, 0, 0]):
        """
        Constructor for StudentUser class.

        Parameters:
        - uid (str): Student ID.
        - first_name (str): First name of the student.
        - last_name (str): Last name of the student.
        - date_of_birth (str): Date of birth of the student.
        - contact_num (str): Contact number of the student.
        - contact_email (str): Email address of the student.
        - username (str): Username of the student.
        - password (str): Password of the student.
        - specialization (list): A list of the student's specialization areas (optional).
        - course_progress (list): A list of the student's progress in different courses (optional, default is six zeros).
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.specialization = specialization
        self.course_progress = course_progress

if __name__ == "__main__":
    pass
