from snake import Snake
from text import Texts
from food import Food
from time import sleep

snake = Snake()
food = Food()
messages = Texts()

score = 0

messages.keep_score(score)

while snake.game:
    snake.screen.update()
    sleep(0.1)
    move = snake.move()

    if abs(snake.segments[len(snake.segments) - 1].xcor()) >= 300 or abs(snake.segments[len(snake.segments) - 1].ycor()) >= 300:
        messages.game_over()
        snake.game = False

    if snake.segments[len(snake.segments) - 1].distance(food) < 15:
        food.remove()
        food = Food()
        score += 1
        messages.keep_score(score)
        snake.new_part_incoming()

snake.exit()