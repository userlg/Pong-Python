import pygame as py
import colorama as co

py.init()
co.init()

WIDTH = 800
HEIGHT = 700
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)


PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

WIN = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("PONG--GAME")

white = co.Fore.WHITE
yellow = co.Fore.YELLOW
red = co.Fore.RED
blue = co.Fore.BLUE
green = co.Fore.GREEN



class Paddle:
    COLOR = WHITE
    VEL = 4


    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self,win) -> None:
        py.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))

    def move(self, up = True) -> None:
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

def handle_movement_paddle(keys, left_paddle, right_paddle) -> None:
    if keys[py.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[py.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    
    if keys[py.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[py.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def draw(win, paddles) -> None:
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    py.display.update()



def main() -> None:
    run = True
    clock = py.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)


    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle,right_paddle])


        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break

        keys = py.key.get_pressed()
        handle_movement_paddle(keys, left_paddle, right_paddle)


    py.quit()

if __name__ == '__main__':
    print(yellow + '\t\t Welcome to this pong Game \n\n')
    main()