import pygame
import sys
import random
from pygame.locals import *


pygame.init()
###############Global Variables################3
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 780
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
FPS = 30
WHITE = (255,255,255)
background = pygame.image.load('Assets/background.png').convert_alpha()
player = pygame.image.load('Assets/dino_main.png').convert_alpha()
bird = pygame.image.load('Assets/berd.png').convert_alpha()
cactus1 = pygame.image.load('Assets/cactusBig0000.png').convert_alpha()
cactus2 = pygame.image.load('Assets/cactusSmall0000.png').convert_alpha()
cactus3 = pygame.image.load('Assets/cactusSmallMany0000.png').convert_alpha()
background_positionX = 0
background_positionY = 0
playerPosY = 430
playerPosX = 30
birdPosX = 500
birdPosY = 30
cactus_PosX = 500
################################################

def background_movement(backPosX,backPosY):
    SCREEN.blit(background,(backPosX,backPosY))
    SCREEN.blit(background,(background_positionX+45,background_positionY))


def dino_player(playerPosX,playerPosY):
    SCREEN.blit(player,(playerPosX,playerPosY))


def bird_movement(birdPosX,birdPosY):
    SCREEN.blit(bird,(birdPosX,birdPosY))


def cactus_movement(cactusPosx,cactusPosY):
    SCREEN.blit(cactus1,(cactus_PosX,cactusPosY))
    
if __name__ == "__main__":

    clock = pygame.time.Clock()
    running = True
    while running:
        SCREEN.fill(WHITE)
        ###########For Event Mapping###############
        #########background Movement Logic########################
        background_positionX += -1
        background_movement(background_positionX,background_positionY)
        if background_positionX <= -50:
            background_positionX = 0
        ##########################################################

        for event in pygame.event.get():
            if event.type == quit or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                sys.exit
            #############Player Movement Logic########################
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    playerPosY -= 150
                    playerPosX += 10
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    playerPosY = 430
                    
        #####################################
        dino_player(playerPosX,playerPosY)
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
