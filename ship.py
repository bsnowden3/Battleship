'''
Created on Jan 18, 2015

@author: Kevin
'''

from json.decoder import WHITESPACE
from Tix import COLUMN
import pygame, sys

WIDTH = 50
HEIGHT = 50
class Ship(object):
    
    def __init__(self, x, y, orientation):
        self.col = x
        self.row = y
        self.health = self.health
        self.orientation = orientation #Orientation of ship (Vertical or Hypothesiss)
        self.status = {}
        for i in range(self.health):#sets up the squares for after the attack
            if self.orientation == 1:#1 = vertical
                self.status[i+1] = [self.col,self.row+i,True]#[Column, Row+1, Alive
            elif self.orientation == 0:#0 = horizontal
                self.status[i+1] = [self.col+i,self.row,True]
            else:
                self.status[0] = [self.col,self.row,True]
    def displayStatus(self):#display the current status of the ship
        return self.status
    def adjustHealth(self,coordinate):
        self.health -= 1
        for i in self.status:
            if self.status[i][0]==coordinate[0]:
                if self.status[i][1]==coordinate[1]:
                    self.status[i][2] = False
                    
                else:
                    pass
            else:
                pass
        pass
    def getHealth(self):
        return self.health
    def getLocation(self):
        location = []
        for i in self.status:
            location.append((self.status[i][0],self.status[i][1]))
        return location
class Aircraft_Carrier(pygame.sprite.Sprite,Ship):
    health = 5#health of current type of ship
    def __init__(self,x,y,orientation):
        self.orientation = orientation
        Ship.__init__(self, x,y,orientation)
        pygame.sprite.Sprite.__init__(self)
        self.setPic()
        self.rect = self.image.get_rect()
        self.rect.y = get_row(y, HEIGHT)
        self.rect.x = get_col(x, WIDTH)
    def setPic(self):
        if self.orientation == 1:
            self.image = pygame.image.load("Aircraft_CarrierV.png").convert_alpha()
        else:
            self.image = pygame.image.load("Aircraft_Carrier.png").convert_alpha()
    def getRect(self):
        return self.rect
class Battleship(pygame.sprite.Sprite,Ship):
    health = 4
    def __init__(self,x,y,orientation):
        self.orientation = orientation
        Ship.__init__(self, x,y,orientation)
        pygame.sprite.Sprite.__init__(self)
        self.setPic()
        self.rect = self.image.get_rect()
        self.rect.y = get_row(y, HEIGHT)
        self.rect.x = get_col(x, WIDTH)
    def setPic(self):
        if self.orientation == 1:
            self.image = pygame.image.load("BattleshipV.png").convert_alpha()
        else:
            self.image = pygame.image.load("Battleship.png").convert_alpha()
    def getRect(self):
        return self.rect
class Submarine(pygame.sprite.Sprite,Ship):
    health = 3
    def __init__(self,x,y,orientation):
        self.orientation = orientation
        Ship.__init__(self, x,y,orientation)
        pygame.sprite.Sprite.__init__(self)
        self.setPic()
        self.rect = self.image.get_rect()
        self.rect.y = get_row(y, HEIGHT)
        self.rect.x = get_col(x, WIDTH)
    def setPic(self):
        if self.orientation == 1:
            self.image = pygame.image.load("SubmarineV.png").convert_alpha()
        else:
            self.image = pygame.image.load("Submarine.png").convert_alpha()
    def getRect(self):
        return self.rect
class Destroyer(pygame.sprite.Sprite,Ship):
    health = 3
    def __init__(self,x,y,orientation):
        self.orientation = orientation
        Ship.__init__(self, x,y,orientation)
        pygame.sprite.Sprite.__init__(self)
        self.setPic()
        self.rect = self.image.get_rect()
        self.rect.y = get_row(y, HEIGHT)
        self.rect.x = get_col(x, WIDTH)
    def setPic(self):
        if self.orientation == 1:
            self.image = pygame.image.load("DestroyerV.png").convert_alpha()
        else:
            self.image = pygame.image.load("Destroyer.png").convert_alpha()
    def getRect(self):
        return self.rect
    
class Patrol_Boat(pygame.sprite.Sprite,Ship):
    health = 2
    def __init__(self,x,y,orientation):
        self.orientation = orientation
        Ship.__init__(self, x,y,orientation)
        pygame.sprite.Sprite.__init__(self)
        self.setPic()
        self.rect = self.image.get_rect()
        self.rect.y = get_row(y, HEIGHT)
        self.rect.x = get_col(x, WIDTH)
    def setPic(self):
        if self.orientation == 1:
            self.image = pygame.image.load("PatrolboatV.png").convert_alpha()
        else:
            self.image = pygame.image.load("Patrolboat.png").convert_alpha()
    def getRect(self):
        return self.rect
    
def get_row(row, height):
    return row*height+11

def get_col(col, width):
    return col*WIDTH+11
#############Test, not important###################
'''
def test():
    pygame.init()  # initialize all imported pygame modules
    window_size = [16 * WIDTH, 9 * HEIGHT]  # width, height
    screen = pygame.display.set_mode(window_size)
    ship = Aircraft_Carrier(0,0,"Vertical")
    ship.adjustHealth((0, 1))
    print ship.getLocation()
    theShip = pygame.sprite.RenderPlain()
    theShip.add(ship)
    theShip.rect = ship.rect
    theShip.draw(screen)
    pygame.display.flip()

test()    
'''
