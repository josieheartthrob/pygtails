import pygame
from pygtails import Game

class Hello(Game):
    def __init__(self):
        super().__init__((400, 300), "Hello, world!")
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

game = Hello()
game.main()
