import pygame as py
import colorama as co
from components import Ball, Paddle

py.init()
co.init()

WIDTH = 800
HEIGHT = 700
FPS = 60
BALL_RADIUS = 7

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (19, 58, 38)

SCORE_FONT = py.font.SysFont("comicsans",50)


WINNING_SCORE = 5

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("PONG--GAME")

white = co.Fore.WHITE
yellow = co.Fore.YELLOW
red = co.Fore.RED
blue = co.Fore.BLUE
green = co.Fore.GREEN


def handle_collision(ball, right_paddle, left_paddle) -> None:
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1


def handle_movement_paddle(keys, left_paddle, right_paddle) -> None:
    if keys[py.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[py.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[py.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[py.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def draw(win, paddles, ball, left_score, right_score) -> None:
    win.fill(GREEN)

    left_score_text = SCORE_FONT.render(f"{left_score}",1, WHITE)

    right_score_text = SCORE_FONT.render(f"{right_score}",1, WHITE)

    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))

    win.blit(right_score_text, (WIDTH * (3 / 4 ) - right_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        py.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)

    py.display.update()


def main() -> None:
    run = True
    clock = py.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball,left_score, right_score)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break

        keys = py.key.get_pressed()
        handle_movement_paddle(keys, left_paddle, right_paddle)
        ball.move()
        handle_collision(ball, right_paddle, left_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        
        won = False

        if right_score == WINNING_SCORE:
            won = True
            win_text = 'Winner the right player'
        elif left_score == WINNING_SCORE:
            won = True
            win_text = 'Winner the right player'

        if won == True:
            text = SCORE_FONT.render(win_text,1, WHITE)
            WIN.blit(text,(WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            py.display.update()
            py.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0
            won = False

    py.quit()


if __name__ == '__main__':
    print(yellow + '\t\t Welcome to this pong Game \n\n')

    main()

#######################Created by Userlg ##################################################################
