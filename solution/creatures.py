# beast.pyclass Beast:
import time

from solution.maze import Lleno, Treasury

class Creature:
    def __init__(self):
        self.position = None
        self.game=None
        self.life=None
        self.power=None
    
    def goNorth(self):
        self.position.goNorth(self)
    def goEast(self):
        self.position.goEast(self)
    def goSouth(self):
        self.position.goSouth(self)
    def goWest(self):
        self.position.goWest(self)
    def goNortheast(self):
        self.position.goNortheast(self)
    def goNorthwest(self):
        self.position.goNorthwest(self)
    def goSoutheast(self):
        self.position.goSoutheast(self)
    def goSouthwest(self):
        self.position.goSouthwest(self)

    def attack(self):
        enemy=self.findEnemy()
        if enemy:
            enemy.isAttackedBy(self)
    def collect(self):
        pass
    def heal(self):
        enemy=self.findEnemy()
        if enemy:
            enemy.isHealedBy(self)
    def isHealedBy(self, other):
        pass
    def findEnemy(self):
        pass
    def isAttackedBy(self, other):
        pass

class Person(Creature):
    def __init__(self, name, type):
        super().__init__()
        self.life=20
        self.power=1
        self.name=name
        self.type = type
    def __str__(self):
        return self.name + ' ' + str(self.type)
    def findEnemy(self):
        return self.game.findEnemyCreature(self.position)
    def collect(self):
        if self.position.isTreasury():
            self.position.state.collectTreasure(self)
        else:
            print(self.position, 'is not a Treasury')
    def isAttackedBy(self, other):
        self.life -= other.power
        print(self, "is attacked by", other)
        if self.life <= 0:
            print(self, "is dead, GAME OVER")
            self.game.stopThreds()
            exit()
        else:
            print(self, "life is now", self.life)
    
    def isHealedBy(self, other):
        self.life += other.power
        print(self, "is healed by", other, "for", other.power)
        print(self, "now has", self.life, 'lives')

class Type:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def ultimate(self, person):
        pass
    def isWarrior(self):
        return False
    def isArcher(self):
        return False
    def isWizard(self):
        return False

class Warrior():
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Warrior"
    
    def isWarrior(self):
        return True

    def print(self):
        print("Character is warrior")
    
    def ultiamte(self, person):
        person.life += 7
        print('Character has now 7 more lives\n Currently has:\n ', person.power, ' power\n', person.life, ' lives')

class Archer():
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Archer"
    
    def isArcher(self):
        return True

    def print(self):
        print("Character is archer")
    
    def ultiamte(self, person):
        person.power += 2
        print('Character has now 2 more power\n Currently has:\n ', person.power, ' power\n', person.life, ' lives')

class Wizard():
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Wizard"
    
    def isWizard(self):
        return True

    def print(self):
        print("Character is wizard")

    def ultiamte(self, person):
        person.power += 1
        person.life += 2
        print('Character has now 1 more power and 2 more lives\n Currently has:\n ', person.power, ' power\n', person.life, ' lives')



class Boss(Creature):
    def __init__(self, power = 5, life = 30):
        super().__init__()
        self.power = power
        self.life = life
        self.num=0

    def __str__(self):
        template='Boss-{0.num}'
        return template.format(self)
    
    def findEnemy(self):
        return self.game.findPerson(self.position)
    
    def isBoss(self):
        True

    def start(self):
        self.act()

    def stop(self):
        print(self , "is stopped")
        exit(0)

    def isAttackedBy(self, other):
        self.life -= other.power
        print(self, "is attacked by", other)
        if self.life <= 0:
            print(self, "is dead")
            self.game.removeBoss(self)
            if type(self.position) is Treasury:
                self.position.change_state(Lleno(self.position))
            self.game.check_wincondition()
        else:
            print(self, "life is now", self.life)   

    def act(self):
        while self.life > 0:
            self.sleep()
            self.attack()
    
    def sleep(self):
        print(self,"is sleeping in", self.position)
        time.sleep(3)

class Beast(Creature):
    def __init__(self, mode, power = 2, life = 10):
        super().__init__()
        self.mode = mode
        self.power = power
        self.life = life
        self.num=0
    
    def __str__(self):
        template='Beast-{0.mode}{0.num}'
        return template.format(self)
    
    def isAggressive(self):
        return self.mode.isAggressive()

    def isLazy(self):
        return self.mode.isLazy()
    
    def isDelicioso(self):
        return self.mode.isDelicioso()
    
    def act(self):
        self.mode.act(self)
    
    def walkRandom(self):
        self.position.walkRandom(self)
    
    def isAttackedBy(self, other):
        self.life -= other.power
        print(self, "is attacked by", other)
        if self.life <= 0:
            print(self, "is dead")
            self.game.removeBeast(self)
            self.game.check_wincondition()
        else:
            print(self, "life is now", self.life)

    def start(self):
        self.act()

    def stop(self):
        print(self , " is stopped")
        exit(0)

    def findEnemy(self):
        return self.game.findPerson(self.position)

class Mode:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def isAggressive(self):
        return False
    def isLazy(self):
        return False
    def isDelicioso(self):
        return False
    def isDepredador(self):
        return False
    def act(self, beast):
        while beast.life > 0:
            self.sleep(beast)
            self.walk(beast)
            self.attack(beast)
    def walk(self, beast):
        beast.walkRandom()
    def sleep(self, beast):
        print(beast," is sleeping")
        time.sleep(3)
    def attack(self,beast):
        beast.attack()
    def heal(self, beast):
        beast.heal()

class Aggressive(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Aggressive"
    
    def isAggressive(self):
        return True

    def print(self):
        print("Aggressive beast")

class Lazy(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Lazy"
    
    def print(self):
        print("Lazy beast")

    def isLazy(self):
        return True

class Depredador(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Depredador"
    
    def print(self):
        print("Depredador beast")

    def isDepredador(self):
        return True
    
class Delicioso(Mode):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Delicioso"
    
    def print(self):
        print("Delicioso beast")

    def isDelicioso(self):
        return True
    
    def act(self, beast):
        while beast.life > 0:
            self.sleep(beast)
            self.walk(beast)
            self.heal(beast)