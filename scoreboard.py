from turtle import Turtle
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.current_level = 1
        self.level()

    def level(self):
        self.clear()
        self.write(f"LEVEL: {self.current_level}", align="left", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.level()

    def game_over(self):
        self.goto(-50,0)
        self.write("GAME OVER!", align="left", font=FONT)

