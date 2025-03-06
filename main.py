from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")


def main_game():
    #Screen setup that resets itself
    screen.bgcolor("black")
    screen.tracer(0)

    #Creating the snake, food and scoreboard
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    #Listening for user inputs to change the direction of the snake
    screen.listen()
    screen.onkey(key="Right", fun=snake.point_east)
    screen.onkey(key="Up", fun=snake.point_north)
    screen.onkey(key="Left", fun=snake.point_west)
    screen.onkey(key="Down", fun=snake.point_south)

    #Main game
    is_game_over = False
    while not is_game_over:
        #Updating the screen and delaying the update
        screen.update()
        time.sleep(0.1)

        #Snake always moves forwards
        snake.move()
    
        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.go_to_random_location()
            scoreboard.increase_score()
            snake.extend()

        #Detect collision with walls
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            restart_game()

        #Detect collision with tail
        for snake_part in snake.snake_body[1:]:
            if snake.head.distance(snake_part) < 10:
                scoreboard.game_over()
                restart_game()


def restart_game():
    screen.update()
    global is_game_over
    is_game_over = True
    time.sleep(1)
    screen.clearscreen()
    main_game()



main_game()




screen.exitonclick()
