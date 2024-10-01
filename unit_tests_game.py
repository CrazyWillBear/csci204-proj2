import unittest
from PortalSaga.Game import Game
from PortalSaga.Planet import Planet
from PortalSaga.Item import Item

class TestGame(unittest.TestCase):
    def testInit(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a Game (don't call start())
        # Test that the instance fields are the correct types
        g = Game()
        self.assertIsInstance(g.planet, Planet)
        self.assertTrue(False)

    def testGoUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # Make a Game
        # Set the rover location to a location of your choosing
        g.roverLocation = [4,8] # chose more carefully than this
        # (Don't set it where it will land on a portal. Remove the portal if needed)
        # Call the goUp() method of the game
        g.goUp() # The GUI normally calls goUp but you can too
        # Test the rover's new location to make sure it has indeed gone up.
        self.assertTrue(False)
        
    def testGoDown(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        self.assertTrue(False)
        
    def testGoLeft(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        self.assertTrue(False)
        
    def testGoRight(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        self.assertTrue(False)
        
    def testShowWayBack(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 2
        self.assertTrue(False)
        
    def testPickUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        self.assertTrue(False)
        
    def testPerformTask(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        self.assertTrue(False)
        
    # add more test functions for other methods you have added (except simple gettter and setters methods)
    
if __name__ == '__main__':
    unittest.main()
    
