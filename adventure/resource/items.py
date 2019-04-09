class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}\n{}\n\n==========\n'.format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return '{}\n{}\nDamage: {}\n\n==========\n'.format(self.name, self.description, self.damage)


class Scroll(Item):
    def __init__(self, name, description, effect):
        self.effect = effect
        super().__init__(name, description)

    def __str__(self):
        return '{}\n{}\nEffect: {}\n\n==========\n'.format(self.name, self.description, self.effect)


def loadItem(item_list):
    with open("resource/items") as items:
        lines = items.readlines()
        for line in lines:
            tmp = line.replace("\n", "").split(",")
            if tmp[0] == "weapon":
                i = Weapon(tmp[1], tmp[2], tmp[3])
            elif tmp[0] == "scroll":
                i = Scroll(tmp[1], tmp[2], tmp[3])
            else:
                i = Item(tmp[1], tmp[2])
            item_list.add(i)
