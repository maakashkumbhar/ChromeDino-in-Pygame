import pygame
import sys
from pygame.locals import *


pygame.init()
###############Global Variables################3
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 450
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
FPS = 60
WHITE = (255,255,255)
background = pygame.image.load('Assets/background.png').convert_alpha()
player = pygame.image.load('Assets/dino_main.png').convert_alpha()
bird = pygame.image.load('Assets/berd.png').convert_alpha()
cactus = pygame.image.load('Assets/cactusBig0000.png').convert_alpha()
background_positionX = 0
background_positionY = 0
playerPosY = 430
birdPosX = 500
birdPosY = 30
cactus_PosX = 500
################################################

def background_movement(backPosX,backPosY):
    SCREEN.blit(background,(backPosX,backPosY))
    SCREEN.blit(background,(background_positionX-20,background_positionY))


def dino_player(playerPosX,playerPosY):
    SCREEN.blit(player,(playerPosX,playerPosY))


def bird_movement(birdPosX,birdPosY):
    SCREEN.blit(bird,(birdPosX,birdPosY))


def cactus_movement(cactusPosx,cactusPosY):
    SCREEN.blit(cactus,(cactus_PosX,cactusPosY))
    
if __name__ == "__main__":

    clock = pygame.time.Clock()
    running = True
    while running:
        SCREEN.fill(WHITE)
        ###########For Event Mapping###############
        #########background Movement Logic########################
        background_positionX += -1
        background_movement(background_positionX,background_positionY)
        if background_positionX <= -300:
            background_positionX = 10
        ##########################################################

        for event in pygame.event.get():
            if event.type == quit or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                sys.exit
            #############Player Movement Logic########################
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    playerPosY -= 150
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    playerPosY = 430
        #####################################
        dino_player(30,playerPosY)
        #####################################
        #########Making the Birds Fly Around#
        birdPosX -= 2
        bird_movement(birdPosX,birdPosY)
        if birdPosX <=-5:
            birdPosX = 500
        #####################################
        #######Cactus Movement###############
        cactus_PosX -= 5
        cactus_movement(cactus_PosX,430)

        if cactus_PosX <= -5:
            cactus_PosX = 500
        #####################################
        clock.tick(FPS)
        pygame.display.update()
