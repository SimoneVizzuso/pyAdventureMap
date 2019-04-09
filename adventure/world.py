import uuid

starting_position_x = 0
starting_position_y = 0


class Room:
    """Room"""

    def __init__(self, x, y, title, description):
        self.x = x
        self.y = y
        self.title = title
        self.description = str(description)
        self.uuid = uuid.uuid1()

    def printInit(self):
        print("You are in " + self.title + "\n")
        self.printDesc()

    def printTitle(self):
        print("You are in " + self.title + "\n --You've already been in this room--")

    def exist(self, x, y):
        return self.x == x and self.y == y

    def printDesc(self):
        desc = self.description.split(".")
        for elem in desc:
            print(elem + "\n")


def loadWorld(l):
    with open("resource/adventureMap") as m:
        lines = m.readlines()
        for line in lines:
            tmp = line.split(";")
            r = Room(int(tmp[0]), int(tmp[1]), tmp[2], tmp[3])
            l.add(r)
