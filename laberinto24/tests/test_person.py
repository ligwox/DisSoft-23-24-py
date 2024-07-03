import unittest
import sys
import os
sys.path.append(os.getcwd())
sys.path.append('D:\laberinto24\solution')
from creatures import Person, Warrior, Archer, Wizard
from solution.game import Game
from maze import Lleno, Protegido, Vacio, Treasury

class TestGame(unittest.TestCase):
    
    def test_makeWarriorPerson_returns_warrior_tipo(self):
        game = Game()
        person = game.makeWarriorPerson('Pepe')
        self.assertIsInstance(person, Person)
        self.assertIsInstance(person.type, Warrior)

    def test_makeArcherPerson_returns_archer_tipo(self):
        game = Game()
        person = game.makeArcherPerson('Pepe')
        self.assertIsInstance(person, Person)
        self.assertIsInstance(person.type, Archer)

    def test_makeWizardPerson_returns_wizard_tipo(self):
        game = Game()
        person = game.makeWizardPerson('Pepe')
        self.assertIsInstance(person, Person)
        self.assertIsInstance(person.type, Wizard)

    def test_warrior_ultimate(self):
        game = Game()
        person_basic_life = 20
        person_basic_power = 1
        expected_warrior_after_ultimate_life = 27
        expected_warrior_after_ultimate_power = 1
        person = game.makeWarriorPerson('Pepe')
        self.assertEqual(person.life, person_basic_life)
        self.assertEqual(person.power, person_basic_power)
        person.type.ultiamte(person)
        self.assertEqual(person.life, expected_warrior_after_ultimate_life)
        self.assertEqual(person.power, expected_warrior_after_ultimate_power)

    def test_archer_ultimate(self):
        game = Game()
        person_basic_life = 20
        person_basic_power = 1
        expected_archer_after_ultimate_life = 20
        expected_archer_after_ultimate_power = 3
        person = game.makeArcherPerson('Pepe')
        self.assertEqual(person.life, person_basic_life)
        self.assertEqual(person.power, person_basic_power)
        person.type.ultiamte(person)
        self.assertEqual(person.life, expected_archer_after_ultimate_life)
        self.assertEqual(person.power, expected_archer_after_ultimate_power)

    def test_wizard_ultimate(self):
        game = Game()
        person_basic_life = 20
        person_basic_power = 1
        expected_wizard_after_ultimate_life = 22
        expected_wizard_after_ultimate_power = 2
        person = game.makeWizardPerson('Pepe')
        self.assertEqual(person.life, person_basic_life)
        self.assertEqual(person.power, person_basic_power)
        person.type.ultiamte(person)
        self.assertEqual(person.life, expected_wizard_after_ultimate_life)
        self.assertEqual(person.power, expected_wizard_after_ultimate_power)

    def test_treasury_affects_person(self):
        game = Game()
        maze = game.createMaze2Tres()
        person_basic_life = 20
        person_basic_power = 1
        expected_life_after_collect_treasure = 20
        expected_power_after_collect_treasure = 3
        self.assertEqual(game.person.life, person_basic_life)
        self.assertEqual(game.person.power, person_basic_power)
        game.person.collect()
        self.assertEqual(game.person.life, expected_life_after_collect_treasure)
        self.assertEqual(game.person.power, expected_power_after_collect_treasure)
        
if __name__ == '__main__':
    unittest.main()