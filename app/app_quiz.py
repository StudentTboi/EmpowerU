class Quiz:
    def __init__(self, quizID: str, qtitle: str) -> None:
        self.quizID = quizID
        self.qtitle = qtitle
        self.questions = []
        self.correct_answers = []
        self.grades = {}
        self.feedback = {}

    def addQuestion(self, question: str, correct_answer: str) -> None:
        """"
        Adding questions and the correct answer

        """

        self.questions.append(question)
        self.correct_answers.append(correct_answer)

    def loadQuizFromFile(filename: str):
        """
        Loads quiz from txt file returning a quiz object

        Parameters:
        filename (str): Path to quiz file

        Returns: 
        Quiz: Quiz object with questions and answers
        """
        with open(filename, 'r') as file:
            lines = file.readlines()

        quizID = ""
        qtitle = ""
        questions = []
        answers = []

        for line in lines:
            line = line.strip()
            if line.startswith("QuizID:"):
                quizID = line.split("QuizID:")[1].strip()
            elif line.startswith("Title:"):
                title = line.split("Title:")[1].strip()
            elif line.startswith("Questions:"):
                questions.append(line.split("Question:")[1].strip())
            elif line.startswith("Answer:"):
                answers.append(line.split("Answer:")[1].strip())

        quiz = Quiz(quizID, title)
        for i in range(len(questions)):
            quiz.addQuestion(questions[i], answers[i])

        return quiz
    
    def gradeQuiz(self, student_answer: list, studentId: int) -> None:
        marks = 0
        total_questions = len(self.questions)

        for i in range(total_questions):
            if student_answer[i].strip().lower() == self.correct_answers[i].strip().lower():
                marks += 1

        percentage = (marks / total_questions) * 100
        self.grades[studentId] = percentage
        print(f"Student {studentId} scored {percentage:.2f}% on quiz {self.quizID}")

    def givefeedback(self, studentId: int, feedback: str) -> None:
        self.feedback[studentId] = feedback
        print(f"Feedback for student {studentId}: {feedback}")