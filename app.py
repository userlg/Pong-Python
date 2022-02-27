from tkinter import E
import pygame as py
import colorama as co

py.init()
co.init()

WIDTH = 700
HEIGHT = 500

WIN = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("PONG--GAME")

white = co.Fore.WHITE
yellow = co.Fore.YELLOW
red = co.Fore.RED
blue = co.Fore.BLUE
green = co.Fore.GREEN

def main() -> None:
    run = True

    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break

    py.quit()

if __name__ == '__main__':
    print(yellow + '\t\t Welcome to this pong Game \n\n')
    main()