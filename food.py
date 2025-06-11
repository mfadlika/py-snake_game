from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, level=None):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("whitesmoke")
        self.speed("fastest")
        self.level = level
        self.refresh()

    def refresh(self):
        while True:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            self.goto(random_x, random_y)

            if self.level is None:
                break

            is_colliding = False
            for block in self.level.obstacles:
                if self.distance(block) < 15:
                    is_colliding = True
                    break

            if not is_colliding:
                break
