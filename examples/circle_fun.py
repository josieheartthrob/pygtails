import pygame
from pygtails import Game, Circle
from colors import *

class CirclePoke(Game):
    def __init__(self):
        super().__init__((400, 300), "Circle Fun")
        self.screen.fill(WHITE)
        pygame.display.flip()
        c = PokeyCircle(self)
        c.draw()

class PokeyCircle(Circle):
    def __init__(self, game):
        super().__init__(game, (20, 20), 50)
        self.color = BLUE

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color,
                           self.center, self.radius)
        pygame.display.flip()

    def on_mouse_down(self, event):
        if self.color == BLUE:
            self.color = GREEN
        else:
            self.color = BLUE
        self.draw()

game = CirclePoke()
game.main()
