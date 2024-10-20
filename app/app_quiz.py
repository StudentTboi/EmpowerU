import app.app_utils as util

class Quiz:
    """
    Represents a quiz with questions, correct answers, grades, and feedback.

    Attributes:
    - quizID (str): Unique ID for the quiz.
    - qtitle (str): Title of the quiz.
    - questions (list): List of quiz questions.
    - correct_answers (list): List of correct answers corresponding to the questions.
    - grades (dict): Dictionary mapping student IDs to their grades.
    - feedback (dict): Dictionary mapping student IDs to feedback comments.
    - quiz_filename (str): Path to the quiz file.
    - grade_filename (str): Path to the grade file.
    """
    
    def __init__(self, quizID: str, qtitle: str, quiz_filename: str = None, grade_filename: str = None) -> None:
        """
        Initializes a Quiz object.

        Parameters:
        - quizID (str): Quiz identifier.
        - qtitle (str): Title of the quiz.
        - quiz_filename (str, optional): Filename to load quiz from.
        - grade_filename (str, optional): Filename to load grades from.
        """
        self.quizID = quizID
        self.qtitle = qtitle
        self.questions = []
        self.correct_answers = []
        self.grades = {}
        self.feedback = {}
        self.quiz_filename = quiz_filename
        self.grade_filename = grade_filename

    def addQuestion(self, question: str, correct_answer: str) -> None:
        """
        Adds a question and its correct answer to the quiz.

        Parameters:
        - question (str): The quiz question.
        - correct_answer (str): The correct answer to the question.
        """
        self.questions.append(question)
        self.correct_answers.append(correct_answer)

    @staticmethod
    def loadQuizFromFile(quiz_filename: str, grade_filename: str):
        """
        Loads quiz questions, answers, and student grades from files.

        Parameters:
        - quiz_filename (str): Path to the quiz file.
        - grade_filename (str): Path to the grade file.

        Returns:
        - Quiz: A Quiz object populated with data from the files.
        """
        with open(quiz_filename, 'r') as file:
            lines = file.readlines()

        quizID = ""
        qtitle = ""
        questions = []
        answers = []
        current_question = ""

        for line in lines:
            if line.startswith("QuizID:"):
                quizID = line.split("QuizID:")[1].strip()
            elif line.startswith("Title:"):
                qtitle = line.split("Title:")[1].strip()
            elif line.startswith("Question:"):
                current_question += line.split("Question:")[1]
            elif line.startswith("Answer:"):
                questions.append(current_question)
                answers.append(line.split("Answer:")[1].strip())
                current_question = ""
            else:
                current_question += line

        # Initialize a Quiz object and add questions/answers
        quiz = Quiz(quizID, qtitle, quiz_filename, grade_filename)
        for i in range(len(questions)):
            quiz.addQuestion(questions[i], answers[i])

        # Load grades
        with open(grade_filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            student_id, grade = line.strip().split(';')
            quiz.grades[student_id] = grade

        return quiz
    
    def gradeQuiz(self, student_answer: list, studentId: int) -> None:
        """
        Grades a student's quiz answers and stores the grade.

        Parameters:
        - student_answer (list): List of student's answers.
        - studentId (int): ID of the student.
        """
        marks = 0
        total_questions = len(self.questions)

        for i in range(total_questions):
            if student_answer[i].strip().lower() == self.correct_answers[i].strip().lower():
                marks += 1

        # Calculate percentage
        percentage = (marks / total_questions) * 100
        self.grades[studentId] = percentage

        # Append grade to file
        new_line = f"{studentId};{percentage}\n"
        util.append_to_file(self.grade_filename, new_line)

    def givefeedback(self, studentId: int, feedback: str) -> None:
        """
        Provides feedback for a student based on their performance.

        Parameters:
        - studentId (int): ID of the student.
        - feedback (str): Feedback to be given to the student.
        """
        self.feedback[studentId] = feedback
        print(f"Feedback for student {studentId}: {feedback}")
