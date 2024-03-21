from turtle import Turtle

START_POSITION = [(0,0), (20,0), (40,0)]
MOVE_DISTANCE = 20
STANDARD_DIR = {
    'RIGHT': 0,
    'UP': 90,
    'LEFT': 180,
    'DOWN': 270
}

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for position in START_POSITION:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.setposition(position)  
            self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(STANDARD_DIR['UP'])

    def down(self):
        self.head.setheading(STANDARD_DIR['DOWN'])

    def left(self):
        self.head.setheading(STANDARD_DIR['LEFT'])

    def right(self):
        self.head.setheading(STANDARD_DIR['RIGHT'])