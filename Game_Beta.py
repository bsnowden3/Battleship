#Yuechen(Mark) Yang ------(markyang@mit.edu)----------------
#partners: Bernard Snowden, Kevin Rodriguez
#Game class---------------------------------------------------------------------
import os
import pygame, sys
from pygame.locals import *
import time
import random
from Ocean import *
from ship import *

pygame.init()

#colors and initials-------------------------------------------------------------------------
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0,0,255)
green = (50,205,50)
ending = s = e = False
ending = s = e = False
corners = (225,400)  #Top Left corner of start button
cornere = (225,475)  #Top Left corner of exit button
button_length = 300 #length of the buttons
button_height = 50 #height of the buttons
clock = pygame.time.Clock()

#startscreen------------------------------------------------------------------------------
def start_screen():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Battleship")
    screen.fill(black)

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

#Main Loop----------------------------------------------------------------------

def main_loop(screen, ocean, ocean_2, Ships, game, ending):

    ocean.draw_grid(screen) 
    ocean_2.draw_grid(screen)
    ocean.Ships.rect = ocean.battleShip.getRect()
    ocean.Ships.draw(screen)
    pygame.display.flip()
        
    while ending==False:

        #game.hitmarker(ocean, ocean_2, ship)
        ocean.Ships.rect = ocean.battleShip.getRect()
        #ocean.Ships.draw(screen)
        game.moves()
        #game.hitmarker(ocean, ocean_2, ship)
        #game.aim(ocean, ocean_2)
        pygame.display.flip() # update screen

        game.victory(ocean, ocean_2) #checks for win or lose

#ocean = Ocean()
#ocean_2 = Player_Ocean()
#ships = Ship(x,y, orientation)
#Main Game class----------------------------------------------------------------
class Game:
    
    def __init__(self, ocean, ocean_2):
        self.coord = (11,0)
        self.enemyx = int(self.coord[0]) * 50 + 10
        self.enemyy = int(self.coord[1]) * 50 + 10
        self.player_remains = ocean.Remains() # to check moves and ships
        self.enemy_remains = ocean_2.Remains()
        self.turn = 0
        #self.adjhealth = Ships.adjustHealth(value)
        #self.moves = moves                               
        #self.enemy_moves = enemy_moves
        self.vic = 'Admiral, enemy fleet annihilated! "R" to replay'
        self.defeat = 'Admiral! Our fleet has been destroyed! "R" to replay'
#movement-----------------------------------------------------------------------
    def player_turn(self, ocean, ocean_2):    # this handles the player actions
        self.coord = self.aim(ocean, ocean_2)
        x = int(self.coord[0])
        y = int(self.coord[1])
        attack_coord = (x,y)
        if x >= 11 and x <= 20 and y >= 0 and y <= 9:
            if ocean_2.Chk_tile(attack_coord) == True:
                key = ocean_2.ship_at_Location(attack_coord)
                ocean_2.shipsDict[key].adjustHealth(attack_coord)
                print 'enemy vessel hit!'
                hit = pygame.image.load("Hitmarker.png") # draw logo
                rect = hit.get_rect()               
                rect.x, rect.y = (x * 50 + 10, y * 50 + 10)
                screen.blit(hit,(rect.x, rect.y))
                pygame.display.flip()
                pygame.mixer.music.load('cannonhit.wav')
                pygame.mixer.music.play(0)
                time.sleep(1)
                print ocean_2.shipsDict[key]
                print ocean_2.shipsDict[key].getHealth()
                print ocean_2.Remains()

            elif ocean_2.Chk_tile(attack_coord) == False:
                print 'shot missed!'
                empty = pygame.image.load("empty.png") # draw logo
                rectempty = empty.get_rect()               
                rectempty.x, rectempty.y = (x * 50 + 17, y * 50 + 17)
                screen.blit(empty,(rectempty.x, rectempty.y))
                pygame.display.flip()
                pygame.mixer.music.load('splash.wav')
                pygame.mixer.music.play(0)
                time.sleep(1)
        else:
            print "Please enter valid coordinates."
            self.player_turn(ocean, ocean_2)
            
    def enemy_turn(self, ocean, ocean_2):     # this handles computer actions

        attack_coord = (random.randint(0,9),random.randint(0,9))
        x = int(attack_coord[0])
        y = int(attack_coord[1])

        if ocean.Chk_tile(attack_coord) == True:
            key = ocean.ship_at_Location(attack_coord)
            ocean.shipsDict[key].adjustHealth(attack_coord)
            hit = pygame.image.load("fire.png") # draw logo
            rect = hit.get_rect()               
            rect.x, rect.y = (x * 50 + 10, y * 50 + 10)
            screen.blit(hit,(rect.x, rect.y))
            pygame.display.flip()
            pygame.mixer.music.load('cannonhit.wav')
            pygame.mixer.music.play(0)
            time.sleep(1)
            print 'our ship is hit!'
            

        elif ocean.Chk_tile(attack_coord) == False:
            print 'they missed!'
            empty = pygame.image.load("empty.png") # draw logo
            rectempty = empty.get_rect()               
            rectempty.x, rectempty.y = (x * 50 + 17, y * 50 + 17)
            screen.blit(empty,(rectempty.x, rectempty.y))
            pygame.display.flip()
            pygame.mixer.music.load('splash.wav')
            pygame.mixer.music.play(0)
            time.sleep(1)

    def moves(self):

        if self.turn == 0 or self.turn % 2 == 0: # player plays first 
            self.player_turn(ocean, ocean_2)                # player_turn() includes attack mechanism
            self.turn += 1
            
        else:                            # computer plays next
            self.enemy_turn(ocean, ocean_2)
            self.turn += 1
            

#screens-----------------------------------------------------------------------                       

    def end_screen(self, condition):
        
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(black)  # first fills the screen black
        font = pygame.font.Font(None, 42)   # prints out victory remarks
        font = font.render(condition, 1, white)
        textpos = font.get_rect()   # set victory remark location
        textpos.centerx = background.get_rect().centerx # text at center
        textpos.centery = background.get_rect().centery
                
        background.blit(font,textpos)
        screen.blit(background, (0,0))
        pygame.display.flip()         
        cd = True
        while cd == True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        cd = False
                        start_screen()
                        

#endgame-----------------------------------------------------------------------        
    def victory(self, ocean, ocean_2):  # sets victory and defeat conditions

        if ocean_2.Remains()== 0:    # if enemy ships remain = 0
            self.end_screen(self.vic) #print victory screen

        elif ocean.Remains() == 0: # if player ships remain = 0
            self.end_screen(self.defeat)  #print defeat screen

#extra features-----------------------------------------------------------------
#cross hair-------------------------------------------------------------------
    def aim(self, ocean, ocean_2):
        width = 50
        height = 50
        x = int(self.coord[0])
        y = int(self.coord[1])
        c = True
        while c == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       # quit when clicks x
                    ending=True          
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if self.enemyx >= 560 and self.enemyx <= 1010 and self.enemyy >=10 and self.enemyy <=460:    
                        if event.key == pygame.K_RIGHT and self.enemyx + 50 != 1060:
                            self.enemyx += 50
                            x += 1
                        elif event.key == pygame.K_LEFT and self.enemyx - 50 != 510:
                            self.enemyx -= 50
                            x -=1
                        elif event.key == pygame.K_UP and self.enemyy - 50 != -40:
                            self.enemyy -= 50
                            y -= 1
                        elif event.key == pygame.K_DOWN and self.enemyy + 50 != 510:
                            self.enemyy += 50
                            y += 1
                        elif event.key == pygame.K_RETURN:
                            c = False
                            return self.coord
                            
                        else:
                            print "not the above"
                        self.coord = (x,y)
                        print self.coord
                        #ocean.draw_grid(screen) 
                        ocean_2.draw_grid(screen)
                        #ocean.Ships.rect = ocean.battleShip.getRect()
                        #ocean.Ships.draw(screen)

                        cross_hair = pygame.draw.rect(screen, green, (self.enemyx,self.enemyy,50,50), 5)
                        pygame.display.flip()
        #cross_hair = pygame.draw.rect(screen, green, (enemyx,enemyy,50,50), 6)
    """
    def screen_shake():
        s = -1
    for n in xrange(0, 3):
        for x in range(0, 20, 8):
            yield (x*s, 0)
        for x in range(20, 0, 8):
            yield (x*s, 0)
        s *= -1
    while True:
        yield (0, 0)
    """
#Hitmarker----------------------------------------------------------------------
    """def hitmarker(self, ocean, ocean_2, ship):
        for part in ship.status:
            if ship.status[i][2] == False:
                hit = pygame.image.load("Hitmarker.png") # draw logo
                rect = image.get_rect()               
                rect.x, rect.y = (ship.status[i][0] * 50 + 10, ship.status[i][1] * 50 + 10)
                screen.blit(hit,(rect.x, rect.y))"""
#runs game---------------------------------------------------------------------
start_screen()

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
                    time.sleep(2)
                    print "Game Start!"
                    ocean = Ocean()
                    ocean_2 = Player_Ocean()
                    game = Game(ocean, ocean_2)
                    screen_width = 1150
                    screen_height = 550
                    screen = pygame.display.set_mode([screen_width,screen_height])
                    screen.fill(blue)
                    main_loop(screen, ocean, ocean_2, ocean.Ships, game, ending)
                    buttons=True
                    buttone=False
                elif (mouse_x >= cornere[0]) and (mouse_x <= cornere[0]+button_length) and (mouse_y >= cornere[1]) and (mouse_y <= cornere[1]+button_height):
                    print "Exit"            # Same idea, for exit button
                    buttons=False
                    buttone=True
                    pygame.quit()
