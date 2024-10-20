import app.app_utils as util

class Quiz:
    def __init__(self, quizID: str, qtitle: str, quiz_filename: str = None, grade_filename: str = None) -> None:
        self.quizID = quizID
        self.qtitle = qtitle
        self.questions = []
        self.correct_answers = []
        self.grades = {}
        self.feedback = {}
        self.quiz_filename = quiz_filename
        self.grade_filename = grade_filename

    def addQuestion(self, question: str, correct_answer: str) -> None:
        """"
        Adding questions and the correct answer

        """

        self.questions.append(question)
        self.correct_answers.append(correct_answer)

    def loadQuizFromFile(quiz_filename: str, grade_filename: str):
        """
        Loads quiz from txt file returning a quiz object

        Parameters:
        filename (str): Path to quiz file

        Returns: 
        Quiz: Quiz object with questions and answers
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
                title = line.split("Title:")[1].strip()
            elif line.startswith("Question:"):
                current_question += line.split("Question:")[1]
            elif line.startswith("Answer:"):
                questions.append(current_question)
                answers.append(line.split("Answer:")[1].strip())
                current_question = ""
            else:
                current_question += line

        quiz = Quiz(quizID, title, quiz_filename, grade_filename)
        for i in range(len(questions)):
            quiz.addQuestion(questions[i], answers[i])

        with open(grade_filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            line.strip()
            student_id = line.split(';')[0]
            grade = line.split(';')[1]
            quiz.grades[student_id] = grade

        return quiz
    
    def gradeQuiz(self, student_answer: list, studentId: int) -> None:
        marks = 0
        total_questions = len(self.questions)

        for i in range(total_questions):
            if student_answer[i].strip().lower() == self.correct_answers[i].strip().lower():
                marks += 1

        percentage = (marks / total_questions) * 100
        self.grades[studentId] = percentage
        
        new_line = f"{studentId};{percentage}\n"

        util.append_to_file(self.grade_filename, new_line)

    def givefeedback(self, studentId: int, feedback: str) -> None:
        self.feedback[studentId] = feedback
        print(f"Feedback for student {studentId}: {feedback}")
