class Item:
    def __init__(self, name, description, action):
        self.name = name
        self.description = description
        self.action = action

    def print(self):
        print('==========\n{}\n{}\n'.format(self.name, self.description))

    def printAction(self):
        print('{} - Con questo oggetto puoi svolgere le seguenti azioni:\n{}\n==========\n'.format(self.name, self.action))


class Weapon(Item):
    def __init__(self, name, description, action, damage):
        self.damage = damage
        super().__init__(name, description, action)

    def __str__(self):
        return '{}\n{}\nDamage: {}\n'.format(self.name, self.description, self.damage)


class Scroll(Item):
    def __init__(self, name, description, action, effect, power, descEffect):
        self.effect = effect
        self.power = power
        self.descEffect = descEffect
        super().__init__(name, description, action)

    def __str__(self):
        print('{}\n{}\nEffect: {}\n'.format(self.name, self.description, self.effect))

    def printEffect(self):
        print(self.descEffect)


def loadItem(item_list):
    with open("resource/items") as items:
        lines = items.readlines()
        for line in lines:
            actions = []
            tmp = line.replace("\n", "").split(",")
            action = tmp[3].split(".")
            for a in action:
                actions.append(a)
            if tmp[0] == "weapon":
                i = Weapon(tmp[1], tmp[2], actions, tmp[4])
            elif tmp[0] == "scroll":
                i = Scroll(tmp[1], tmp[2], actions, tmp[4], tmp[5], tmp[6])
            else:
                i = Item(tmp[1], tmp[2], actions)
            item_list.add(i)
