from turtle import Turtle


class Level:
    def __init__(self, level_number):
        self.obstacles = []
        self.level_number = level_number
        self.draw_level()

    def create_block(self, x, y):
        block = Turtle("square")
        block.penup()
        block.color("black")
        block.goto(x, y)
        self.obstacles.append(block)

    def draw_level(self):
        if self.level_number == 2:
            for x in range(-240, 250, 20):
                self.create_block(x, 100)
        elif self.level_number == 3:
            for x in range(-240, 250, 20):
                self.create_block(x, 100)
            for x in range(-240, 250, 20):
                self.create_block(x, -100)

    def check_collision(self, head):
        for block in self.obstacles:
            if head.distance(block) < 15:
                return True
        return False