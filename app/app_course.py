from app.app_quiz import Quiz

class Course:
    def __init__(self, course_type):
        if course_type == "AI":
            self.filepath = "./learning_materials/ai"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/ai_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/ai_quiz.txt")
        elif course_type == "InfoSec":
            self.filepath = "./learning_materials/infoSec"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/infoSec_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/infoSec_quiz.txt")
        elif course_type == "PyLearn":
            self.filepath = "./learning_materials/python"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/py_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/py_quiz.txt")
    
    def loadReadingFromFile(filename: str):
        """
        Loads quiz from txt file returning a quiz object

        Parameters:
        filename (str): Path to quiz file

        Returns: 
        Quiz: Quiz object with questions and answers
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines