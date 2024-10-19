from app.app_quiz import Quiz

class Course:
    def __init__(self, course_type):
        if course_type == "AI":
            filepath = "./learning_materials/ai"
        self.reading_materials = Course.loadReadingFromFile(f"{filepath}/ai_content.txt")
        self.quiz = Quiz.loadQuizFromFile(f"{filepath}/ai_quiz.txt")
    
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