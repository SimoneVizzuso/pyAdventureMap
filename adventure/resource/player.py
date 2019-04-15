import uuid

from adventure import world


class Player:
    def __init__(self):
        self.hp = 100
        self.victory = False
        self.inventory = set()
        self.position_x, self.position_y = 0, 0
        self.adventureMap = set()
        self.nextRooms = {'nord': False, 'sud': False, 'est': False, 'ovest': False}
        self.localRoom = None
        self.uuid = uuid.uuid1()
        self.weapon = None

    def isAlive(self):
        return self.hp > 0

    def win(self):
        return self.victory

    def printInventory(self):
        for item in self.inventory:
            print(item)
            item.printAction()

    def heal(self, hpHealed):
        self.hp = self.hp + hpHealed
        if self.hp > 100:
            self.hp = 100

    def hit(self, damage):
        self.hp = self.hp - int(damage)
        print("\nTi rimane " + str(self.hp) + " di vita")

    def inventoryAction(self):
        if not self.inventory:
            print("\nNon hai oggetti nell'inventario")
        else:
            choice = input("Quale oggetto vuoi usare?")
            for i in self.inventory:
                if i.getName() == choice.lower():
                    action = input("Che cosa vuoi fare?")
                    for a in i.chooseAction():
                        if action.lower() == a:
                            if action.lower() == "equipaggia":
                                if self.weapon is not None:
                                    self.inventory.add(self.weapon)
                                    self.weapon = None
                                self.inventory.remove(i)
                                self.weapon = i
                                print("\nHai equipaggiato l'oggetto")
                                return
                            if action.lower() == "cura":
                                self.heal(i.getPower())
                                i.printEffect()
                            if action.lower() == "danno":
                                self.hit(i.getPower())
                                i.printEffect()
                            if action.lower() == "esci":
                                return

    def addInventory(self, item):
        self.inventory.add(item)

    def printAction(self):
        self.localRoomInit()

        print("\n==========\n\nAttualmente puoi svolgere le seguenti azioni:\n")
        for room in self.adventureMap:
            if room.getX() == self.position_x and room.getY() == self.position_y + 1 and room.isLocked() is False:
                print("Nord - Spostati nella stanza a Nord")
                self.nextRooms['nord'] = True
            if room.getX() == self.position_x and room.getY() == self.position_y - 1 and room.isLocked() is False:
                print("Sud - Spostati nella stanza a Sud")
                self.nextRooms['sud'] = True
            if room.getX() == self.position_x + 1 and room.getY() == self.position_y and room.isLocked() is False:
                print("Est - Spostati nella stanza ad Est")
                self.nextRooms['est'] = True
            if room.getX() == self.position_x - 1 and room.getY() == self.position_y and room.isLocked() is False:
                print("Ovest - Spostati nella stanza ad Ovest")
                self.nextRooms['ovest'] = True
        print("Oggetti - Apri il tuo Inventario")
        print("Guarda - Osserva attentamente la zona (rilegge la descrizione)")
        print("Esplora - Cerca oggetti e strumenti")

    def combactAction(self):
        print("\n==========\n\nAttualmente puoi svolgere le seguenti azioni:\n")
        print("Attacca - Colpisci con l'arma equipaggiata")
        print("Oggetti - Apri il tuo inventario")

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
            self.printInventory()
            self.inventoryAction()
        elif choice.lower() == 'guarda':
            for room in self.adventureMap:
                if room.getX() == self.position_x and room.getY() == self.position_y:
                    room.printDesc()
        elif choice.lower() == 'esplora':
            self.explore()
        else:
            print("\nInserisci una azione valida")

    def localRoomInit(self):
        for x in self.adventureMap:
            if x.getX() == self.position_x and x.getY() == self.position_y:
                self.localRoom = x

    def move(self, x, y):
        for room in self.adventureMap:
            if room.getX() == self.position_x + x and room.getY() == self.position_y + y:
                self.position_x = room.getX()
                self.position_y = room.getY()
                self.localRoomInit()
                room.print()
                room.setVisited()
                return

    def combact(self):
        enemy = self.localRoom.getEnemy()
        print("\nAppare un" + enemy.getName())
        while enemy.is_alive():
            print(enemy)
            self.combactAction()
            choice = input("Cosa vuoi fare?\n")
            if choice.lower() == "attacca":
                enemy.hit(self.weapon.getDamage())
            elif choice.lower() == "Oggetti":
                self.printInventory()
            if enemy.is_alive():
                self.hit(enemy.getDamage())
                print(str(enemy.getName()) + " nemico ti infligge " + str(enemy.getDamage()))
            else:
                print("\nHai sconfitto il nemico!")
                for room in self.adventureMap:
                    if self.localRoom == room:
                        room.loseEnemy()

    def explore(self):
        global x
        if self.localRoom.getItems() is not None:
            for x in self.adventureMap:
                if x == self.localRoom:
                    x.printItem()
            actions = x.getItems().chooseAction()
            actualAction = input("Che cosa vuoi fare con questo oggetto?")
            for tmp in actions:
                if actualAction.lower() == tmp:
                    if actualAction.lower() == "raccogli":
                        self.addInventory(x.getItems())
                        print("Hai raccolto l'oggetto")
                        x.loseItem()
                    elif actualAction.lower() == "tira":
                        x.useLever()
                        x.loseItem()
        else:
            print("Non c'e' altro che puoi fare in questa stanza")

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
