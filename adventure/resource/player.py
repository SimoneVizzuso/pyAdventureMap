from adventure import world
import uuid


class Player:
    def __init__(self):
        self.hp = 100
        self.victory = False
        self.inventory = set()
        self.position_x, self.position_y = 0, 0
        self.adventureMap = set()
        self.nextRooms = {'nord':False, 'sud':False, 'est':False, 'ovest':False}
        self.uuid = uuid.uuid1()

    def isAlive(self):
        return self.hp > 0

    def win(self):
        return self.victory

    def printInventory(self):
        for item in self.inventory:
            print(item)

    def printAction(self):
        print("\n==========\n\nAttualmente puoi svolgere le seguenti azioni:\n")
        for room in self.adventureMap:
            if room.getX() == self.position_x and room.getY() == self.position_y + 1:
                print("Nord - Spostati nella stanza a Nord")
                self.nextRooms['nord'] = True
            if room.getX() == self.position_x and room.getY() == self.position_y - 1:
                print("Sud - Spostati nella stanza a Sud")
                self.nextRooms['sud'] = True
            if room.getX() == self.position_x + 1 and room.getY() == self.position_y:
                print("Est - Spostati nella stanza ad Est")
                self.nextRooms['est'] = True
            if room.getX() == self.position_x - 1 and room.getY() == self.position_y:
                print("Ovest - Spostati nella stanza ad Ovest")
                self.nextRooms['ovest'] = True
        print("Oggetti - Apri il tuo Inventario")
        print("Esplora - Osserva la zona")

    def action(self, choice):
        if choice.lower() == 'nord':
            if self.nextRooms['nord']:
                self.move(0, 1)
        elif choice.lower() == 'sud':
            if self.nextRooms['sud']:
                self.move(0, -1)
        elif choice.lower() == 'est':
            if self.nextRooms['est']:
                self.move(1, 0)
        elif choice.lower() == 'ovest':
            if self.nextRooms['ovest']:
                self.move(-1, 0)
        elif choice.lower() == 'oggetti':
            self.itemAction()
        else:
            print("\nInserisci una azione valida")

    def localRoom(self):
        for room in self.adventureMap:
            if room.getX() == self.position_x and room.getY() == self.position_y:
                room.print()

    def move(self, x, y):
        for room in self.adventureMap:
            if room.getX() == self.position_x + x and room.getY() == self.position_y + y:
                self.position_x = room.getX()
                self.position_y = room.getY()
                self.localRoom()

    def itemAction(self):
        if not self.inventory:
            print("\nNon hai oggetti nell'inventario")
        else:
            for i in self.inventory:
                i.printAction()

    def intro(self):
        world.loadWorld(self.adventureMap)
        print(world.messageInit)
        for m in self.adventureMap:
            if m.getX() == 0 and m.getY() == 0:
                self.position_x = m.getX()
                self.position_y = m.getY()
                m.print()
                m.setVisited()
                break
