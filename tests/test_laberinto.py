import unittest
import os
import time
import sys
from pathlib import Path
project_dir = Path(__file__).parent.parent
sys.path.append(str(project_dir))
sys.path.append('D:\laberinto24\solution')
from solution.game import Game

class TestGame(unittest.TestCase):
    
    def test_createRoom_returns_room_with_walls(self):
        game = Game()
        room = game.makeRoom(1)
        self.assertIsNotNone(room.north)
        self.assertIsNotNone(room.south)
        self.assertIsNotNone(room.east)
        self.assertIsNotNone(room.west)

    def test_createRoom_returns_room_with_correct_id(self):
        game = Game()
        room = game.makeRoom(5)
        self.assertEqual(room.num, 5)
        
    def test_createRoom_returns_different_rooms(self):
        game = Game()
        room1 = game.makeRoom(1)
        room2 = game.makeRoom(2)
        self.assertNotEqual(room1, room2)


if __name__ == '__main__':
    unittest.main()