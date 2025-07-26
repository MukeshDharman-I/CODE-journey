import pygame

class Images:

    def __init__(self):

        self.player = pygame.image.load("images/ship.bmp")

        self.playerX = 600

        self.playerY = 700

        self.playerY_Change = 0

        self.playerX_Change = 0

        self.press_Right = False