from player import Player
from platform import *

class World:

    def __init__(self, physics):
        self.physics = physics

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.platforms = []

    def load(self, iostream):
        for line in iostream:
            fields = line.strip().split()
            if len(fields) < 3:
                continue
            x = int(fields[1])
            y = int(fields[2])
            if fields[0] == "BigPlatform":
                self.create_big_platform(x, y)
            elif fields[0] == "SmallPlatform":
                self.create_small_platform(x, y)


    def create_big_platform(self, x, y):
        platform = BigPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)
        
    def create_small_platform(self, x, y):
        platform = SmallMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)
    
        self.player.update(dt)

        self.physics.handle_collisions()

    def draw(self, target):
        for platform in self.platforms:
            target.draw(platform)

        target.draw(self.player)
