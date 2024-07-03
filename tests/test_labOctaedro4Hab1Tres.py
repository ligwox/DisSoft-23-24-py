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

    def test_create4Room1TresOcataedroLab(self):
        game = Game()
        maze = game.create4Room1TresOcataedroLab()
        
        self.assertIsInstance(maze, Maze)
        
        #4
        cont = maze.children
        self.assertEqual(len(cont), 5)
        
        room1, room2, room3, room4, tres5 = cont
        
        self.assertIsInstance(room1, Room)
        self.assertIsInstance(room2, Room)
        self.assertIsInstance(room3, Room)
        self.assertIsInstance(room4, Room)
        self.assertIsInstance(tres5, Treasury)

        # Verificar paredes y puertas
        self.assertIsNotNone(room1.north) 
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room1.east)
        self.assertIsNotNone(room1.west)
        self.assertIsNotNone(room1.northeast) 
        self.assertIsNotNone(room1.northwest)
        self.assertIsNotNone(room1.southwest)
        self.assertIsNotNone(room1.southeast)
        
        self.assertIsNotNone(room2.north) 
        self.assertIsNotNone(room2.south)
        self.assertIsNotNone(room2.east)
        self.assertIsNotNone(room2.west)
        self.assertIsNotNone(room2.northeast) 
        self.assertIsNotNone(room2.northwest)
        self.assertIsNotNone(room2.southwest)
        self.assertIsNotNone(room2.southeast)

        self.assertIsNotNone(room3.north) 
        self.assertIsNotNone(room3.south)
        self.assertIsNotNone(room3.east)
        self.assertIsNotNone(room3.west)
        self.assertIsNotNone(room3.northeast) 
        self.assertIsNotNone(room3.northwest)
        self.assertIsNotNone(room3.southwest)
        self.assertIsNotNone(room3.southeast)
        
        self.assertIsNotNone(room4.north) 
        self.assertIsNotNone(room4.south)
        self.assertIsNotNone(room4.east)
        self.assertIsNotNone(room4.west)
        self.assertIsNotNone(room4.northeast) 
        self.assertIsNotNone(room4.northwest)
        self.assertIsNotNone(room4.southwest)
        self.assertIsNotNone(room4.southeast)

        self.assertIsNotNone(tres5.north) 
        self.assertIsNotNone(tres5.south)
        self.assertIsNotNone(tres5.east)
        self.assertIsNotNone(tres5.west)
        self.assertIsNotNone(tres5.northeast) 
        self.assertIsNotNone(tres5.northwest)
        self.assertIsNotNone(tres5.southwest)
        self.assertIsNotNone(tres5.southeast)
        
        #Verify that walls and doors on their places
        self.assertIsInstance(room1.north, Wall)
        self.assertIsInstance(room1.south, Door)
        self.assertIsInstance(room1.west, Door)
        self.assertIsInstance(room1.east, Wall)
        self.assertIsInstance(room1.northeast, Wall)
        self.assertIsInstance(room1.northwest, Wall)
        self.assertIsInstance(room1.southwest, Door)
        self.assertIsInstance(room1.southeast, Door)

        self.assertIsInstance(room2.north, Wall)
        self.assertIsInstance(room2.south, Wall)
        self.assertIsInstance(room2.west, Wall)
        self.assertIsInstance(room2.east, Wall)
        self.assertIsInstance(room2.northeast, Wall)
        self.assertIsInstance(room2.northwest, Door)
        self.assertIsInstance(room2.southwest, Wall)
        self.assertIsInstance(room2.southeast, Wall)

        self.assertIsInstance(room3.north, Wall)
        self.assertIsInstance(room3.south, Wall)
        self.assertIsInstance(room3.west, Wall)
        self.assertIsInstance(room3.east, Wall)
        self.assertIsInstance(room3.northeast, Door)
        self.assertIsInstance(room3.northwest, Wall)
        self.assertIsInstance(room3.southwest, Wall)
        self.assertIsInstance(room3.southeast, Wall)

        self.assertIsInstance(room4.north, Door)
        self.assertIsInstance(room4.south, Wall)
        self.assertIsInstance(room4.west, Wall)
        self.assertIsInstance(room4.east, Wall)
        self.assertIsInstance(room4.northeast, Wall)
        self.assertIsInstance(room4.northwest, Wall)
        self.assertIsInstance(room4.southwest, Wall)
        self.assertIsInstance(room4.southeast, Wall)

        self.assertIsInstance(tres5.north, Wall)
        self.assertIsInstance(tres5.south, Wall)
        self.assertIsInstance(tres5.west, Wall)
        self.assertIsInstance(tres5.east, Door)
        self.assertIsInstance(tres5.northeast, Wall)
        self.assertIsInstance(tres5.northwest, Wall)
        self.assertIsInstance(tres5.southwest, Wall)
        self.assertIsInstance(tres5.southeast, Wall)

        #Verify that doors are between correct rooms
        self.assertIs(room1.southeast, room2.northwest)
        self.assertIs(room1.southwest, room3.northeast)
        self.assertIs(room1.south, room4.north)
        self.assertIs(room1.west, tres5.east)


if __name__ == '__main__':
    unittest.main()