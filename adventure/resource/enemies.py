class Enemy:
    def __init__(self, name, hp, damage):
        self.name = str(name)
        self.hp = int(hp)
        self.damage = int(damage)

    def __str__(self):
        return '{}\nIl nemico ha {} punti ferita\n'.format(self.name, self.hp)

    def is_alive(self):
        return self.hp > 0

    def getName(self):
        return '{}'.format(self.name)

    def getDamage(self):
        return self.damage

    def hit(self, hitDamage):
        self.hp = self.hp - int(hitDamage)


def loadEnemy(enemy_list):
    with open("resource/enemy") as enemies:
        lines = enemies.readlines()
        for line in lines:
            tmp = line.replace("\n", "").split(",")
            e = Enemy(tmp[0], tmp[1], tmp[2])
            enemy_list.add(e)
