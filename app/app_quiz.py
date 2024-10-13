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

class QuizLoader:
    
    @staticmethod
    def load_quiz_from_file(file_path="./authenticate/quiz.txt"):
        # Check if the file exists
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            
            # Check if file has content
            if len(lines) == 0:
                print(f"WARNING: {file_path} is empty.")
                return None
            
            # quiz ID and title
            quiz_id, quiz_title = lines[0].strip("\n").split(", ")

            questions = []

            # process questions
            for line in lines[1:]:
                if len(line) < 5:
                    print(f"WARNING: A line in {file_path} is invalid: {line.strip()}")
                    continue

                parts = line.strip().split(", ")
                
                if len(parts) < 3:
                    print(f"WARNING: A question in {file_path} is not properly formatted.")
                    continue
                
                # question text, correct answer, and choices
                question_text = parts[0]
                correct_answer = int(parts[1])
                choices = [int(choice) for choice in parts[2:]]  # List of choices

                # append it to the questions list
                question = Question(question_text, correct_answer, choices)
                questions.append(question)

            return Quiz(quiz_id, quiz_title, questions)

        else:
            print(f"Please check that the file {file_path} exists.")
            return None
