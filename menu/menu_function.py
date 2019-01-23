##Menu

import pygame
from pygame import *
from math import *

menuimage=image.load("menu screen.png")
menuplayon=image.load("menu play collide.png")
menuplayRect=Rect(729,428,134,66)
menuinstructionon=image.load("menu instructions collide.png")
menuinstructionRect=Rect(586,505,387,57)
instruction=image.load("instruction screen.png")
instructionmenuon=image.load("instruction screen menu collide.png")
instructionmenuRect=Rect(100,519,92,32)
instructionplayon=image.load("instruction screen play collide.png")
instructionplayRect=Rect(804,517,69,38)

screen = display.set_mode((1000,600))
pygame.display.set_caption("Marvel Street Fighter")
font.init()

mx=0
my=0

menuscreen=True
instructionscreen=False
play=False

running = True

def menu():
    global menuscreen, instructionscreen, play, mx, my
    if menuscreen==True:
        if instructionscreen==False and play==False:
            screen.blit(menuimage,(0,0))
        if menuplayRect.collidepoint(mx,my) and instructionscreen==False and play==False:
            screen.blit(menuplayon,(0,0))
            if mb[0]==1:
                play=True
                menuscreen=False
                instructionscreen=False
        if menuinstructionRect.collidepoint(mx,my):
            screen.blit(menuinstructionon,(0,0))
            if mb[0]==1:
                screen.blit(instruction,(0,0))
                play=False
                instructionscreen=True
                menuscreen=False
                
    if instructionscreen==True and play==False and menuscreen==False:
        screen.blit(instruction,(0,0))
        if instructionplayRect.collidepoint(mx,my):
            screen.blit(instructionplayon,(0,0))
            if mb[0]==1:
                play=True
                menuscreen=False
                instructionscreen=False
        if instructionmenuRect.collidepoint(mx,my):
            screen.blit(instructionmenuon,(0,0))
            if mb[0]==1:
                screen.blit(menuimage,(0,0))
                instructionscreen=False
                menuscreen=True
                play=False




while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    
    mx1=mx
    my1=my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    mb1=mb

    menu()
    display.flip()
quit()
