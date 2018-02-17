#TODO: Documentation

import pygame
import sys

from pygame.locals import *

class Game(object):
    #TODO: Documentation

    def __init__(self, resolution, title, flags=0, depth=0):
        #TODO: Documentation
        pygame.init() 
        self.screen = pygame.display.set_mode(resolution, flags)
        pygame.display.set_caption(title)

        self._handle = {QUIT:            self.quit,
                        ACTIVEVENT:      self.on_focus,
                        KEYDOWN:         self.on_key_down,
                        KEYUP:           self.on_key_up,
                        MOUSEMOTION:     self.on_mouse_move,
                        MOUSEBUTTONUP:   self.on_mouse_up,
                        MOUSEBUTTONDOWN: self.on_mouse_down,
                        VIDEORESIZE:     self.on_resize}

    def main(self):
        '''The main loop. Call this to run the game.'''
        for event in pygame.event.get():
            self._handle[event.type](event)

    def quit(self, event):
        #TODO: Documentation
        pygame.quit()
        sys.exit()

    def on_focus(self, event):
        #TODO: Documentation
        pass

    def on_key_down(self, event):
        #TODO: Documentation
        pass

    def on_key_up(self, event):
        #TODO: Documentation
        pass

    def on_mouse_move(self, event):
        #TODO: Documentation
        pass

    def on_mouse_up(self, event):
        #TODO: Documentation
        pass

    def on_mouse_down(self, event):
        #TODO: Documentation
        pass

    def on_resize(self, event):
        #TODO: Documentation
        pass
