from snake import Snake
from text import Texts
from food import Food
from time import sleep

snake = Snake()
food = Food()
messages = Texts()

score = 0

high_score_file = open("high_score.txt")

high_score = int(high_score_file.read())

high_score_file.close()

messages.keep_score(score, high_score)

while snake.game:
    snake.screen.update()
    sleep(0.1)
    snake.move()

    if snake.segments[len(snake.segments) - 1].distance(food) < 15:
        food.remove()
        food = Food()
        score += 1
        messages.keep_score(score, high_score)
        snake.new_part_incoming()

    if not snake.game:
        if score > high_score:
            high_score_file = open("high_score.txt", mode="w")
            high_score_file.write(str(score))

        messages.game_over()

snake.exit()