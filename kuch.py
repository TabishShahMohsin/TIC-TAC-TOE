
import keyboard
import random
import pygame
import sys
# pip install keyboard
import os




pygame.init()


screen=pygame.display.set_mode((1280,720) )
pygame.display.set_caption("Tic-Tac-Toe")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock=pygame.time.Clock


test_surface=pygame.Surface(1280,720)
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(test_surface)
            
    pygame.display.update()
    clock.tick(60)
    