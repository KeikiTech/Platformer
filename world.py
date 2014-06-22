from player import Player
from platform import *

class World:

    MAX_Y = 1000

    def __init__(self, physics):
        self.physics = physics

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.platforms = []

    def load(self, iostream):
        for line in iostream:
            if line.startswith("#"):
                continue
            fields = line.strip().split()
            if len(fields) < 3:
                continue
            x = int(fields[1])
            y = int(fields[2])
            if fields[0] == "BigPlatform":
                self.create_big_platform(x, y)
            elif fields[0] == "SmallPlatform":
                self.create_small_platform(x, y)
            elif fields[0] == "SmallHMovingPlatform":
                self.create_small_hmoving_platform(x, y)
            elif fields[0] == "SmallYMovingPlatform":
                self.create_small_ymoving_platform(x, y)


    def create_big_platform(self, x, y):
        platform = BigPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)
        
    def create_small_platform(self, x, y):
        platform = SmallPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_small_hmoving_platform(self, x, y):
        platform = SmallHMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_small_ymoving_platform(self, x, y):
        platform = SmallYMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)
    
        # Check for game over; respawn if necessary
        if self.player.position.y > self.MAX_Y:
            self.player.position.x = self.player.current_checkpoint.x
            self.player.position.y = self.player.current_checkpoint.y

        self.player.update(dt)

        self.physics.handle_collisions()

    def draw(self, target):
        for platform in self.platforms:
            target.draw(platform)

        target.draw(self.player)
