import uuid
starting_position_x = 0
starting_position_y = 0

messageInit ="""
Benvenuto in questo magico mondo, sei pronto ad iniziare la tua avventura?
Combatterai contro mostri e draghi, in questa ricerca verso l'ignoto
"""


class Room:
    """Room"""

    def __init__(self, x, y, title, description):
        self.x = x
        self.y = y
        self.title = title
        self.description = description
        self.visited = False
        self.uuid = uuid.uuid1()

    def print(self):
        if self.visited:
            print(">>Ti trovi in " + self.title + "\n Sei già stato in questa stanza\n")
            return
        print(">>Ti trovi in " + self.title + "\n")
        self.printDesc()

    def printDesc(self):
        desc = self.description.split(".")
        for elem in desc:
            print(elem)

    def setVisited(self):
        self.visited = True


def loadWorld(d):
    with open("resource/adventureMap") as m:
        lines = m.readlines()
        for line in lines:
            tmp = line.split(";")
            r = Room(int(tmp[0]), int(tmp[1]), tmp[2], tmp[3])
            key = str(tmp[0]) + "," + str(tmp[1])
            d[key] = r
