from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.level_write()

    def level_up(self):
        self.level += 1
        self.clear()
        self.level_write()

    def level_write(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" Your Level is: {self.level}\n GAME OVER!", align="center", font=FONT)
