from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        




    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal")) 



    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update_score()


    def r_point(self):
        self.r_score+=1
        self.clear()
        self.update_score()




