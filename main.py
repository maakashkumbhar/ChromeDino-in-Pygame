import pygame
import sys
from pygame.locals import *



###############Global Variables################3
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
FPS = 60
WHITE = (255,255,255)
background = pygame.image.load('Assets/background.png').convert_alpha()
################################################


if __name__ == "__main__":

    running = True
    while running:
        SCREEN.fill(WHITE)
        SCREEN.blit(background,(0,0))
        ###########For Event Mapping###############
        for event in pygame.event.get():
            if event.type == quit or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                sys.exit
        pygame.display.update()
