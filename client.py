import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNumber = 0 # Number of connected clients


def updateWindow():
    pygame.display.update()