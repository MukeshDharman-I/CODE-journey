import pygame
import random

class Alien:

     def __init__(self):

        self.alien = pygame.image.load("images/alien.bmp")

        self.alienX = random.randint(0,1000)

        self.alienY = random.randint(0,600)

        self.alienY_Change = 0

        self.alienX_Change = 0