#Marvel Street Fighter
#Johnny Fung

import pygame
from pygame import *
from math import *

#Song
init()
mixer.music.load("song/21 brothers fight.mp3")
mixer.music.play()

#Menu and instruction screen loads and rects
menu=image.load("menu/menu screen.png")
menuplayon=image.load("menu/menu play collide.png")
menuplayRect=Rect(729,428,134,66)
menuinstructionon=image.load("menu/menu instructions collide.png")
menuinstructionRect=Rect(586,505,387,57)
instruction=image.load("menu/instruction screen.png")
instructionmenuon=image.load("menu/instruction screen menu collide.png")
instructionmenuRect=Rect(100,519,92,32)
instructionplayon=image.load("menu/instruction screen play collide.png")
instructionplayRect=Rect(804,517,69,38)

#Menu function
def menuandinstructions():
    global menuscreen, instructionscreen, play, mx, my
#Flags to make sure game is not running  	   
    if menuscreen==True and instructionscreen==False and play==False:
        screen.blit(menu,(0,0))
#Indicator to show user the buttons
        if menuplayRect.collidepoint(mx,my) and instructionscreen==False and play==False:
            screen.blit(menuplayon,(0,0))
#Sets the flags to play the game and turn off the menu.
            if mb[0]==1:
                play=True
                menuscreen=False
                instructionscreen=False
#Instruction screen button indicator
        if menuinstructionRect.collidepoint(mx,my):
            screen.blit(menuinstructionon,(0,0))
#Gives the user the instructions and makes sure the game is not on
            if mb[0]==1:
                screen.blit(instruction,(0,0))
                play=False
                instructionscreen=True
                menuscreen=False
#Indicator for play button               
    if instructionscreen==True and play==False and menuscreen==False:
        screen.blit(instruction,(0,0))
        if instructionplayRect.collidepoint(mx,my):
            screen.blit(instructionplayon,(0,0))
#Changes the flags which activates the game
            if mb[0]==1:
                play=True
                menuscreen=False
                instructionscreen=False
#From instruction screen back to menu
        if instructionmenuRect.collidepoint(mx,my):
            screen.blit(instructionmenuon,(0,0))
            if mb[0]==1:
                screen.blit(menu,(0,0))
                instructionscreen=False
                menuscreen=True
                play=False    
    display.flip()

#Thor sprite storage
thorstance=[]
thorstanceleft=[]
thorright=[]
thorleft=[]
thorattack1=[]
thorattack1left=[]
thorattack2=[]
thorattack2left=[]
thorjumpright=[]
thorjumpleft=[]
#Used to set his position after running in a certain direction
thorcurrent="tr"
#Sprite animation variables
thorstanceframe=0
thorstanceframedelay=1
thorrunframe=0
thorrunframedelay=1
thorjumpframe=0
thorjumpframedelay=1

#Thor Sprites
#Uploads the sprites and adds them into the list
#Stance
for i in range (8):
    thorstance.append(image.load("avengers/thor/thorstance/thorstance "+str(i)+".png"))
    thorstanceleft.append(image.load("avengers/thor/thorstanceleft/thorstanceleft "+str(i)+".png"))
#Run
for i in range(11):
    thorright.append(image.load("avengers/thor/thorrunright/thorrunright "+str(i)+".png"))
    thorleft.append(image.load("avengers/thor/thorrunleft/thorrunleft "+str(i)+".png"))
#Attack 1
    thorattack1.append(image.load("avengers/thor/thorattackone/thorattackone "+str(i)+".png"))
    thorattack1left.append(image.load("avengers/thor/thorattackoneleft/thorattackoneleft "+str(i)+".png"))
#Attack 2
    thorattack2.append(image.load("avengers/thor/thorattacktwo/thorattacktwo "+str(i)+".png"))
    thorattack2left.append(image.load("avengers/thor/thorattacktwoleft/thorattacktwoleft "+str(i)+".png"))
#Jump    
for i in range(9):
    thorjumpright.append(image.load("avengers/thor/thor jump right/thor jump right "+str(i)+".png"))
    thorjumpleft.append(image.load("avengers/thor/thor jump left/thor jump left "+str(i)+".png"))

#Thor - Used for when not moving
#Used to set his position after running in a certain direction
thorcurrent=[]

#Hogun sprites storage
hogunstance=[]
hogunstanceleft=[]
hogunright=[]
hogunleft=[]
hogunattack1=[]
hogunattack1left=[]
hogunattack2=[]
hogunattack2left=[]
hogunjumpright=[]
hogunjumpleft=[]
#Hogun's current position, before he is moved
hoguncurrent="hl"
#Hogun animation variables
hogunstanceframe=0
hogunstanceframedelay=1
hogunrunframe=0
hogunrunframedelay=1
hogunattackframe=0
hogunattackframedelay=1
hogunjumpframe=0
hogunjumpframedelay=1

#Hogun Sprites
#Uploads the sprites and adds them into the list
#Stance
for i in range (6):
    hogunstance.append(image.load("avengers/hogun/hogun stance/hogun stance "+str(i)+".png"))
    hogunstanceleft.append(image.load("avengers/hogun/hogun stance left/hogun stance left "+str(i)+".png"))
#Run
for i in range(9):
    hogunright.append(image.load("avengers/hogun/hogun run/hogun run "+str(i)+".png"))
    hogunleft.append(image.load("avengers/hogun/hogun run left/hogun run left "+str(i)+".png"))
#Attack 1
for i in range(7):
    hogunattack1.append(image.load("avengers/hogun/hogun attackone/hogun attackone "+str(i)+".png"))
    hogunattack1left.append(image.load("avengers/hogun/hogun attackone left/hogun attackone left "+str(i)+".png"))
#Attack 2
    hogunattack2.append(image.load("avengers/hogun/hogun attacktwo/hogun attacktwo "+str(i)+".png"))
    hogunattack2left.append(image.load("avengers/hogun/hogun attacktwo left/hogun attacktwo left "+str(i)+".png"))
#Jump    
for i in range(9):
    hogunjumpright.append(image.load("avengers/hogun/hogun jump/hogun jump "+str(i)+".png"))
    hogunjumpleft.append(image.load("avengers/hogun/hogun jump left/hogun jump left "+str(i)+".png"))

#Hogun
#Used to set his position after running in a certain direction
hoguncurrent=[]

screen = display.set_mode((1000,600))
#Sets the window title
pygame.display.set_caption("Marvel Street Fighter")
font.init()
#Background picture
backpic1=image.load("backgrounds/bg1.png")
#Health bar
thorhp=image.load("avengers/hp bars/thorhp.png")
hogunhp=image.load("avengers/hp bars/hogunhp.png")

#Position of characters
X=0
Y=1

init()
myClock = time.Clock()

#Flags to set the game
menuscreen=True
instructionscreen=False
play=False
gameover=False

def framethorstance():
    global thorstanceframe,thorstanceframedelay
#Makes the image blit slower instead of blitting it instantly
    myClock.tick(11)
#Resets the frame for the animation
    thorstanceframedelay-=1
#Adds and subtracts frame to reset the animation
    if thorstanceframedelay==0:
        thorstanceframedelay=1
        thorstanceframe+=1
#Resets when all the images in the list get blit
    if thorstanceframe==7: thorstanceframe =0

def framethorrunandattack():
    global thorrunframe,thorrunframedelay
    myClock.tick(16)
    thorrunframedelay-=1
    if thorrunframedelay==0:
        thorrunframedelay=1
        thorrunframe+=1
    if thorrunframe==11: thorrunframe =0

def framethorjump():
    global thorjumpframe,thorjumpframedelay
    myClock.tick(10)
    thorjumpframedelay-=1
    if thorjumpframedelay==0:
        thorjumpframedelay=1
        thorjumpframe+=1
    if thorjumpframe==9: thorjumpframe =0

def framehogunstance():
    global hogunstanceframe,hogunstanceframedelay
    myClock.tick(11)
    hogunstanceframedelay-=1
    if hogunstanceframedelay==0:
        hogunstanceframedelay=1
        hogunstanceframe+=1
    if hogunstanceframe==6: hogunstanceframe =0
    

def framehogunrun():
    global hogunrunframe,hogunrunframedelay
    myClock.tick(17)
    hogunrunframedelay-=1
    if hogunrunframedelay==0:
        hogunrunframedelay=1
        hogunrunframe+=1
    if hogunrunframe==9: hogunrunframe =0

def framehogunattack():
    global hogunattackframe,hogunattackframedelay
    myClock.tick(14)
    hogunattackframedelay-=1
    if hogunattackframedelay==0:
        hogunattackframedelay=1
        hogunattackframe+=1
    if hogunattackframe==6: hogunattackframe =0

def framehogunjump():
    global hogunjumpframe,hogunjumpframedelay
    myClock.tick(50)
    hogunjumpframedelay-=1
    if hogunjumpframedelay==0:
        hogunjumpframedelay=1
        hogunjumpframe+=1
    if hogunjumpframe==9: hogunjumpframe =0

#Sets up the game screen    
def drawScene(screen,char1,char2):
    global keys,thorcurrent,hoguncurrent,char1Rect,char2Rect,char1hp,char2hp,char2hpstart,char2hplength
    global gameover,menuscreen,instructionscreen,play,p1win
    screen.blit(backpic1,(0,0))
#If the user presses the button, run the frame to blit the animations
    if keys[K_d]:
#Calls the fuction that controls the frame blit rate
        framethorrunandattack()
#Blits at the character's X,Y coordinates which is adjusted below
        screen.blit(thorright[thorrunframe],(char1[X],char1[Y]+520))
#Sets the current position he is facing
        thorcurrent="tr"
    elif keys[K_a]:
        framethorrunandattack()
        screen.blit(thorleft[thorrunframe],(char1[X],char1[Y]+520))
        thorcurrent="tl"
    elif keys[K_w] and thorcurrent=="tr":
        framethorjump()
        screen.blit(thorjumpright[thorjumpframe],(char1[X],char1[Y]+490))
        thorcurrent="tr"
    elif keys[K_w] and thorcurrent=="tl":
        framethorjump()
        screen.blit(thorjumpleft[thorjumpframe],(char1[X],char1[Y]+490))
        thorcurrent="tl"
    elif keys[K_i] and thorcurrent=="tr":
        framethorrunandattack()
        screen.blit(thorattack1[thorrunframe],(char1[X],char1[Y]+490))
        thorcurrent="tr"
    elif keys[K_i] and thorcurrent=="tl":
        framethorrunandattack()
        screen.blit(thorattack1left[thorrunframe],(char1[X],char1[Y]+490))
        thorcurrent="tl"
    elif keys[K_o] and thorcurrent=="tr":
        framethorrunandattack()
        screen.blit(thorattack2[thorrunframe],(char1[X],char1[Y]+500))
        thorcurrent="tr"
    elif keys[K_o] and thorcurrent=="tl":
        framethorrunandattack()
        screen.blit(thorattack2left[thorrunframe],(char1[X],char1[Y]+500))
        thorcurrent="tl"
#If no key is pressed, it blits the Thor stance
    else:
        if thorcurrent=="tr":
            framethorstance()
            screen.blit(thorstance[thorstanceframe],(char1[X],char1[Y]+520))
        if thorcurrent=="tl":
            framethorstance()
            screen.blit(thorstanceleft[thorstanceframe],(char1[X],char1[Y]+520))
    #Hogun hp lower
#When the user pressing attack key and if they two characters collide.
    if keys[K_i] and char1Rect.collidepoint(char2[X],char2[Y]):
        myClock.tick(5)
#The other character loses hp
        char2hp+=9
    if keys[K_o] and char1Rect.collidepoint(char2[X],char2[Y]):
        myClock.tick(5)
        char2hp+=9
    #Hogun
    if keys[K_RIGHT]:
        framehogunrun()
        screen.blit(hogunright[hogunrunframe],(char2[X],char2[Y]+510))
        hoguncurrent="hr"
    elif keys[K_LEFT]:
        framehogunrun()
        screen.blit(hogunleft[hogunrunframe],(char2[X],char2[Y]+510))
        hoguncurrent="hl"
    elif keys[K_UP] and hoguncurrent=="hr":
        framehogunjump()
        screen.blit(hogunjumpright[hogunjumpframe],(char2[X],char2[Y]+490))
        hoguncurrent="hr"
    elif keys[K_UP] and hoguncurrent=="hl":
        framehogunjump()
        screen.blit(hogunjumpleft[hogunjumpframe],(char2[X],char2[Y]+490))
        hoguncurrent="hl"
    elif keys[K_KP2] and hoguncurrent=="hr":
        framehogunattack()
        screen.blit(hogunattack1[hogunattackframe],(char2[X],char2[Y]+500))
        hoguncurrent="hr"
    elif keys[K_KP2] and hoguncurrent=="hl":
        framehogunattack()
        screen.blit(hogunattack1left[hogunattackframe],(char2[X],char2[Y]+500))
        hoguncurrent="hl"
    elif keys[K_KP3] and hoguncurrent=="hr":
        framehogunattack()
        screen.blit(hogunattack2[hogunattackframe],(char2[X],char2[Y]+500))
        hoguncurrent="hr"
    elif keys[K_KP3] and hoguncurrent=="hl":
        framehogunattack()
        screen.blit(hogunattack2left[hogunattackframe],(char2[X],char2[Y]+500))
        hoguncurrent="hl"
    else:
        if hoguncurrent=="hr":
            framehogunstance()
            screen.blit(hogunstance[hogunstanceframe],(char2[X],char1[Y]+510))
        if hoguncurrent=="hl":
            framehogunstance()
            screen.blit(hogunstanceleft[hogunstanceframe],(char2[X],char1[Y]+510))
    #Thor hp lower
#Same as Thor attacks
    if keys[K_KP2] and char2Rect.collidepoint(char1[X]+50,char1[Y]):
        myClock.tick(5)
        char1hp-=9
        if char1hp<=0: char1hp=0
    if keys[K_KP3] and char2Rect.collidepoint(char1[X]+50,char1[Y]):
        myClock.tick(5)
        char1hp-=9

        if char1hp<=0: char1hp=0
    #HP bars
#Increase start position of the second player's hp bar every time he gets hit
    char2hpstart=673+char2hp
#Decreases length of hp bar everytime he gets hit
    char2hplength=308-char2hp
    screen.blit(hogunhp,(567,0))
    draw.rect(screen,(255,0,0),(char2hpstart,69,char2hplength,42))
    screen.blit(thorhp,(0,0))
    draw.rect(screen,(255,0,0),(20,69,char1hp,42))
#Makes sure the hp bar will not continue to decrease so it will end when
#character 2 has no health    
    if char2hpstart>=980:
        char2hplength=0
#Game Over screens
        p1win()
    if char1hp==0:
        p2win()
    display.flip()

def moveChar1(char1):
    global keys
#Sets boundaries so the characters cannot go off the screen and adds/subtracts
#the coordinates when the user is going left/right
    if keys[K_d] and char1[X]<950 :
        char1[X]+=8
    if keys[K_a] and char1[X]>0:
        char1[X]-=8    
##    if keys[K_w] and keys[K_d] and char1[Y]>470:
##        char1[Y] -=7
##        char1[X] +=7
##        if char1[Y]<470 or char1[Y]==470:
##            char1[Y]-=7
##            if char1[Y]>520:
##                char1[Y]==520
##    if keys[K_w] and keys[K_a] and char1[Y]>470:
##        char1[Y] -=7
##        char1[X] -=7
##        if char1[Y]<=470 or char1[Y]==470:
##            char1[Y]-=7
##            if char1[Y]>530:
##                char1[Y]==520      

def moveChar2(char2):
    global keys
#Sets boundaries so the characters cannot go off the screen and adds/subtracts
#the coordinates when the user is going left/right
    if keys[K_RIGHT] and char2[X]<950 :
        char2[X]+=8
    if keys[K_LEFT] and char2[X]>0:
        char2[X]-=8
##    if keys[K_UP] and char2[Y]>470:
##        char2[Y] -=7
##        char2[X] -=7
##        if char2[Y]<=470 or char2[Y]==470:
##            char2[Y]-=7
##            if char2[Y]>530:
##                char2[Y]==520

#Game Over image loads and Rect sizes
p1wins=image.load("game over/p1off.png")
p1winsquit=image.load("game over/p1on.png")
p1quitRect=Rect(784,432,145,46)
p2wins=image.load("game over/p2off.png")
p2winsquit=image.load("game over/p2on.png")
p2quitRect=Rect(784,476,145,46)

#Tells the users who won
def p1win():
    screen.blit(p1wins,(0,0))
#Quit the game after someone loses
    if p1quitRect.collidepoint(mx,my):
        screen.blit(p1winsquit,(0,0))
        if mb[0]==1:
            quit()

def p2win():
    screen.blit(p2wins,(0,0))
    if p2quitRect.collidepoint(mx,my):
        screen.blit(p2winsquit,(0,0))
        if mb[0]==1:
            quit()

running = True          
char1hp=307
char1=[290,0,0]
char2hp=0
char2=[580,0,0]
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    keys=key.get_pressed()
    mb1=mb
    
#Rects of the characters for - used for hp loss
    char1Rect=Rect(char1[X],char1[Y],70,70)
    char2Rect=Rect(char2[X],char2[Y],70,70)

#Starts the menu screen
    menuandinstructions()

#If the menu and instruction screen is not on, then start the game and activate the functions.
    if play==True and menuscreen==False and instructionscreen==False and gameover==False:
        moveChar1(char1)
        moveChar2(char2)
        drawScene(screen,char1,char2)

    display.flip()
quit()
