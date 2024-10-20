"""
FIT1056 EMPOWERU
"""
import os

from ast import literal_eval

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
                
                student_id, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization, course_progress = line.strip("\n").split(";")
                specialization = literal_eval(specialization)
                course_progress = literal_eval(course_progress)
                if input_username == username:
                    if input_password == password:
                        return StudentUser(student_id, first_name, last_name, date_of_birth, contact_num, contact_email, input_username, input_password, specialization, course_progress)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {student_path} exists.")

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password, specialization=[], course_progress=[0,0,0,0,0,0]):
        """
        Constructor
        """
        super().__init__(uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password)
        self.specialization = specialization
        self.course_progress = course_progress

    def store_student_answer(self,student,course,answers):
        # Assume no skips in student ID
        student_id =student.uid
        course_name=""
        
        filepath = "./authenticate/quiz_student_ans.txt"
        for num in range(len(student.specialization)):
            if student.specialization[num] ==course:
                course_name= student.specialization[num]

        new_student_line = f"{student_id};{course_name};{answers};\n"
        
        if util.append_to_file(filepath, new_student_line):
            return True
        else:
            return False
        
    

if __name__ == "__main__":
  pass
