""" Game to play 'Lost Rovers'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
"""
from GUI.graphics import Point
from items import SparePart, ShipPiece, Portal
from planet import Planet

class Game:
    SIZE = 15                 # 15x15 squares in the map

    def __init__(self):
        # TODO Part 1
        # Your game needs instance fields for:
        # 1) a Planet instance. This is the current planet you are on. 
        #      It begins as a starting planet.
        # 2) a rover location of row and column. This is where you are 
        #       on the map.  The rover starts in an empty location on the map.
        self.planet = Planet(starting=True)
        self.rover_loc = self.planet.getEmptyLocation()

        # TODO Part 2
        # Your game needs instance fields for:
        # 1) a Stack of Portals the rover has traveled through

        # TODO Part 3
        # Your game needs instance fields for:
        # 1) a List of items in your inventory
        # 2) a Queue of tasks to fix the broken ship pieces
        pass

    def getRoverImage(self):
        """ Called by GUI when screen updates.
            Returns image name (as a string) of the rover. 
		(Likely './Img/rover.ppm') """
        # Only edit this if you get your own rover image
        return './Img/rover.ppm'

    def getRoverLocation(self):
        """ Called by GUI when screen updates.
            Returns location (as a Point). """
        # TODO Part 1
        return Point(self.rover_loc[1], self.rover_loc[0]) # backwards of what you expect

    def getImage(self, point):
        """ Called by GUI when screen updates.
            Returns image name (as a string) or None for the 
		    spare part, ship component, or portal at the given 
		    point coordinates. (such as './Img/engine.ppm') """
        row = point.y # point is backwards of what you expect
        col = point.x

        obj = self.planet.map[row][col]
        
        return obj.getImageName() if obj != None else None

    def goUp(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        if self.rover_loc[0] != 0:
            self.rover_loc[0] -= 1

        # TODO Part 2

    def goDown(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        if self.rover_loc[0] != len(self.planet.map) - 1:
            self.rover_loc[0] += 1
        pass 

        # TODO Part 2
        # If the robot lands on a portal, teleport

    def goLeft(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        if self.rover_loc[1] != 0:
            self.rover_loc[1] -= 1
        pass 

        # TODO Part 2
        # If the robot lands on a portal, teleport

    def goRight(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        if self.rover_loc[1] != len(self.planet.map) - 1:
            self.rover_loc[1] += 1
        pass 

        # TODO Part 2
        # If the robot lands on a portal, teleport

    def showWayBack(self):
        """ Called by GUI when button clicked.
            Flash the portal leading towards home. """
        # TODO Part 2
        pass 

    def getInventory(self):
        """ Called by GUI when inventory updates.
            Returns entire inventory (as a string). 
		3 cake
		2 screws
		1 rug
	  """
        # TODO Part 3
        pass 

    def pickUp(self):
        """ Called by GUI when button clicked. 
		If rover is standing on a part (not a portal 
		or ship component), pick it up and add it
		to the inventory. """
        # TODO Part 3
        pass 

    def getCurrentTask(self):
        """ Called by GUI when task updates.
            Returns top task (as a string). 
		'Fix the engine using 2 cake, 3 rugs' or
		'You win!' 
 	  """
        # TODO Part 3
        pass 

    def performTask(self):
        """ Called by the GUI when button clicked.
            If necessary parts are in inventory, and rover
            is on the relevant broken ship piece, then fixes
            ship piece and removes parts from inventory. If
            we run out of tasks, we win. """
        # TODO Part 3
        pass 

    # Put other methods here as needed if nay.

