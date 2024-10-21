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
        self.assertIsInstance(p.map, list)
        # no others for now since it's still part 1
    def testShipPieces(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of ship components to make sure there are enough
        # and they have the correct variety (broken, etc)
        item_types = []
        broken_items = 0
        ok_items = 0

        for row in p.map:
            for col in row:
                if isinstance(col, ShipPiece):
                    if col.getStatus() == "broken":
                        broken_items += 1
                    else:
                        ok_items += 1
                    
                    if col.getKind() not in item_types:
                        item_types.append(col.getImageName())

        self.assertTrue(broken_items >= 4)
        self.assertTrue(broken_items + ok_items >= 5)
        self.assertTrue(len(item_types) >= 3)
        
    def testSpareParts(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        # Test the number of spare parts to make sure there are enough
        # Also test that multiple sorts of spare parts are represented

        # Make second, third, and fourth starting Planets
        # Get the number of spare parts of each
        # Test that they do not all have the same number of spare parts.
        p1 = Planet(15, True)
        part_types = []

        parts1 = 0
        for row in p1.map:
            for col in row:
                if isinstance(col, SparePart):
                    parts1 += 1

                    if col.getImageName() not in part_types:
                        part_types.append(col.getImageName())
        
        # Make second, third, and fourth starting Planets
        p2 = Planet(15, True)
        parts2 = 0
        for row in p2.map:
            for col in row:
                if isinstance(col, SparePart):
                    parts2 += 1

                    if col.getImageName() not in part_types:
                        part_types.append(col.getImageName())

        p3 = Planet(15, True)
        parts3 = 0
        for row in p3.map:
            for col in row:
                if isinstance(col, SparePart):
                    parts3 += 1

                    if col.getImageName() not in part_types:
                        part_types.append(col.getImageName())

        p4 = Planet(15, True)
        parts4 = 0
        for row in p4.map:
            for col in row:
                if isinstance(col, SparePart):
                    parts4 += 1

                    if col.getImageName() not in part_types:
                        part_types.append(col.getImageName())

        self.assertTrue(len(part_types) >= 2)
        self.assertTrue(parts1 != parts2 != parts3 != parts4)
        
    def testPortals(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p1 = Planet(15, True)
        # Test the number of portals to make sure there are enough

        portals1 = 0
        for row in p1.map:
            for col in row:
                if isinstance(col, Portal):
                    portals1 += 1
        
        # Make second, third, and fourth starting Planets
        p2 = Planet(15, True)
        portals2 = 0
        for row in p2.map:
            for col in row:
                if isinstance(col, Portal):
                    portals2 += 1

        p3 = Planet(15, True)
        portals3 = 0
        for row in p3.map:
            for col in row:
                if isinstance(col, Portal):
                    portals3 += 1

        p4 = Planet(15, True)
        portals4 = 0
        for row in p4.map:
            for col in row:
                if isinstance(col, Portal):
                    portals4 += 1
        # Get the number of portals of each
        # Test that they do not all have the same number of portals.

        self.assertTrue(portals1 != portals2 != portals3 != portals4)
    
if __name__ == '__main__':
    unittest.main()
