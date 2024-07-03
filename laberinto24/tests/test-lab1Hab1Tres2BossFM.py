import unittest
import sys
import os

sys.path.append(os.getcwd())
sys.path.append('D:\laberinto24\solution')
from creatures import Delicioso, Boss, Beast
from maze import Maze, Room, Door, Treasury, Wall
from game import Game

class TestGame(unittest.TestCase):
    
    def test_create1Tres1Hab1Beast1BossFM(self):
        game = Game()
        maze = game.create1Tres1Hab1Beast1BossFM()
        
        self.assertIsInstance(maze, Maze)
        cont = maze.children
        self.assertEqual(len(cont), 2)
        room1, tres2 = cont
        
        self.assertIsInstance(room1, Room)
        self.assertIsInstance(tres2, Treasury)

        # Verificar paredes y puertas
        self.assertIsNotNone(room1.north) 
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room1.east)
        self.assertIsNotNone(room1.west)
        
        self.assertIsNotNone(tres2.north)
        self.assertIsNotNone(tres2.south)
        self.assertIsNotNone(tres2.east)
        self.assertIsNotNone(tres2.west)  
        
        #Verify that walls and doors on their places
        self.assertIsInstance(room1.north, Wall)
        self.assertIsInstance(room1.south, Door)
        self.assertIsInstance(room1.west, Wall)
        self.assertIsInstance(room1.east, Wall)

        self.assertIsInstance(tres2.north, Door)
        self.assertIsInstance(tres2.south, Wall)
        self.assertIsInstance(tres2.west, Wall)
        self.assertIsInstance(tres2.east, Wall)

        #Verify that doors are between correct rooms
        self.assertIs(room1.south, tres2.north)

        # Check beast entities
        self.assertIsInstance(game.beasts[0], Beast)
        self.assertIsInstance(game.bosses[0], Boss)

        # Check beast modes
        self.assertIsInstance(game.beasts[0].mode, Delicioso)

        # Check beast positions
        self.assertIsInstance(game.beasts[0].position, Room)
        self.assertIsInstance(game.bosses[0].position, Treasury)


if __name__ == '__main__':
    unittest.main()