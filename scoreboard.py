from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.ht()
        self.pu()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, ALIGNMENT , FONT )


    def game_over(self):
        self.home()
        self.write("GAME OVER", False, ALIGNMENT, FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()