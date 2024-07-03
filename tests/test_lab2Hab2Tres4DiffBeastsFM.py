import unittest
import sys
import os

sys.path.append(os.getcwd())
sys.path.append('D:\laberinto24\solution')
#from solution.maze import Maze, Room, Door
from creatures import Aggressive, Delicioso, Depredador, Lazy
from maze import Maze, Protegido, Room, Door, Treasury, Wall, BombedWall, Bomb, North, East, South, West, Northeast, Southeast, Southwest, Northwest, Rectangle
from game import Game


class TestMazeGame(unittest.TestCase):

    def test_create2Room2Treasuries4DifferentBeastsFM(self):
        game = Game()
        maze = game.create2Room2Treasuries4DifferentBeastsFM()
        
        self.assertIsInstance(maze, Maze)
        
        #4
        cont = maze.children
        self.assertEqual(len(cont), 4)
        
        room1, tres2, room3, tres4 = cont
        
        self.assertIsInstance(room1, Room)
        self.assertIsInstance(tres2, Treasury)
        self.assertIsInstance(room3, Room)
        self.assertIsInstance(tres4, Treasury)

        # Verificar paredes y puertas
        self.assertIsNotNone(room1.north) 
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room1.east)
        self.assertIsNotNone(room1.west)
        
        self.assertIsNotNone(tres2.north)
        self.assertIsNotNone(tres2.south)
        self.assertIsNotNone(tres2.east)
        self.assertIsNotNone(tres2.west)  

        self.assertIsNotNone(room3.north) 
        self.assertIsNotNone(room3.south)
        self.assertIsNotNone(room3.east)
        self.assertIsNotNone(room3.west)
        
        self.assertIsNotNone(tres4.north)
        self.assertIsNotNone(tres4.south)
        self.assertIsNotNone(tres4.east)
        self.assertIsNotNone(tres4.west)  
        
        #Verify that walls and doors on their places
        self.assertIsInstance(room1.north, Wall)
        self.assertIsInstance(room1.south, Door)
        self.assertIsInstance(room1.west, Wall)
        self.assertIsInstance(room1.east, Door)

        self.assertIsInstance(tres2.north, Door)
        self.assertIsInstance(tres2.south, Wall)
        self.assertIsInstance(tres2.west, Wall)
        self.assertIsInstance(tres2.east, Door)

        self.assertIsInstance(room3.north, Wall)
        self.assertIsInstance(room3.south, Door)
        self.assertIsInstance(room3.west, Door)
        self.assertIsInstance(room3.east, Wall)

        self.assertIsInstance(tres4.north, Door)
        self.assertIsInstance(tres4.south, Wall)
        self.assertIsInstance(tres4.west, Door)
        self.assertIsInstance(tres4.east, Wall)

        #Verify that doors are between correct rooms
        self.assertIs(room1.south, tres2.north)
        self.assertIs(room1.east, room3.west)
        self.assertIs(tres2.east, tres4.west)
        self.assertIs(room3.south, tres4.north)

        # Check beast modes
        self.assertIsInstance(game.beasts[0].mode, Aggressive)
        self.assertIsInstance(game.beasts[1].mode, Lazy)
        self.assertIsInstance(game.beasts[2].mode, Delicioso)
        self.assertIsInstance(game.beasts[3].mode, Depredador)

        # Check beast positions
        self.assertIsInstance(game.beasts[0].position, Room)
        self.assertIsInstance(game.beasts[1].position, Treasury)
        self.assertIsInstance(game.beasts[2].position, Room)
        self.assertIsInstance(game.beasts[3].position, Treasury)

if __name__ == '__main__':
    unittest.main()