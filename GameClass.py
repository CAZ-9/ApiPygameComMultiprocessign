import pygame
import sys


class Game:
    def __init__(self):
        self._NAME = 'TryYourself'
        self._HEIGHT = 400
        self._WIDTH = 600
        self._FPS = 60
        self._FPS_CLOK = pygame.time.Clock()
        self._VEC = pygame.math.Vector2

    def run(self):
        print('shall we begin?')
        pygame.init()
        displaysurface = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        pygame.display.set_caption(self._NAME)

        # GAME LOOP:
        while True:

            for event in pygame.event.get():
                # Will run when the close window button is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pass

                # For events that occur upon clicking the mouse (left click)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

                # Event handling for a range of different key presses
                if event.type == pygame.KEYDOWN:
                    pass


    @property
    def HEIGHT(self):
        return self._HEIGHT

    @HEIGHT.setter
    def HEIGHT(self, value):
        self._HEIGHT = value

    @property
    def WIDTH(self):
        return self._HEIGHT

    @WIDTH.setter
    def WIDTH(self, value):
        self._WIDTH = value


