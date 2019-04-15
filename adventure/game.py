from adventure.resource import enemies
from adventure.resource import items
from adventure.resource.player import Player


def play():
    item = set()
    items.loadItem(item)
    enemy = set()
    enemies.loadEnemy(enemy)
    player = Player()
    player.intro()
    while player.isAlive() and not player.win():
        player.printAction()
        player.action(input())


if __name__ == "__main__":
    play()
