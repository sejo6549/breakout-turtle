import time
from turtle import Turtle
import tkinter as tk

class Scoreboard(Turtle):
    def __init__(self, x, y, lives):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.username_list=[]
        self.lives=lives
        self.goto(x, y)
        self.write(f"x{self.lives} lives\nScore: {self.score}", align="center", font=("Roboto", 24, "normal"))

    def lose_a_life(self):
        self.lives-=1
        if(self.lives==0):
            self.game_over()
        else:
            self.clear()
            self.write(f"x{self.lives} lives\nScore: {self.score}", align="center", font=("Roboto", 24, "normal"))

    def update_score(self, points):
        self.score+=points
        self.clear()
        self.write(f"x{self.lives} lives\nScore: {self.score}", align="center", font=("Roboto", 24, "normal"))


    def game_over(self):
        self.clear()
        self.write(f"Game over. \nYou scored {self.score} points", align="center", font=("Roboto", 24, "normal"))
