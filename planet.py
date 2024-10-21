from random import randint
from items import SparePart, ShipPiece, Portal

class Planet:

    def __init__(self, size=15, starting=False):
        # TODO Part 1
        # Make the following instance fields
        # 1) The map is a size x size 2D Python list
        self.map = list()
        for row in range(size):
                self.map.append([None] * size)

        # If its the starting planet
        # Setup the starting map (when starting is True)
        # It has spaceship components, spare parts, and wormholes
        if starting:
            self.map[7][5] = ShipPiece("engine_broken.ppm", "broken")
            self.map[7][6] = ShipPiece("cabin_broken.ppm", "broken")
            self.map[6][5] = ShipPiece("exhaust_broken.ppm", "broken")
            self.map[6][6] = ShipPiece("engine_broken.ppm", "broken")
            self.map[8][6] = ShipPiece("exhaust.ppm", "working")



        # If its not the starting planet
        # Setup a map for a planet that isn't the starting Planet
        # It has spare parts and wormholes
        for i in range(randint(2, 6)):  # number of wormholes random
            # find set of random coordinates where there is an empty spot on map
            coords = [randint(0, size - 1), randint(0, size - 1)]
            while self.map[coords[0]][coords[1]] != None:
                coords = [randint(0, size - 1), randint(0, size - 1)]

            # when this spot is found, assign a portal to it
            self.map[coords[0]][coords[1]] = Portal(self, [coords[0], coords[1]])

        # Examples of making all three items on a planet
        # x = SparePart("screw.ppm") 
        # y = ShipPiece("cabin.ppm", "working")
        # z = Portal()

        sparepart_imgs = ['gear.ppm', 'screw.ppm', 'cake.ppm', 'bagel.ppm']
        imgs_index = 0
        for i in range(randint(4, 8)):  # number of parts random
            # find set of random coordinates where there is an empty spot on map
            coords = [randint(0, size - 1), randint(0, size - 1)]
            while self.map[coords[0]][coords[1]] != None:
                coords = [randint(0, size - 1), randint(0, size - 1)]

            # when this spot is found, assign a part to it
            self.map[coords[0]][coords[1]] = SparePart(sparepart_imgs[imgs_index])

            imgs_index += 1
            if imgs_index == len(sparepart_imgs):
                imgs_index = 0

    def getEmptyLocation(self):
        """
        Finds the first empty spot found when traversing the map
        """
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == None:
                    return [row, col]
        return -1  # no empty locations found
    
    def findPortal(self):
        """
        Finds the first portal when traversing the map
        """
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if isinstance(self.map[row][col], Portal):
                    return self.map[row][col]
        return -1  # no portals found


if __name__ == "__main__":
    planet = Planet(starting=True)
    for row in planet.map:
        print(row)
