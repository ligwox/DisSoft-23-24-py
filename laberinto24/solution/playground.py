import os
import time
import sys
from pathlib import Path

import keyboard

project_dir = Path(__file__).parent.parent
sys.path.append(str(project_dir))
from builder.builder import Director
from solution.game import Game

if __name__ == "__main__":

    director=Director()
    director.procesar(os.getcwd() + '\\json\\maze2room2beasts.json')
    game=director.getGame()
    game.launchThreds()
    while True:
        if keyboard.is_pressed('q'):
            break
        elif keyboard.is_pressed("w"):
            game.person.goNorth()
            time.sleep(0.3)
        elif keyboard.is_pressed("s"):
            game.person.goSouth()
            time.sleep(0.3)
        elif keyboard.is_pressed("a"):
            game.person.goWest()
            time.sleep(0.3)
        elif keyboard.is_pressed("d"):
            game.person.goEast()
            time.sleep(0.3)
        elif keyboard.is_pressed("e"):
            game.person.attack()
            time.sleep(0.3)
        elif keyboard.is_pressed("f"):
            game.person.collect()
            time.sleep(0.3)
        elif keyboard.is_pressed("r"):
            game.person.type.ultiamte(game.person)
            time.sleep(0.3)
        elif keyboard.is_pressed("x"):
            game.openDoors()
            time.sleep(0.3)
        elif keyboard.is_pressed("c"):
            game.closeDoors()
            time.sleep(0.3)
    game.stopThreds()


    # OCTAEDRO
    # while True:
    #     if keyboard.is_pressed('q'):
    #         game.person.goNorthwest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("w"):
    #         game.person.goNorth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("e"):
    #         game.person.goNortheast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("a"):
    #         game.person.goWest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("d"):
    #         game.person.goEast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("z"):
    #         game.person.goSouthwest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("x"):
    #         game.person.goSouth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("c"):
    #         game.person.goSoutheast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("f"):
    #         game.person.collect()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("g"):
    #         game.person.attack()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("r"):
    #         game.person.type.ultiamte(game.person)
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("v"):
    #         game.openDoors()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("b"):
    #         game.closeDoors()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("n"):
    #         break

    # HEXAGON
    # while True:
    #     if keyboard.is_pressed('q'):
    #         game.person.goNorthwest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("w"):
    #         game.person.goNorth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("s"):
    #         game.person.goSouth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("a"):
    #         game.person.goSouthwest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("d"):
    #         game.person.goSoutheast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("e"):
    #         game.person.goNortheast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("f"):
    #         game.person.collect()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("g"):
    #         game.person.attack()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("r"):
    #         game.person.type.ultiamte(game.person)
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("x"):
    #         game.openDoors()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("c"):
    #         game.closeDoors()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("z"):
    #         break




    # RECTANGLE
    # while True:
    #     if keyboard.is_pressed('q'):
    #         break
    #     elif keyboard.is_pressed("w"):
    #         game.person.goNorth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("s"):
    #         game.person.goSouth()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("a"):
    #         game.person.goWest()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("d"):
    #         game.person.goEast()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("e"):
    #         game.person.attack()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("f"):
    #         game.person.collect()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("r"):
    #         game.person.type.ultiamte(game.person)
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("x"):
    #         game.openDoors()
    #         time.sleep(0.3)
    #     elif keyboard.is_pressed("c"):
    #         game.closeDoors()
    #         time.sleep(0.3)