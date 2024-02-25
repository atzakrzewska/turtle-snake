from turtle import Screen
from snake import Snake, Border
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=640, height=600)
screen.bgcolor("gray0")
screen.title("Niebezpieczny Wąż")
screen.tracer(0)

snake = Snake()
apple = Food()
scoreboard = Scoreboard()
border = Border()

game_is_on = True

screen.listen()

# WSAD keys snake manipulation
screen.onkeypress(fun=snake.move_north, key="w")
screen.onkeypress(fun=snake.move_east, key="d")
screen.onkeypress(fun=snake.move_south, key="s")
screen.onkeypress(fun=snake.move_west, key="a")

# arrow keys snake manipulation
screen.onkeypress(fun=snake.move_north, key="Up")
screen.onkeypress(fun=snake.move_east, key="Right")
screen.onkeypress(fun=snake.move_south, key="Down")
screen.onkeypress(fun=snake.move_west, key="Left")

while game_is_on:
    snake.move()
    screen.update()

    # detect collision with food
    if snake.head.distance(apple) < 1:
        apple.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 270:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
