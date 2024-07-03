import json
#import curses
import keyboard
import sys
import os
sys.path.append(os.getcwd())

from solution.game import Game
from solution.maze import Maze, Octaedro, Protegido, Room, Door, Treasury, Wall, Bomb, Rectangle, Hexagon, North, East, South, West, Northeast, Southeast, Southwest, Northwest,Open,Close,Enter
from solution.creatures import Archer, Beast,Aggressive, Boss, Delicioso, Depredador,Lazy, Person, Warrior, Wizard
import time

class Director:
    def __init__(self):
        self.dict=None
        self.builder=None

    def procesar(self,filename):
        self.leer_archivo(filename)
        self.iniBuilder()
        self.crear_laberinto()
        self.crear_game()
        self.crear_beasts()
        self.crear_person()
        self.crear_bosses()

    def leer_archivo(self, filename):
        try:
            with open(filename) as f:
                data = json.load(f)
                self.dict= data
        except FileNotFoundError:
            print(f"File {filename} does not exist")
            return None
    
    def iniBuilder(self):
        if (self.dict['form'] == 'rectangle'):
            self.builder=LaberintoBuilder()
        elif (self.dict['form'] == 'hexagon'):
            self.builder=LaberintoHexagonalBuilder()
        elif (self.dict['form'] == 'octaedro'):
            self.builder=LaberintoOctaedralBuilder()
        else:
            print("Form not found")
            return None

    def getGame(self):
        return self.builder.getGame()

    def crear_game(self):
        self.builder.makeGame()

    def crear_laberinto(self):
        self.builder.makeMaze()
        
        for each in self.dict['maze']:
            self.crear_laberinto_recursivo(each, 'root')
            
        for each in self.dict['doors']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.makeDoor(n1, or1, n2, or2)
    
    def crear_laberinto_recursivo(self, un_dic, padre):
    
        if un_dic['tipo'] == 'room':
            cont = self.builder.makeRoom(un_dic['num'])
        
        if un_dic['tipo'] == 'treasury':
            cont = self.builder.makeTreasury(un_dic['num'])
            
        if un_dic['tipo'] == 'bomb':
            self.builder.makeBombIn(padre)
            
        if 'hijos' in un_dic:
            for each in un_dic['hijos']:
                self.crear_laberinto_recursivo(each, cont)

    def crear_beasts(self):
        for each in self.dict['beasts']:
            modo = each['modo']
            if modo == 'Aggressive':
                self.builder.makeAggressiveBeastPosition(each['posicion'])
            elif modo == 'Lazy':
                self.builder.makeLazyBeastPosition(each['posicion'])
            elif modo == 'Delicioso':
                self.builder.makeDeliciosoBeastPosition(each['posicion'])
            elif modo == 'Depredador':
                self.builder.makeDepredadorBeastPosition(each['posicion'])
    
    def crear_person(self):
        pers = self.dict['person']
        if pers['type'] == 'Warrior':
            self.builder.addWarriorPersonToGame(pers['name'])
        elif pers['type'] == 'Archer':
            self.builder.addArcherPersonToGame(pers['name'])
        elif pers['type'] == 'Wizard':
            self.builder.addWizardPersonToGame(pers['name'])

    def crear_bosses(self):
        for each in self.dict['bosses']:
            self.builder.makeBossPosition(each['posicion'])

class LaberintoBuilder:
    def __init__(self):
        self.game = None
        self.maze = None
    
    def getGame(self):
        return self.game
    
    def makeGame(self):
        self.game = Game()
        self.game.prototype =self.maze
        self.game.maze = self.game.cloneMaze()

    def makeForm(self, num):
        return Rectangle(num)
     
    def makeMaze(self):
        self.maze= Maze()
    
    def makeWall(self):
        return Wall()
    
    def makeDoor(self,cont1, cont2):
        door=Door(cont1, cont2)
        return door

    def makeBombIn(self, cont):
        bomb=Bomb()
        cont.addChild(bomb)
        return bomb

    def makeRoom(self, num):
        room=Room(num)
        room.form=self.makeForm(num)
        for each in room.getOrientations():
            each.setEMinOr(self.makeWall(), room.form)
        self.maze.addRoom(room)
        return room

    def makeTreasury(self, num):
        treasury=Treasury(num)
        treasury.form=self.makeForm(num)
        for each in treasury.getOrientations():
            each.setEMinOr(self.makeWall(), treasury.form)
        self.maze.addTreasury(treasury)
        return treasury

    def makeNorth(self):
        return North().get_instance()

    def makeEast(self):
        return East.get_instance()
    
    def makeSouth(self):
        return South().get_instance()
    
    def makeWest(self):
        return West().get_instance()
    
    def makeDoor(self, un_num, una_or_string, otro_num, otra_or_string):
        lado1 = self.maze.getCont(un_num)
        lado2 = self.maze.getCont(otro_num)
        
        or1 = getattr(self, 'make'+una_or_string)()
        or2 = getattr(self, 'make'+otra_or_string)()
        
        pt = Door(lado1, lado2)
        pt.addCommand(Open(pt))
        lado1.setEMinOr(pt,or1) 
        lado2.setEMinOr(pt,or2)


    def makeWarriorPerson(self, name):
        return Person(name, Warrior())
    def makeArcherPerson(self, name):
        return Person(name, Archer())
    def makeWizardPerson(self, name):
        return Person(name, Wizard())
    
    def addWarriorPersonToGame(self, name):
        pers = self.makeWarriorPerson(name)
        self.game.addPerson(pers)
    def addArcherPersonToGame(self, name):
        pers = self.makeArcherPerson(name)
        self.game.addPerson(pers)
    def addWizardPersonToGame(self, name):
        pers = self.makeWizardPerson(name)
        self.game.addPerson(pers)

    def makeAggressiveBeast(self):
        return Beast(Aggressive(), 3, 10)
    def makeLazyBeast(self):
        return Beast(Lazy(), 1, 15)
    def makeDeliciosoBeast(self):
        return Beast(Delicioso(), 2, 6)
    def makeDepredadorBeast(self):
        return Beast(Depredador(), 9, 2)

    def makeAggressiveBeastPosition(self, num):
        cont=self.game.getCont(num)
        beast=self.makeAggressiveBeast()
        beast.position=cont
        self.game.addBeast(beast)

    def makeLazyBeastPosition(self, num):
        cont=self.game.getCont(num)
        beast=self.makeLazyBeast()
        beast.position=cont
        self.game.addBeast(beast)

    def makeDeliciosoBeastPosition(self, num):
        cont=self.game.getCont(num)
        beast=self.makeDeliciosoBeast()
        beast.position=cont
        self.game.addBeast(beast)

    def makeDepredadorBeastPosition(self, num):
        cont=self.game.getCont(num)
        beast=self.makeDepredadorBeast()
        beast.position=cont
        self.game.addBeast(beast)

    def makeBoss(self):
        return Boss()
    
    def makeBossPosition(self, num):
        cont=self.game.getCont(num)
        if type(cont) is Treasury:
            cont.change_state(Protegido(cont))
        boss = self.makeBoss()
        boss.position=cont
        self.game.addBoss(boss)

class LaberintoHexagonalBuilder(LaberintoBuilder):
    def makeForm(self, num):
        return Hexagon(num)
    
    def makeRoom(self, num):
        room=Room(num)
        room.form=self.makeForm(num)
        for each in room.getOrientations():
            each.setEMinOr(self.makeWall(), room.form)
        self.maze.addRoom(room)
        return room
    
    def makeTreasury(self,num):
        treasury=Treasury(num)
        treasury.form=self.makeForm(num)
        for each in treasury.getOrientations():
            each.setEMinOr(self.makeWall(), treasury.form)
        self.maze.addTreasury(treasury)
        return treasury
    
    def makeNortheast(self):
        return Northeast().get_instance()

    def makeNorthwest(self):
        return Northwest.get_instance()
    
    def makeSoutheast(self):
        return Southeast().get_instance()
    
    def makeSouthwest(self):
        return Southwest().get_instance()

class LaberintoOctaedralBuilder(LaberintoBuilder):
    def makeForm(self, num):
        return Octaedro()
    
    def makeNortheast(self):
        return Northeast().get_instance()

    def makeNorthwest(self):
        return Northwest.get_instance()
    
    def makeSoutheast(self):
        return Southeast().get_instance()
    
    def makeSouthwest(self):
        return Southwest().get_instance()
    
def main(): #stdscr
    
    director=Director()
    director.procesar(os.getcwd()+'\\json\\maze2room2beasts.json')
    game=director.getGame()
    game.addPerson("Pepe")
    person=game.person
    game.openDoors()
    game.launchThreds()
    
    while True:
        if keyboard.is_pressed('q'):
            break  # Exit the program
        elif keyboard.is_pressed("w"): #curses.KEY_UP:
            person.goNorth()
        elif keyboard.is_pressed("s"): #curses.KEY_DOWN:
            person.goSouth()
        elif keyboard.is_pressed("a"): #curses.KEY_LEFT:
            person.goWest()
        elif keyboard.is_pressed("d"): #curses.KEY_RIGHT:
            person.goEast()
        elif keyboard.is_pressed("e"):#curses.KEY_ENTER or key in [10, 13]:
            person.attack()
        elif keyboard.is_pressed("x"):
            game.openDoors()
        elif keyboard.is_pressed("c"):
            game.closeDoors()
    game.stopThreds()
#main()


