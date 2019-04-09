from adventure import world
from adventure.resource import items
from adventure.resource import enemies


def play():
    map = dict()
    world.loadWorld(map)
    item = set()
    items.loadItem(item)
    enemy = set()
    enemies.loadEnemy(enemy)
    print(world.messageInit)
    start = str(world.starting_position_x) + "," + str(world.starting_position_y)
    if start in map:
        r = map[start]
        r.print()
        r.setVisited()
    while


if __name__ == "__main__":
    play()
