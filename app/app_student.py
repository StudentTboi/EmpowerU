"""
FIT1056 EMPOWERU
"""
import os

from app.app_lecturer import User

class StudentUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        student_path = "./authenticate/students.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                if len(line)<6:
                    continue
                
                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, enrolled_courses = line.strip("\n").split(",")
                enrolled_courses_list = enrolled_courses.split("&")
                if input_username == username:
                    if input_password == password:
                        return StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, input_username, input_password, enrolled_courses_list)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {student_path} exists.")

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, enrolled_courses=[]):
        """
        Constructor
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.enrolled_courses = enrolled_courses
        self.import_course_data()
    
    def import_course_data(self):
        return
        

if __name__ == "__main__":
  pass
