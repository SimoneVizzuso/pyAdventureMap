from adventure import world
import uuid

class Player:
    def __init__(self):
        self.hp = 100
        self.victory = False
        self.invetory = set()
        self.position_x, self.position_y = world.starting_position_x, world.starting_position_y
        self.uuid = uuid.uuid1()


