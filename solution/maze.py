# mapelement.py
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Command:
    def __init__(self, receptor):
        self.receptor = receptor
    
    def execute(self):
        pass
    def isEnter(self):
        return False

class Open(Command):
    def execute(self):
        self.receptor.removeCommand(self)
        self.receptor.addCommand(Close(self.receptor))
        self.receptor.addCommand(Enter(self.receptor))
        self.receptor.open()

class Close(Command):
    def execute(self):
        self.receptor.removeCommand(self)
        self.receptor.addCommand(Open(self.receptor))
        self.receptor.close()

class Enter(Command):
    def execute(self):
        self.receptor.enter()
    def isEnter(self):
        return True

class MapElement:
    def __init__(self):
        self.commands = []
    
    def enter(self,someone):
        pass

    def print(self):
        print("MapElement")
    
    def isRoom(self):
        return False
    
    def isTreasury(self):
        return False

    def isDoor(self):
        return False
    
    def recorrer(self,unBloque):
        pass
    def open(self):
        pass
    def close(self):
        pass
    def recorrer(self,unBloque):
        unBloque(self)
        
    def addCommand(self, command):
        self.commands.append(command)
    def removeCommand(self, command):
        self.commands.remove(command)
    def getCommands(self):
        return self.commands
    def accept(self,visitor):
        pass

class Container(MapElement):
    # Composite
    def __init__(self):
        super().__init__()
        self.children = []
        self.num = None    
        self.form = None    
    
    def getPoint(self):
        return self.form.getPoint()

    def setPoint(self, point):
        self.form.setPoint(point)
    def getExtent(self):
        return self.form.extent
    def setExtent(self, extent):
        self.form.extent=extent
    
    def addChild(self, component):
        self.children.append(component)

    def removeChild(self, component):
        self.children.remove(component)
    
    def print(self):
        print("Container")
    
    def walkRandom(self,someone):
        pass
    def addOrientation(self, orientation):
        #self.orientations.append(orientation)
        self.form.addOrientation(orientation)
    
    def removeOrientation(self, orientation):
        #self.orientations.remove(orientation)
        self.form.removeOrientation(orientation)
    
    def getOrientations(self):
        return self.form.orientations

    def walkRandom(self, someone):        
        orientation = self.form.getRandomOrientation()
        orientation.walkRandom(someone)
   
    def goNorth(self, someone):
        #self.north.enter(someone)
        self.form.goNorth(someone)
    def goEast(self, someone):
        #self.east.enter(someone)
        self.form.goEast(someone)
    def goSouth(self, someone):
        #self.south.enter(someone)
        self.form.goSouth(someone)
    def goWest(self, someone):
        #self.west.enter(someone)
        self.form.goWest(someone)
    def goNortheast(self, someone):
        self.form.goNortheast(someone)
    def goNorthwest(self, someone):
        self.form.goNorthwest(someone)
    def goSoutheast(self, someone):
        self.form.goSoutheast(someone)
    def goSouthwest(self, someone):
        self.form.goSouthwest(someone)


    def setEMinOr(self, em, orientation):
        #orientation.setEMinOr(em, self)
        self.form.setEMinOr(em, orientation)
    
    def recorrer(self, unBloque):
        unBloque(self)
        for child in self.children:
            child.recorrer(unBloque)
        self.form.recorrer(unBloque)
        #for orient in self.orientations:
        #    orient.recorrerEn(unBloque,self)
    def getCommands(self):
        lista=[]
        lista += self.commands
        for child in self.children:
            lista += child.getCommands()
        lista += self.form.getCommands()
        return lista	

    def calcularPosicion(self):
        self.form.calcularPosicion()  
    
class Maze(Container):
    def __init__(self):
        super().__init__()

    def addRoom(self, cont):
        self.addChild(cont)

    def addTreasury(self, cont):
        self.addChild(cont)

    def enter(self,someone):
        self.children[0].enter(someone)

    def print(self):
        print("Maze")   
    
    def getCont(self, num):
        for cont in self.children:
            if cont.num == num:
                return cont
        return None
    
    def recorrer(self, unBloque):
        unBloque(self)
        for child in self.children:
            child.recorrer(unBloque)        

    def getOrientations(self):
        pass
    def accept(self, visitor):
        for child in self.children:
            child.accept(visitor)   

class Room(Container):
    def __init__(self, num):
        super().__init__()
        self.num=num

    def enter(self,someone):
        print(str(someone) + " enter room" + str(self.num))
        someone.position=self
    
    def print(self):
        print("Room")

    def isRoom(self):
        return True
    def __str__(self):
        return "Room-" + str(self.num)    
    def accept(self, visitor):
        visitor.visitRoom(self)
    
class Treasury(Container):
    def __init__(self, num):
        super().__init__()
        self.num=num
        self.state = Lleno(self)

    def enter(self,someone):
        print(str(someone) + " enter treasury" + str(self.num))
        someone.position=self
    
    def change_state(self,state):
        self.state=state
    
    def print(self):
        print("Treasury")

    def isTreasury(self):
        return True
    def __str__(self):
        return "Treasury-" + str(self.num)    
    def accept(self, visitor):
        visitor.visitTreasury(self)

class TreasuryState():
    def __init__(self, tresury):
        self.treasury = tresury
    def collectTreasure(self,someone):
        pass

class Vacio(TreasuryState):
    def __init__(self, tresury):
        super().__init__(tresury)
    def collectTreasure(self,someone):
        print(self.treasury, ' is empty')

class Lleno(TreasuryState):
    def __init__(self, tresury):
        super().__init__(tresury)
    def collectTreasure(self,someone):
            someone.power += 2
            print(str(someone) + " looted ", self.treasury, " and gained 2 power\nCurrent power is", str(someone.power))
            self.treasury.change_state(Vacio(self.treasury))

class Protegido(TreasuryState):
    def __init__(self, tresury):
        super().__init__(tresury)
    def collectTreasure(self, someone):
        print(self.treasury, ' is protected by boss, kill him first')

class Leaf(MapElement):
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Leaf")

class Tunnel(Leaf):
    def __init__(self):
        super().__init__()
        self.maze = None
    def enter(self,someone):
        print(str(someone) + " enter Tunnel"+"\n")
        self.maze=someone.game.cloneMaze()
        self.maze.enter(someone)

class Decorator(Leaf):
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def print(self):
        print("Decorator")

class Bomb(Decorator):
    def __init__(self):
        super().__init__()
        self.active = False

    def print(self):
        print("Bomb")

    def enter(self, someone):
        print(someone + " walked into a bomb"+"\n")

class Wall(MapElement):
    def __init__(self):
        pass
    
    def print(self):
        print("Wall")

    def enter(self, someone):
        print(someone , " walked into a wall")

    def calcularPosicionDesde(self,aForm,aPoint):
        pass
# bombedwall.py

class BombedWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False
    
    def print(self):
        print("BombedWall")

# door.py

class Door(MapElement):
    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.opened = False
        self.visited = False
    
    def enter(self,someone):
        if (self.opened):
            if someone.position == self.side1:
                self.side2.enter(someone)
            else:
                self.side1.enter(someone)
        else:
            print("The door "+str(self)+" is locked")

    def __str__(self):
        return "Puerta-"+str(self.side1)+"-"+str(self.side2)
    
    def open(self):
        print("Opening the door between "+str(self.side1)+" and "+str(self.side2))
        self.opened = True
    
    def close(self):
        print("Closing the door between "+str(self.side1)+" and "+str(self.side2))
        self.opened = False

    def isDoor(self):
        return True
    def calcularPosicionDesde(self,aForm,aPoint):
        if self.visited:
            return  
        self.visited = True
        if aForm.num==self.side1.num:
            self.side2.setPoint(aPoint)
            self.side2.calcularPosicion()
        else:
            self.side1.setPoint(aPoint)
            self.side1.calcularPosicion()


class Orientation:
    def __init__(self):
        pass
    def walkRandom(self, someone):
        pass
    def setEMinOr(self, em, aContainer):
        pass
    def recorrerEn(self, unBloque, aContainer):
        pass
    def getCommands(self,aForm):
        pass
    def calcularPosicionDesde(self,aForm):
        pass

class North(Orientation):
    _instance = None
    def __init__(self):
        if not North._instance:
            super().__init__()
            North._instance = self
    def setEMinOr(self, em, aContainer):
        aContainer.north = em

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = North()
        return cls._instance

    def print(self):
        print("North")
    
    def walkRandom(self, someone):
        someone.goNorth()

    def recorrerEn(self, unBloque, aContainer):
        aContainer.north.recorrer(unBloque)
    
    def getCommands(self,aForm):
        return aForm.north.getCommands()
    def calcularPosicionDesde(self, aForm):
        unPunto=Point(aForm.point.x,aForm.point.y-1)
        aForm.north.calcularPosicionDesde(aForm,unPunto)

class South(Orientation):
    _instance = None
    def __init__(self):
        if not South._instance:
            super().__init__()  
            South._instance = self

    @staticmethod 
    def get_instance():
        if not South._instance:
            South()
        return South._instance
    
    def print(self):
        print("South")
    
    def walkRandom(self, someone):
        someone.goSouth()
    
    def setEMinOr(self, em, aContainer):
        aContainer.south = em
    
    def recorrerEn(self, unBloque, aContainer):
        aContainer.south.recorrer(unBloque)

    def getCommands(self,aForm):
        return aForm.south.getCommands()
    def calcularPosicionDesde(self, aForm):
        unPunto=Point(aForm.point.x,aForm.point.y+1)
        aForm.south.calcularPosicionDesde(aForm,unPunto)

class East(Orientation):
    _instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')
        # if not East._instance:
        #     super().__init__()
        #     East._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def walkRandom(self, someone):
        someone.goEast()
    
    def setEMinOr(self, em, aContainer):
        aContainer.east = em
    # @staticmethod
    # def get_instance():
    #     if not East._instance:
    #         East()
    #     return East._instance
    
    # def print(self):
    #     print("East")
    def recorrerEn(self, unBloque, aContainer):
        aContainer.east.recorrer(unBloque)
    def getCommands(self,aForm):
        return aForm.east.getCommands()
    def calcularPosicionDesde(self, aForm):
        unPunto=Point(aForm.point.x+1,aForm.point.y)
        aForm.east.calcularPosicionDesde(aForm,unPunto)

class West(Orientation):
    _instance = None
    def __init__(self):
        if not West._instance:
            super().__init__()
            West._instance = self

    @staticmethod
    def get_instance():
        if not West._instance:
            West()
        return West._instance
    
    def print(self):
        print("West")
    
    def walkRandom(self, someone):
        someone.goWest()

    def setEMinOr(self, em, aContainer):
        aContainer.west = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.west.recorrer(unBloque)

    def getCommands(self,aForm):
        return aForm.west.getCommands()
    def calcularPosicionDesde(self, aForm):
        unPunto=Point(aForm.point.x-1,aForm.point.y)
        aForm.west.calcularPosicionDesde(aForm,unPunto)

class Northeast(Orientation):
    _instance = None
    
    def __init__(self):
        if not Northeast._instance:
            super().__init__()
            Northeast._instance = self

    @staticmethod
    def get_instance():
        if not Northeast._instance:
            Northeast()
        return Northeast._instance

    def print(self):
        print("Northeast")

    def walkRandom(self, someone):
        someone.goNortheast()

    def setEMinOr(self, em, aContainer):
        aContainer.northeast = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.northeast.recorrer(unBloque)
        
class Northwest(Orientation):
    _instance = None
    
    def __init__(self):
        if not Northwest._instance:
            super().__init__()
            Northwest._instance = self

    @staticmethod
    def get_instance():
        if not Northwest._instance:
            Northwest()
        return Northwest._instance

    def print(self):
        print("Northwest")

    def walkRandom(self, someone):
        someone.goNorthwest()

    def setEMinOr(self, em, aContainer):
        aContainer.northwest = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.northwest.recorrer(unBloque)
        
class Southeast(Orientation):
    _instance = None
    
    def __init__(self):
        if not Southeast._instance:
            super().__init__()
            Southeast._instance = self

    @staticmethod
    def get_instance():
        if not Southeast._instance:
            Southeast()
        return Southeast._instance

    def print(self):
        print("Southeast")

    def walkRandom(self, someone):
        someone.goSoutheast()

    def setEMinOr(self, em, aContainer):
        aContainer.southeast = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.southeast.recorrer(unBloque)
        
class Southwest(Orientation):
    _instance = None
    
    def __init__(self):
        if not Southwest._instance:
            super().__init__()
            Southwest._instance = self

    @staticmethod
    def get_instance():
        if not Southwest._instance:
            Southwest()
        return Southwest._instance

    def print(self):
        print("Southwest")

    def walkRandom(self, someone):
        someone.goSouthwest()

    def setEMinOr(self, em, aContainer):
        aContainer.southwest = em

    def recorrerEn(self, unBloque, aContainer):
        aContainer.southwest.recorrer(unBloque)


class Form:
    def __init__(self):
        self.orientations = []
        self.point = None
        self.extent=None
        self.num=None

    def addOrientation(self, orientation):
        self.orientations.append(orientation)   
    def removeOrientation(self, orientation):
        self.orientations.remove(orientation)
    def getRandomOrientation(self):
        return random.choice(self.orientations)
    def setEMinOr(self, em, orientation):
        orientation.setEMinOr(em, self)
    def recorrer(self,unBloque):
        for orient in self.orientations:
            orient.recorrerEn(unBloque,self)
    def getCommand(self):
        lista=[]
        for orient in self.orientations:
            lista += orient.getCommandFrom(self)
        return lista
    def setPoint(self,point):
        self.point=point
    def getPoint(self):
        return self.point
    def calcularPosicion(self):
        for orient in self.orientations:
            orient.calcularPosicionDesde(self)

class Rectangle(Form):
    def __init__(self,num):
        super().__init__()
        self.num = num
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.addAllOrientations()

    def addAllOrientations(self):
        self.addOrientation(North.get_instance())
        self.addOrientation(South.get_instance())
        self.addOrientation(East.get_instance())
        self.addOrientation(West.get_instance())
    def goNorth(self, someone):
        self.north.enter(someone)
    def goEast(self, someone):
        self.east.enter(someone)
    def goSouth(self, someone):
        self.south.enter(someone)
    def goWest(self, someone):
        self.west.enter(someone)

class Hexagon(Form):
    def __init__(self):
        super().__init__()
        self.north = None
        self.northeast = None
        self.southeast = None
        self.south = None
        self.southwest = None
        self.northwest = None
        self.addAllOrientations()
    def addAllOrientations(self):
        self.addOrientation(North.get_instance())
        self.addOrientation(Northeast.get_instance())
        self.addOrientation(Southeast.get_instance())
        self.addOrientation(South.get_instance())
        self.addOrientation(Southwest.get_instance())
        self.addOrientation(Northwest.get_instance())

    def goNorth(self, someone):
        self.north.enter(someone)

    def goNortheast(self, someone):
        self.northeast.enter(someone)

    def goSoutheast(self, someone):
        self.southeast.enter(someone)

    def goSouth(self, someone):
        self.south.enter(someone)

    def goSouthwest(self, someone):
        self.southwest.enter(someone)

    def goNorthwest(self, someone):
        self.northwest.enter(someone)

class Octaedro(Form):
    def __init__(self):
        super().__init__()
        self.north = None
        self.northeast = None
        self.southeast = None
        self.south = None
        self.southwest = None
        self.northwest = None
        self.east = None
        self.west = None
        self.addAllOrientations()
    
    def addAllOrientations(self):
        self.addOrientation(North.get_instance())
        self.addOrientation(Northeast.get_instance())
        self.addOrientation(Southeast.get_instance())
        self.addOrientation(South.get_instance())
        self.addOrientation(Southwest.get_instance())
        self.addOrientation(Northwest.get_instance())
        self.addOrientation(East.get_instance())
        self.addOrientation(West.get_instance())

    def goNorth(self, someone):
        self.north.enter(someone)

    def goNortheast(self, someone):
        self.northeast.enter(someone)

    def goSoutheast(self, someone):
        self.southeast.enter(someone)

    def goSouth(self, someone):
        self.south.enter(someone)

    def goSouthwest(self, someone):
        self.southwest.enter(someone)

    def goNorthwest(self, someone):
        self.northwest.enter(someone)

    def goEast(self, someone):
        self.east.enter(someone)
    
    def goWest(self, someone):
        self.west.enter(someone)

