from turtle import Screen, Turtle
from snake import Snake
from food import Food
from level import Level
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)

border = Turtle()
border.penup()
border.pensize(3)
border.color("black")
border.goto(290, 290)
border.pendown()
border.goto(-290, 290)
border.goto(-290, -290)
border.goto(290, -290)
border.goto(290, 290)
border.goto(290, 290)
border.hideturtle()

snake = Snake()
scoreboard = Scoreboard()


def choose_speed():
    speed = screen.textinput("Choose Speed", "(1 = Slow, 2 = Medium, 3 = Fast):")
    if speed == "1":
        return 0.12
    elif speed == "2":
        return 0.1
    elif speed == "3":
        return 0.08
    else:
        return 0.1

def choose_level():
    level = screen.textinput("Choose Level", "(1-3):")
    if level == "1":
        return 1
    elif level == "2":
        return 2
    elif level == "3":
        return 3
    else:
        return 1

game_speed = choose_speed()
game_level = choose_level()
level = Level(game_level)
food = Food(level)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall and level.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 or level.check_collision(snake.head):
        game_is_on = False
        scoreboard.update_scoreboard()
        scoreboard.reset()
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.update_scoreboard()
            scoreboard.reset()
            scoreboard.game_over()

screen.exitonclick()
