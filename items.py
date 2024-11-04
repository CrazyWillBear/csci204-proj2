""" Classes for items that appear in the map (except the rover).
    Each class has a getKind() method which returns what sort of 
    item it is as a String.
"""

class SparePart:
    def __init__(self, imageName):
        # Part 1
        self.img_name = "./Img/" + imageName

    def getImageName(self):
        # TODO Part 1
        return self.img_name

    def getKind(self):
        return "part"

    def getName(self):
        return self.img_name.split("/")[-1].replace(".ppm", "")


class ShipPiece:
    def __init__(self, imageName, status):
        # TODO Part 1
        # Make the following instance fields
        # 1) The image name
        # 2) Its status; is it broken or working?
        self.img_name = imageName
        self.status = status

    def getImageName(self):
        # TODO Part 1
        if self.status == 'broken':
            return "./Img/" + self.img_name.replace(".", "_broken.")

        return "./Img/" + self.img_name

    def getKind(self):
        return "ship"
    
    def getStatus(self):
        # TODO Part 1
        return self.status

    def setStatus(self, status):
        """ 'working' or 'broken' """
        self.status = status
    
    def getName(self):
        return self.img_name.split("/")[-1].replace(".ppm", "")


class Portal:
    def __init__(self, planet, loc, con_portal=None):
        # TODO Part 1
        # Make the following instance fields
        # 1) The current image name ("./Img/portal.ppm" or "./Img/portal_flashing.ppm")
        self.img_name = "./Img/portal.ppm"

        # TODO Part 2
        # Make the following instance fields
        # 1) The map that this portal is on
        # 2) The location [row, column] of this portal on this map
        # 3) The portal at the other end of the wormhole (None if it isn't known yet)
        self.planet = planet
        self.loc = loc
        self.con_portal = con_portal

    def getImageName(self):
        # TODO Part 1
        return self.img_name

    def getKind(self):
        return "portal"
