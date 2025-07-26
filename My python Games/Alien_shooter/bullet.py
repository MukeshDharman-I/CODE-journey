import pygame

from img import Images


class Bullet():
 
    def __init__(self):
        self.imag = Images()
        self.bulletImg=pygame.image.load("images/bullet.bmp")
        self.bulletX=0
        self.bulletY=630
        self.bulletY_change=12
        self.bulletX_change=0
        self.bullet_state="ready"