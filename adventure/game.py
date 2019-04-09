from adventure import world


def play():
    map = dict()
    world.loadWorld(map)
    print(world.messageInit)
    start = str(world.starting_position_x) + "," + str(world.starting_position_y)
    if start in map:
        r = map[start]
        r.print()
        r.setVisited()
        r.print()


if __name__ == "__main__":
    play()
