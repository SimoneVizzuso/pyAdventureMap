class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return 'Appare un {}\nIl nemico ha {} punti ferita\n'.format(self.name, self.hp)

    def is_alive(self):
        return self.hp > 0


def loadEnemy(enemy_list):
    with open("resource/enemy") as enemies:
        lines = enemies.readlines()
        for line in lines:
            tmp = line.replace("\n", "").split(",")
            e = Enemy(tmp[0], tmp[1], tmp[2])
            enemy_list.add(e)
