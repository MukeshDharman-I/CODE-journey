import pygame
import math
import sys # to exit
import random # for movement of alien

'''
gonna use a formul , distance between two points and the midpoint

D=square_root((X2-X1)^2 + (Y2-Y1)^2)'''

#initialize pygame
pygame.init()

#screen                       width , height
screen=pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Alien_Shooter")

icon=pygame.image.load("images/logo.bmp")
pygame.display.set_icon(icon)

#player , spaceship
playerImg=pygame.image.load("images/ship.bmp")
playerX_change=0
playerX=300
playerY=480

# for more num of aliens

alienImg=[]
alienX=[]
alienY=[]
alienX_change=[]
alienY_change=[]
num_of_aliens=6

#alien 
for i in range(num_of_aliens):
    alienImg.append(pygame.image.load("images/alien.bmp"))
    alienX.append(500)
    alienY.append(200)
    alienY_change.append(0)
    alienX_change.append(0.3)

#bullet
#ready-you can't see the bullet on the screen
#fir-the bullet is curently moving
bulletImg=pygame.image.load("images/bullet.bmp")
bulletX=0
bulletY=480
bulletY_change=3
bulletX_change=0
bullet_state="ready"

#Score
score=0

def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))        # draws image(player)

def alien(alienX,alienY,i):
    screen.blit(alienImg[i],(alienX,alienY))        # draws image(alien)

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y))

def isCollision(alienX,alienY,bulletX,bulletY):
    # formula
    distance=math.sqrt(((bulletX-alienX)*(bulletX-alienX))+((bulletY-alienY)*(bulletY-alienY)))
    if distance < 30:
        return True
    else:
        return False
#or clossing the screen
while True:
    
    for event in pygame.event.get(): # all event that happens 
        if event.type==pygame.QUIT: #if the event is quit (if clicked on close) it quits
            sys.exit() 
    # if keystroke is pressed check whether it is right keyoor left key
        if event.type==pygame.KEYDOWN:
            # a key is pressed
            if event.key==pygame.K_RIGHT:
                playerX_change = 1
            elif event.key==pygame.K_LEFT:
                #left key is pressed
                playerX_change = -1
            elif event.key==pygame.K_SPACE:
                #space key is pressed
                if bullet_state == "ready":
                    #get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        elif event.type==pygame.KEYUP:
            # checks whether key is released
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT: 
                playerX_change=0 # resets change value at once the key is released


    #Adding bg color
    screen.fill((33,71,97))     

    #moving ship while pressing 
    playerX+=playerX_change

    #setting boundary
    if playerX <= 0:
        playerX=0
    elif playerX >=736:
        playerX=736

    player(playerX,playerY) # called after the screen is done (first screen then image on top of screen)
 
 #checking boundaries for alien
    for i in range(num_of_aliens):
        alienX[i]+=alienX_change[i]

        if alienX[i] <= 0:
            alienY_change[i]=10 # to make alien move down
            alienY[i]+=alienY_change[i] # changes the value of
            alienX_change[i]=0.3
            alienY_change[i]=0 # resets y axis value
        elif alienX[i] >=740:
            alienY_change[i]=10
            alienY[i]+=alienY_change[i]
            alienX_change[i]=-0.3
            alienY_change[i]=0
        collision=isCollision(alienX[i],alienY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state="ready"
            score+=1
            alienX[i]=random.randint(0,750)
            alienY[i]=random.randint(50,150)    

    alien(alienX[i],alienY[i],i) # called after the screen is done (first screen then image on top of screen)

    #bullet movement
    if bulletY <= 0:
        bulletY=480
        bullet_state="ready"

    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)  
        bulletY -= bulletY_change    



    pygame.display.update() # updating the screen as the players are gonna move  