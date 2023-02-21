from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,background=THEME_COLOR)
        self.score = Label(text="Score:0", font=("Arial", 15),background=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        self.correct_button_img = PhotoImage(file="images/true.png")
        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.correct_button = Button(image=self.correct_button_img, highlightthickness=0, command=self.right_answer)
        self.correct_button.grid(column=0, row=2)
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the question.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


