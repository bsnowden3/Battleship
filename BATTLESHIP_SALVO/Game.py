#Yuechen(Mark) Yang ------(markyang@mit.edu)------------------------------------
#Game class---------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
import time
import random
from Ocean import *
from ship import *

#colors and initials-------------------------------------------------------------------------
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0,0,255)

screen_width = 1150
screen_height = 550
screen = pygame.display.set_mode([screen_width,screen_height])
screen.fill(blue)
ending = s = e = False
#Main Loop----------------------------------------------------------------------

def main_loop(screen, ocean, ocean_2, Ships, game, ending):

    ocean.draw_grid(screen) 
    ocean_2.draw_grid(screen)
    ocean.Ships.rect = ocean.battleShip.getRect()
    ocean.Ships.draw(screen)
    pygame.display.flip() # update screen

    while ending==False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # quit when clicks x
                ending=True          
                pygame.quit()

        game.moves() # starts turns
        ocean.draw_grid(screen) 
        ocean_2.draw_grid(screen)
        ocean.Ships.rect = ocean.battleShip.getRect()
        ocean.Ships.draw(screen)
        pygame.display.flip() # update screen

        game.victory(ocean, ocean_2) #checks for win or lose

ocean = Ocean()
ocean_2 = Player_Ocean()

#Main Game class----------------------------------------------------------------
class Game:
    
    def __init__(self, ocean, ocean_2):

        self.player_remains = ocean.Remains() # to check moves and ships
        self.enemy_remains = ocean_2.Remains()
        #self.adjhealth = Ships.adjustHealth(value)
        #self.moves = moves                               
        #self.enemy_moves = enemy_moves
        self.vic = 'Admiral, enemy fleet annihilated! "R" to replay'
        self.defeat = 'Admiral! Our fleet has been destroyed! "R" to replay'
#movement-----------------------------------------------------------------------
    def player_turn(self, ocean, ocean_2):    # this handles the player actions
        
        attack_coord = raw_input("Adjust target coordinates: ") # input coord in form: letter,number
        attack_coord = tuple(attack_coord.split(',')) # make input into a tuple
        attack_coord = (int(attack_coord[0]),int(attack_coord[1]))

        if ocean_2.Chk_tile(attack_coord) == True:
            key = ocean_2.ship_at_Location(attack_coord)
            ocean_2.shipsDict[key].adjustHealth(attack_coord)
            print 'enemy vessel hit!'
            print ocean_2.shipsDict[key]
            print ocean_2.shipsDict[key].getHealth()
            print ocean_2.Remains()

        elif ocean_2.Chk_tile(attack_coord) == False:
            print 'shot missed!'
            
    def enemy_turn(self, ocean, ocean_2):     # this handles computer actions

        attack_coord = (random.randint(0,9),random.randint(0,9))

        if ocean.Chk_tile(attack_coord) == True:
            key = ocean.ship_at_Location(attack_coord)
            ocean.shipsDict[key].adjustHealth(attack_coord)
            print 'our ship is hit!'
            

        elif ocean.Chk_tile(attack_coord) == False:
            print 'they missed!'

    def moves(self):

        turns = 0

        if turns == 0 or turns % 2 == 0: # player plays first 
            self.player_turn(ocean, ocean_2)                # player_turn() includes attack mechanism
            turns += 1
            
        else:                            # computer plays next
            self.enemy_turn(ocean, ocean_2)
            turns += 1
            

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

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main_loop()

#endgame-----------------------------------------------------------------------        
    def victory(self, ocean, ocean_2):  # sets victory and defeat conditions

        if ocean_2.Remains()== 0:    # if enemy ships remain = 0
            self.end_screen(self.vic) #print victory screen

        elif ocean.Remains() == 0: # if player ships remain = 0
            self.end_screen(self.defeat)  #print defeat screen

#extra features-----------------------------------------------------------------
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
ocean = Ocean()
ocean_2 = Player_Ocean()
game = Game(ocean, ocean_2)
main_loop(screen, ocean, ocean_2, ocean.Ships, game, ending)
        
    

        

        
