#Project 6.177
#Ocean class for Battleship Game
#Bernard Snowden (bsnowden@mit.edu)
#Partners: Mark Yang and Kevin Rodriquez

blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

HEIGHT = 50
WIDTH = 50

#from Ships import *

import pygame
from Squares import Square
from ship import *
import time
from random import randint

pygame.init()
screen_width = 1150
screen_height = 550
screen=pygame.display.set_mode([screen_width,screen_height])
screen.fill(blue)

class Ocean():
    def __init__(self):

        self.screen_width = 1150
        self.screen_height = 550
        self.ocean_tile_width = 50
        self.ocean_tile_height = 50
        self.size = 10
        self.totalShips = 5
        self.shipsRemain = 5
        self.squares = pygame.sprite.RenderPlain()
        self.boardSquares = [[0 for x in range(self.size)] for x in range(self.size)] # creates the grid data structure
        for i in range(self.size):
            for j in range(self.size):
                s = Square(i, j, blue) # creates a blue square for a specific index in grid
                self.boardSquares[i][j] = s # adds square to our data structure for easy access
        self.squares.add(s)
        self.shipsDict = {}
        #self.screen_size()

        #initialization of Ships
        # Im assume Kevin will have different ship classes that inherit from Ship
        self.createShips()
        
                      
        self.Ships = pygame.sprite.RenderPlain()
        for i in self.shipsDict:
            self.Ships.add(self.shipsDict[i])
        
    
    def draw_grid(self, screen):
        for counter in range(self.size+1):
            pygame.draw.line(screen,white,(10, 10+(counter*self.ocean_tile_height)),(510,10+(counter*self.ocean_tile_height)),5)

            pygame.draw.line(screen,white,(10+(counter*self.ocean_tile_width), 10),(10+(counter*self.ocean_tile_width),510),5)
 #creates ships objects           
    def createShips(self):

        coordinate = self.generateLocation(5)
        self.aircraft_Carrier = Aircraft_Carrier(coordinate[0],coordinate[1],coordinate[2])#initializes Aircraft_Carrier
        allShipsLocations = []
        allShipsLocations.append(self.aircraft_Carrier.getLocation())#add Air_craft carriers locations
 
        coordinate = self.checkCoord(allShipsLocations,4)        
        self.battleShip = Battleship(coordinate[0],coordinate[1],coordinate[2])
        allShipsLocations.append(self.battleShip.getLocation())
        

        coordinate = self.checkCoord(allShipsLocations, 3)
        self.destroyer = Destroyer(coordinate[0], coordinate[1],coordinate[2])
        allShipsLocations.append(self.destroyer.getLocation())
        

        coordinate = self.checkCoord(allShipsLocations, 3)
        self.submarine = Submarine(coordinate[0], coordinate[1],coordinate[2])
        allShipsLocations.append(self.submarine.getLocation())
        

        coordinate = self.checkCoord(allShipsLocations, 2)
        self.patrolBoat = Patrol_Boat(coordinate[0], coordinate[1],coordinate[2])
        allShipsLocations.append(self.patrolBoat.getLocation())
        


        self.shipsDict = {"Aircraft Carrier":self.aircraft_Carrier, "Battleship": self.battleShip, "Destroyer": self.destroyer, "Submarine":self.submarine, "Patrol Boat": self.patrolBoat}
        pass
    
    def checkCoord(self, allShipsLocations,size):
        check = False
        counter = 0
        goofed = 0
        while check == False:
            counter = 0
            coordinate = self.generateLocation(size)
            for ships in allShipsLocations:
                for loc in ships:
                    for i in range(size):
                        if coordinate[2]==0:
                            if (coordinate[0]+i,coordinate[1]) == loc:
                                counter += 1
                        elif coordinate[2]==1:
                            if (coordinate[0],coordinate[1]+i)== loc:
                                counter += 1
            if counter == 0:
                check = True
        return coordinate

    
    def generateLocation(self,size):
        orientation = randint(0,1)
        if(orientation == 0):
            x = randint(0,10-size)
            y = randint(0,9)
        else:
            y = randint(0,10-size)
            x = randint(0,9)
        return (x,y,orientation)
            

### Checks if ship is in location
    def Chk_tile(self, (ships_X,ships_Y)):
        
        for key in self.shipsDict:
            list_locations = self.shipsDict[key].getLocation()
            counter = 0
            for locTuple in list_locations:
                counter += 1
                if locTuple == (ships_X, ships_Y):
                    if (self.shipsDict[key].status[counter][2]== True): 
                        return True
                    else:
                        return False
        return False ### Returns false if there is ship is not location
    


###returns name of the ship in loc x,y
    def ship_at_Location(self, (ships_X,ships_Y)):

        for key in self.shipsDict:
            list_locations = self.shipsDict[key].getLocation()
            for locTuple in list_locations:
                if locTuple == (ships_X, ships_Y):
                    return key 


###
    def Remains(self):
        self.shipsRemain = self.totalShips
        for key in self.shipsDict:
            if(self.shipsDict[key].getHealth() == 0):
                self.shipsRemain -= 1

        return self.shipsRemain

    def drawShip(ship):
        pass
        
        



class Player_Ocean(Ocean):

    def __init__(self):
        Ocean.__init__(self)

    def draw_grid(self, screen):
        for counter in range(self.size+1):
            pygame.draw.line(screen,white,(560, 10+(counter*self.ocean_tile_height)),(1060,10+(counter*self.ocean_tile_height)),5)
            pygame.draw.line(screen,white,(560+(counter*self.ocean_tile_width), 10),((560+counter*self.ocean_tile_width),510),5)

    def generateLocation(self,size):
        orientation = randint(0,1)
        if(orientation == 0):
            x = randint(11,21-size)
            y = randint(0,9)
        else:
            y = randint(0,10-size)
            x = randint(11,20)
        return (x,y,orientation)
            
            

        

class Enemy_Ocean(Ocean):

    def __init__(self):
        Ocean.__init__(self)

"""    
ocean = Ocean()
ocean_2 = Player_Ocean()
ocean.draw_grid(screen)
ocean_2.draw_grid(screen)
#ocean.squares.draw(screen)

#ocean.Ships.rect = ocean.battleShip.getRect()
ocean.Ships.draw(screen)
ocean_2.Ships.draw(screen)
pygame.display.flip() # update screen
if ocean.Chk_tile((0,0))== True:
    ocean.shipsDict[ocean.ship_at_Location((0,0))].adjustHealth((0,0))
    print "Dead"
else:
    print "Escaped"
if ocean.Chk_tile((1,0))== True:
    ocean.shipsDict[ocean.ship_at_Location((1,0))].adjustHealth((1,0))
    print "Dead"
else:
    print "Escaped"


time.sleep(5)
"""
