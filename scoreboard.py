from turtle import *
import random


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(-100, 270)
        self.pencolor("white")
        #self.write(f"SCORE: {self.score}", font=("Arial", 12, "normal"))
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}   HIGH SCORE {self.high_score}", font=("Arial", 12, "normal"))


    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("high score",mode="w") as file:
            file.write("Current High Score: ")
            file.write(str(self.high_score))


    def gameover(self):
        self.goto(-70, 0)
        self.write(f"GAME OVER!", font=("Arial", 20, "normal"))

    def increasescore(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
