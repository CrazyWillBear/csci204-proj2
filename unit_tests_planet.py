import unittest
from planet import Planet
from items import SparePart, ShipPiece, Portal

class TestPlanet(unittest.TestCase):
    def testInstanceFields(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True) 
        # Test the type of each instance field
        self.assertTrue(False)
    
    def testShipPieces(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of ship components to make sure there are enough
        # and they have the correct variety (broken, etc)
        self.assertTrue(False)
        
    def testSpareParts(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of spare parts to make sure there are enough
        # Also test that multiple sorts of spare parts are represented

        # Make second, third, and fourth starting Planets
        # Get the number of spare parts of each
        # Test that they do not all have the same number of spare parts.
        self.assertTrue(False)
        
    def testPortals(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of portals to make sure there are enough
        
        # Make second, third, and fourth starting Planets
        # Get the number of portals of each
        # Test that they do not all have the same number of portals.
        self.assertTrue(False)
    
if __name__ == '__main__':
    unittest.main()
