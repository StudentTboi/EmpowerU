import os

class Question:
    def __init__(self, question_text, correct_answer, choices):
        """
        Constructor for the Question class.
        """
        self.question_text = question_text 
        self.correct_answer = correct_answer  
        self.choices = choices 

class Quiz:
    def __init__(self, quiz_id, title, questions):
        """
        Constructor for the Quiz class.
        """
        self.quiz_id = quiz_id  
        self.title = title  
        self.questions = questions  


        else:
            print(f"Please check that the file {file_path} exists.")
            return None
