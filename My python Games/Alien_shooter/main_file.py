import sys
import pygame
import math

from settings import Settings
from img import Images
from bullet import Bullet
from alien import Alien


class Alien_Invader:

    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.ship = Images()

        self.bullet = Bullet()

        self.aliens = Alien()


        self.screen=pygame.display.set_mode((self.settings.width,self.settings.height),pygame.FULLSCREEN)

        pygame.display.set_caption(self.settings.caption)

        #self.clock=pygame.time.Clock() - for FPS

    def fire_bullet(self,x,y):
        self.bullet.bullet_state = "fire"
        self.screen.blit(self.bullet.bulletImg,(x,y))

        

    def _KeyDown_Event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.playerX_Change = self.settings.ship_speed
        elif event.key == pygame.K_LEFT:
            self.ship.playerX_Change = -self.settings.ship_speed

        elif event.key == pygame.K_UP:
            self.ship.playerY_Change = -self.settings.ship_speed 
        elif event.key == pygame.K_DOWN:
            self.ship.playerY_Change = self.settings.ship_speed        

        elif event.key==pygame.K_SPACE:
                if self.bullet.bullet_state == "ready":
                    self.bullet.bulletX = self.ship.playerX
                    self.bullet.bulletY = self.ship.playerY
                    self.fire_bullet(self.bullet.bulletX,self.bullet.bulletY)      


    def _Key_Up_Event(self,event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.ship.playerX_Change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.ship.playerY_Change = 0    


    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.K_q:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._KeyDown_Event(event)

            elif event.type == pygame.KEYUP:
                self._Key_Up_Event(event)
     
    def isCollision(self,alienX,alienY,bulletX,bulletY):

        self.screen.blit(self.aliens.alien,(self.aliens.alienX,self.aliens.alienY))

        self.distance=math.sqrt(((bulletX-alienX)*(bulletX-alienX))+((bulletY-alienY)*(bulletY-alienY)))
        if self.distance < 30:
            self.screen.blit(self.aliens.alien,(self.aliens.alienX,self.aliens.alienY))

    def _update_events(self):

            pygame.display.flip()

            self.screen.fill(self.settings.bg_color)

            if self.ship.playerX <= 0:
                self.ship.playerX = 0
            elif self.ship.playerX >=1540:
                self.ship.playerX = 1540  

            if self.ship.playerY <= 200:
                self.ship.playerY = 200    
            elif self.ship.playerY >= 700:
                self.ship.playerY =700


            self.ship.playerX += self.ship.playerX_Change

            self.ship.playerY += self.ship.playerY_Change



            self.screen.blit(self.ship.player,(self.ship.playerX,self.ship.playerY))

            


    def run_game(self):

        while True:

            self._check_events()

            if self.bullet.bulletY <= 0:
                self.bullet.bullet_state = "ready"
                self.bullet.bulletY = 630    
        
            if self.bullet.bullet_state=="fire":
                self.fire_bullet(self.bullet.bulletX,self.bullet.bulletY)  
                self.bullet.bulletY -= self.bullet.bulletY_change    

            self._update_events()

            #self.clock.tick(60) - Asigned to 60 fps


if __name__=='__main__':

    ai = Alien_Invader()
    ai.run_game()            
