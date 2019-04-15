import uuid

from adventure.resource import items, enemies

starting_position_x = 0
starting_position_y = 0

itemsList = set()
enemiesList = set()

messageInit = """
Benvenuto in questo magico mondo, sei pronto ad iniziare la tua avventura?
Combatterai contro mostri e draghi, in questa ricerca verso l'ignoto
Sei finito qui in seguito all'inseguimento di alcune guardie della citta'
Dopo aver rubato del cibo per fame sei stato rincorso fino ad ora finendo di fronte ad una cavita' all'interno di una montagna
Avendo paura di farti vedere decidi di entrare e sperare nella buona fede
Nel momento in cui entri dentro la grotta senti la porta dietro di te chiudersi rumorosamente."""


class Room:
    """Room"""

    def __init__(self, x, y, title, description, item, enemy, locked):
        self.x = int(x)
        self.y = int(y)
        self.title = title
        self.enemy = enemy
        self.item = item
        self.description = description
        self.visited = False
        self.uuid = uuid.uuid1()
        self.locked = locked

    def print(self):
        if self.visited:
            print("\n>>Ti trovi in " + self.title + "\n\nSei già stato in questa stanza\n")
            return
        print("\n>>Ti trovi in " + self.title)
        self.printDesc()

    def printDesc(self):
        print("\n")
        desc = self.description.split(".")
        for elem in desc:
            print(elem)

    def setVisited(self):
        self.visited = True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getItems(self):
        if self.item is not None:
            return self.item

    def printItem(self):
        if self.item is not None:
            print(self.item)

    def loseEnemy(self):
        self.enemy = None

    def getEnemy(self):
        if self.enemy is not None:
            return self.enemy

    def loseItem(self):
        self.item = None

    def useLever(self):
        print("\nHai tirato la leva, senti dei rumori in lontananza")

    def isLocked(self):
        return self.locked


def loadWorld(d):
    items.loadItem(itemsList)
    enemies.loadEnemy(enemiesList)
    with open("resource/adventureMap") as m:
        lines = m.readlines()
        for line in lines:
            print(line)
            tmp = line.split(",")
            if tmp[4] != ' ':
                for i in itemsList:
                    if i.name == tmp[4]:
                        addItem = i
                        r = Room(int(tmp[0]), int(tmp[1]), tmp[2], tmp[3], addItem, tmp[5], tmp[6])
            elif tmp[5] != ' ':
                for e in enemiesList:
                    if e.name == tmp[5]:
                        addEnemy = e
                        r = Room(int(tmp[0]), int(tmp[1]), tmp[2], tmp[3], tmp[4], addEnemy, tmp[6])
            else:
                r = Room(int(tmp[0]), int(tmp[1]), tmp[2], tmp[3], tmp[4], tmp[5], tmp[6])
            d.add(r)

