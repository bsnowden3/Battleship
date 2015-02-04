import time
import pygame, sys
from pygame.locals import *

black = (0,0,0)

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship")
screen.fill(black)

ending = s = e = False

corners = (225,400)  #Top Left corner of start button
cornere = (225,475)  #Top Left corner of exit button

button_length = 300 #length of the buttons
button_height = 50 #height of the buttons

def start_screen():
  
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    image = pygame.image.load("sc.png") # draw logo
    rect = image.get_rect()               
    rect.x, rect.y = (125, 50)

    start_button = pygame.image.load("start.png") # draw start button
    recs = start_button.get_rect()
    recs.x, recs.y = (225,400)

    exit_button = pygame.image.load("exit.png") # draw exit button
    rece = start_button.get_rect()
    rece.x, rece.y = (225,475)
    
    screen.blit(image,(rect.x, rect.y))        # out puts everything to screen
    screen.blit(exit_button,(rece.x, rece.y))
    screen.blit(start_button,(recs.x, recs.y))
    pygame.display.flip()

start_screen()

#Main Loop:---------------------------------------------------------------------
while ending==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # quit when clicks x
            ending=True          
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos   # the line below checks for where the mouse is, if it falls in button and clicks, do task
                if (mouse_x >= corners[0]) and (mouse_x <= corners[0]+button_length) and (mouse_y >= corners[1]) and (mouse_y <= corners[1]+button_height):
                    pygame.mixer.music.load('firing.wav')
                    pygame.mixer.music.play(0)
                    time.sleep(3)
                    print "Game Start!"
                    #Game_loop()
                    buttons=True
                    buttone=False
                elif (mouse_x >= cornere[0]) and (mouse_x <= cornere[0]+button_length) and (mouse_y >= cornere[1]) and (mouse_y <= cornere[1]+button_height):
                    print "Exit"            # Same idea, for exit button
                    buttons=False
                    buttone=True
                    pygame.quit()
