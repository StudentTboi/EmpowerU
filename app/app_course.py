from app.app_quiz import Quiz

class Course:
    """
    Represents a course with specific learning materials and a quiz.

    Attributes:
    - course_type (str): The type of course (e.g., 'AI', 'InfoSec', 'PyLearn').
    - filepath (str): The path to the course's learning materials.
    - reading_materials (list): List of reading materials loaded from a file.
    - quiz (Quiz): Quiz object loaded from a file.
    """

    def __init__(self, course_type):
        """
        Initializes the course based on the course type.

        Parameters:
        - course_type (str): Type of the course to initialize ('AI', 'InfoSec', or 'PyLearn').
        """
        self.course_type = course_type
        if course_type == "AI":
            self.filepath = "./learning_materials/ai"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/ai_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/ai_quiz.txt", f"{self.filepath}/quiz_grade.txt")
        elif course_type == "InfoSec":
            self.filepath = "./learning_materials/infoSec"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/infoSec_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/infoSec_quiz.txt", f"{self.filepath}/quiz_grade.txt")
        elif course_type == "PyLearn":
            self.filepath = "./learning_materials/python"
            self.reading_materials = Course.loadReadingFromFile(f"{self.filepath}/py_content.txt")
            self.quiz = Quiz.loadQuizFromFile(f"{self.filepath}/py_quiz.txt", f"{self.filepath}/quiz_grade.txt")
    
    @staticmethod
    def loadReadingFromFile(filename: str):
        """
        Loads reading materials from a file.

        Parameters:
        - filename (str): Path to the reading materials file.

        Returns:
        - list: Lines of text from the file.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
