import unittest
import sys
import os
sys.path.append(os.getcwd())
sys.path.append('D:\laberinto24\solution')
from solution.game import Game
from maze import Lleno, Protegido, Vacio, Treasury

class TestGame(unittest.TestCase):
    
    def test_makeTreasury_returns_treasury_with_walls(self):
        game = Game()
        treasury = game.makeTreasury(1)
        self.assertIsNotNone(treasury.north)
        self.assertIsNotNone(treasury.south)
        self.assertIsNotNone(treasury.east)
        self.assertIsNotNone(treasury.west)

    def test_makeTreasury_returns_treasury_with_correct_id(self):
        game = Game()
        treasury = game.makeTreasury(5)
        self.assertEqual(treasury.num, 5)
        
    def test_makeTreasury_returns_different_treasuries(self):
        game = Game()
        treasury1 = game.makeTreasury(1)
        treasury2 = game.makeTreasury(2)
        self.assertNotEqual(treasury1, treasury2)
    
    def test_makeTreasury_returns_treasury_with_lleno_state(self):
        game = Game()
        treasury = game.makeTreasury(1)
        self.assertIsInstance(treasury, Treasury)
        self.assertIsInstance(treasury.state, Lleno)

    def test_changeState_changes_treasury_state(self):
        game = Game()
        treasury = game.makeTreasury(1)
        treasury.change_state(Vacio(treasury))
        self.assertIsInstance(treasury.state, Vacio)
    
    def test_makeBoss_changes_treasury_state_for_protegido(self):
        game = Game()
        treasury = game.makeTreasury(1)
        boss = game.makeBoss(treasury)
        self.assertIsInstance(treasury.state, Protegido)

        
if __name__ == '__main__':
    unittest.main()