from adventure import world
from adventure.world import Room


def play():
    map = set()
    world.loadWorld(map)
    for room in map:
        if room.x == world.starting_position_x and room.y == world.starting_position_y:
            start = room
    start.printInit()


if __name__ == "__main__":
    play()
