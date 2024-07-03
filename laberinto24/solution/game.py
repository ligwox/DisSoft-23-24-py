import os
from maze import Maze, Octaedro, Protegido, Room, Door, Treasury, Wall, BombedWall, Bomb, North, East, South, West, Northeast, Southeast, Southwest, Northwest, Rectangle
from creatures import Archer, Beast, Boss, Delicioso, Depredador, Mode, Aggressive, Lazy, Person, Warrior, Wizard
from threadManager import ThreadManager
import copy
import time





class Game:
    def __init__(self):
        self.maze = None
        self.beasts = []
        self.bosses = []
        self.person=None
        self.prototype = None
        self.threadManager = ThreadManager()

    def check_wincondition(self):
        if len(self.beasts) == 0 and len(self.bosses) == 0:
            print("All beasts and bosses are dead\n------GAME OVER------")
            self.stopThreds()
            exit()

    def getCont(self, id):
        return self.maze.getCont(id)
    
    def launchThreds(self):
        print("The beasts start to move...\nBosses are activated")
        for beast in self.beasts:
            self.threadManager.addBeastThread(beast)
        for boss in self.bosses:
            self.threadManager.addBossThread(boss)
        self.threadManager.start()

    def stopThreds(self):
        print("The beasts and bosses ared stopped...")
        #self.threadManager.stop()
        for beast in self.beasts:
            beast.life=0
        for boss in self.bosses:
            boss.life = 0
        #self.threadManager.join()

    def makeWall(self):
        return Wall()
    
    def makeDoor(self,room1, room2):
        door=Door(room1, room2)
        return door

    def makeRoom(self, id):
        room=Room(id)
        room.form=self.makeForm()
        room.addOrientation(self.makeNorth())
        room.addOrientation(self.makeEast())
        room.addOrientation(self.makeSouth())
        room.addOrientation(self.makeWest())
        room.north=self.makeWall()
        room.east=self.makeWall()
        room.south=self.makeWall()
        room.west=self.makeWall()
        return room
    
    def makeTreasury(self, id):
        treasury=Treasury(id)
        treasury.form=self.makeForm()
        treasury.addOrientation(self.makeNorth())
        treasury.addOrientation(self.makeEast())
        treasury.addOrientation(self.makeSouth())
        treasury.addOrientation(self.makeWest())
        treasury.north=self.makeWall()
        treasury.east=self.makeWall()
        treasury.south=self.makeWall()
        treasury.west=self.makeWall()
        return treasury

    def makeRoom(self, id):
        room=Room(id)
        room.form=self.makeFormOctaedro()
        room.addOrientation(self.makeNorth())
        room.addOrientation(self.makeNortheast())
        room.addOrientation(self.makeNorthwest())
        room.addOrientation(self.makeEast())
        room.addOrientation(self.makeWest())
        room.addOrientation(self.makeSouth())
        room.addOrientation(self.makeSoutheast())
        room.addOrientation(self.makeSouthwest())
        room.north=self.makeWall()
        room.east=self.makeWall()
        room.south=self.makeWall()
        room.west=self.makeWall()
        room.northeast=self.makeWall()
        room.northwest=self.makeWall()
        room.southeast=self.makeWall()
        room.southwest=self.makeWall()
        return room
    
    def makeTreasury(self, id):
        treasury=Treasury(id)
        treasury.form=self.makeFormOctaedro()
        treasury.addOrientation(self.makeNorth())
        treasury.addOrientation(self.makeNortheast())
        treasury.addOrientation(self.makeNorthwest())
        treasury.addOrientation(self.makeEast())
        treasury.addOrientation(self.makeWest())
        treasury.addOrientation(self.makeSouth())
        treasury.addOrientation(self.makeSoutheast())
        treasury.addOrientation(self.makeSouthwest())
        treasury.north=self.makeWall()
        treasury.east=self.makeWall()
        treasury.south=self.makeWall()
        treasury.west=self.makeWall()
        treasury.northeast=self.makeWall()
        treasury.northwest=self.makeWall()
        treasury.southeast=self.makeWall()
        treasury.southwest=self.makeWall()
        return treasury
    
    def makeForm(self):
        return Rectangle()
    
    def makeFormOctaedro(self):
        return Octaedro()

    def makeNorth(self):
        return North().get_instance()

    def makeEast(self):
        return East.get_instance()
    
    def makeSouth(self):
        return South().get_instance()
    
    def makeWest(self):
        return West().get_instance()
    
    def makeSoutheast(self):
        return Southeast().get_instance()

    def makeSouthwest(self):
        return Southwest().get_instance()

    def makeNortheast(self):
        return Northeast().get_instance()

    def makeNorthwest(self):
        return Northwest().get_instance()

    def create4Room1TresOcataedroLab(self):
        room1 = self.makeRoom(1)
        room2 = self.makeRoom(2)
        room3 = self.makeRoom(3)
        room4 = self.makeRoom(4)
        tres5 = self.makeTreasury(5)

        door12 = self.makeDoor(room1, room2)
        door13 = self.makeDoor(room1, room3)
        door14 = self.makeDoor(room1, room4)
        door15 = self.makeDoor(room1, tres5)
        
        room1.southeast = door12
        room2.northwest = door12
        
        room1.southwest = door13
        room3.northeast = door13
        
        room1.south = door14
        room4.north = door14
        
        room1.west = door15
        tres5.east = door15
        
        maze = Maze()
                
        maze.addRoom(room1)
        maze.addRoom(room2)
        maze.addRoom(room3)
        maze.addRoom(room4)
        maze.addTreasury(tres5)
        self.maze = maze

        return maze

    def createMaze2Room(self):
        maze = Maze()
        self.maze = maze
        room1 = Room(1)
        room2 = Room(2)

        door=Door(room1, room2)

        room1.south = door  
        room2.north = door

        self.maze.addRoom(room1)
        self.maze.addRoom(room2)

    def createMaze2Tres(self):
        tres1 = self.makeTreasury(1)
        tres2 = self.makeTreasury(2)

        door12 = self.makeDoor(tres1, tres2)
        
        tres1.south = door12
        tres2.north = door12

        person = self.makeWarriorPerson('Pepe')
        

        maze = Maze()
        
        maze.addTreasury(tres1)
        maze.addTreasury(tres2)
        self.maze = maze
        
        self.addPerson(person)

        return maze

    def create4Room4BeastFM(self):
        room1 = self.makeRoom(1)
        room2 = self.makeRoom(2)
        room3 = self.makeRoom(3)
        room4 = self.makeRoom(4)
        
        door12 = self.makeDoor(room1, room2)
        door13 = self.makeDoor(room1, room3)
        door24 = self.makeDoor(room2, room4)
        door34 = self.makeDoor(room3, room4)
        
        room1.south = door12
        room2.north = door12
        
        room1.east = door13
        room3.west = door13
        
        room2.east = door24
        room4.west = door24
        
        room3.south = door34
        room4.north = door34
        
        maze = Maze()
                
        maze.addRoom(room1)
        maze.addRoom(room2)
        maze.addRoom(room3)
        maze.addRoom(room4)
        self.maze = maze

        beast1 = self.makeAggressiveBeast(room1)
        beast2 = self.makeLazyBeast(room2)  
        beast3 = self.makeAggressiveBeast(room3)
        beast4 = self.makeLazyBeast(room4)
       
        self.addBeast(beast1)
        self.addBeast(beast2)
        self.addBeast(beast3)
        self.addBeast(beast4)

        return maze
    
    def create1Tres1Hab1Beast1BossFM(self):
        room1 = self.makeRoom(1)
        treasury2 = self.makeTreasury(2)

        door12 = self.makeDoor(room1, treasury2)

        room1.south = door12
        treasury2.north = door12

        maze = Maze()

        maze.addRoom(room1)
        maze.addTreasury(treasury2)
        self.maze = maze

        beast = self.makeDeliciosoBeast(room1)
        boss = self.makeBoss(treasury2)

        self.addBeast(beast)
        self.addBoss(boss)

        return maze

    def create2Room2Treasuries4DifferentBeastsFM(self):
        room1 = self.makeRoom(1)
        treasury2 = self.makeTreasury(2)
        room3 = self.makeRoom(3)
        treasury4 = self.makeTreasury(4)
        
        door12 = self.makeDoor(room1, treasury2)
        door13 = self.makeDoor(room1, room3)
        door24 = self.makeDoor(treasury2, treasury4)
        door34 = self.makeDoor(room3, treasury4)
        
        room1.south = door12
        treasury2.north = door12
        room1.east = door13
        room3.west = door13
        treasury2.east = door24
        treasury4.west = door24
        room3.south = door34
        treasury4.north = door34
        
        maze = Maze()
                
        maze.addRoom(room1)
        maze.addTreasury(treasury2)
        maze.addRoom(room3)
        maze.addTreasury(treasury4)
        self.maze = maze

        beast1 = self.makeAggressiveBeast(room1)
        beast2 = self.makeLazyBeast(treasury2)  
        beast3 = self.makeDeliciosoBeast(room3)
        beast4 = self.makeDepredadorBeast(treasury4)
       
        self.addBeast(beast1)
        self.addBeast(beast2)
        self.addBeast(beast3)
        self.addBeast(beast4)

        return maze

    def createMaze2RoomFM(self):
        room1 = self.makeRoom(1)
        room2 = self.makeRoom(2)
        door = self.makeDoor(room1, room2)
        maze = Maze()
        self.maze = maze
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
      
        room1.south = door 
        room2.north = door

        return maze
    
    def addPerson(self, pers):
        self.person = pers
        self.person.game=self
        self.maze.enter(self.person)

    def addBeast(self, beast):
        beast.num=len(self.beasts)+1
        beast.game=self
        self.beasts.append(beast)

    def addBoss(self, boss):
        boss.num=len(self.bosses)+1
        boss.game=self
        self.bosses.append(boss)

    def removeBeast(self, beast):
        self.beasts.remove(beast)

    def removeBoss(self, boss):
        self.bosses.remove(boss)

    def makeWarriorPerson(self, name):
        person = Person(name, Warrior())
        person.game=self
        return person
    
    def makeArcherPerson(self, name):
        person = Person(name, Archer())
        person.game=self
        return person
    
    def makeWizardPerson(self, name):
        person = Person(name, Wizard())
        person.game=self
        return person
    
    def makeAggressiveBeast(self,cont):
        beast= Beast(Aggressive(), 3, 10)
        beast.position=cont
        return beast
    
    def makeLazyBeast(self,cont):
        beast= Beast(Lazy(), 1, 15)
        beast.position=cont
        return beast
    
    def makeDeliciosoBeast(self,cont):
        beast= Beast(Delicioso(), 2, 6)
        beast.position=cont
        return beast
    
    def makeDepredadorBeast(self,cont):
        beast= Beast(Depredador(), 9, 2)
        beast.position=cont
        return beast
    
    def makeBoss(self,cont):
        boss = Boss()
        if type(cont) is Treasury:
            cont.change_state(Protegido(cont))
        boss.position=cont
        return boss
    
    def print(self):
        print("Game")
    
    def findPerson(self,unCont):
        if self.person.position ==unCont:
            return self.person
        else:
            return None
    
    def findEnemyCreature(self,unCont):
        for boss in self.bosses:
            if boss.position == unCont:
                return boss
        for beast in self.beasts:
            if beast.position == unCont:
                return beast
        else:
            return None
    
    def openDoors(self):
        print("Opening all doors...")
        abrirPuertas=lambda each: each.open()
        #eval('add(3,4)',{'__builtins__':None},dispatcher)
        self.maze.recorrer(abrirPuertas)

    def closeDoors(self):
        print("Closing all doors...")
        cerrarPuertas=lambda each: each.close()

        self.maze.recorrer(cerrarPuertas)
    
    def cloneMaze(self):
        return copy.deepcopy(self.prototype)
      

# BombedGame.py
class BombedGame(Game):
  def makeWall(self):
    return BombedWall()

  def print(self):
    print("BombedGame")
