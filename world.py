from res import Res
from player import Player
from platform import *
from fireball import Fireball
from ufo import UFO
from spritesheet import SpriteSheet

class World:

    MAX_Y = 1000

    def __init__(self, physics, font):
        self.physics = physics
        self.font = font

        self.player = Player(100, 50)
        self.physics.add_collideable(self.player)
        
        self.health_rect_back = sf.RectangleShape()
        self.health_rect_back.position = sf.Vector2(5, 50)
        self.health_rect_back.size = sf.Vector2(200, 24)
        self.health_rect_back.fill_color = sf.Color(0, 0, 0, 255)
        self.health_rect = sf.RectangleShape()
        self.health_rect.position = sf.Vector2(5, 50)
        self.health_rect.size = sf.Vector2(200, 24)
        self.health_rect.fill_color = sf.Color(0, 255, 0, 255)
        
        self.game_over = False
        self.game_over_text = sf.Text("Game Over!", font, 40)
        self.game_over_text.position = sf.Vector2(300, 200)
        
        self.platforms = []
        self.ufos = []
        self.fireballs = []
        self.explosions = []
        self.text = []

    def load(self, iostream):
        for line in iostream:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if len(fields) < 3:
                continue
            x = int(fields[1])
            y = int(fields[2])
            if fields[0] == "Text":
                text = fields[3]
                text = text.replace("\\n", "\n")
                self.create_text(x, y, text)
            elif fields[0] == "BigPlatform":
                self.create_big_platform(x, y)
            elif fields[0] == "SmallPlatform":
                self.create_small_platform(x, y)
            elif fields[0] == "SmallHMovingPlatform":
                self.create_small_hmoving_platform(x, y)
            elif fields[0] == "SmallVMovingPlatform":
                self.create_small_vmoving_platform(x, y)
            elif fields[0] == "Fireball":
                self.create_fireball(x, y)
            elif fields[0] == "UFO":
                self.create_ufo(x, y)

    def create_text(self, x, y, text):
        text_object = sf.Text(text, self.font, 20)
        text_object.position = sf.Vector2(x, y)
        self.text.append(text_object)

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

    def create_small_vmoving_platform(self, x, y):
        platform = SmallVMovingPlatform(x, y)
        self.platforms.append(platform)
        self.physics.add_collideable(platform)

    def create_fireball(self, x, y):
        fireball = Fireball(x, y, self)
        self.fireballs.append(fireball)
        self.physics.add_collideable(fireball)

    def create_explosion(self, x, y):
        explosion = SpriteSheet(Res.explosion)
        explosion.init(16, 4, 0.1)
        explosion.position = sf.Vector2(x, y)
        explosion.set_frame_loop(0, 9, False)
        self.explosions.append(explosion)
        Res.explosion_sound.loop = False
        Res.explosion_sound.volume = 10.0
        #Res.explosion_sound.position = (x, y, 0)
        Res.explosion_sound.play()
    
    def create_ufo(self, x, y):
        ufo = UFO(x, y, self)
        self.ufos.append(ufo)
        self.physics.add_collideable(ufo)
        
    def update(self, dt):
        if self.game_over:
            Res.music.pause()
            Res.explosion_sound.pause()
            return
    
        for platform in self.platforms:
            platform.update(dt)
        
        for ufo in self.ufos:
            ufo.update(dt)

        to_remove = []
        for fireball in self.fireballs:
            fireball.update(dt)
            if fireball.dead or fireball.position.y > 500:
                to_remove.append(fireball)
        for r in to_remove:
            self.fireballs.remove(r)
            self.physics.remove_collideable(r)
        
        to_remove = []
        for explosion in self.explosions:
            explosion.update(dt)
            if explosion.loop_done:
                to_remove.append(explosion)
        for r in to_remove:
            self.explosions.remove(r)
    
        # Check for game over; respawn if necessary
        if self.player.position.y > self.MAX_Y:
            self.player.position.x = self.player.current_checkpoint.x
            self.player.position.y = self.player.current_checkpoint.y

        self.player.update(dt)
        self.physics.handle_collisions()
        
        self.health_rect.size = sf.Vector2((self.player.health/5)*200, 24)
        
        if self.player.health <= 0:
            self.game_over = True
        
        #sf.Listener.set_position((self.player.position.x, self.player.position.y, 0))

    def draw(self, target):
        if self.game_over:
            target.view = target.default_view
            target.draw(self.game_over_text)
            return
    
        for platform in self.platforms:
            target.draw(platform)

        target.draw(self.player)
        
        for ufo in self.ufos:
            target.draw(ufo)
        
        for fireball in self.fireballs:
            target.draw(fireball)
            
        for explosion in self.explosions:
            target.draw(explosion)
        
        for text in self.text:
            target.draw(text)
        
        target.view = target.default_view
        
        target.draw(self.health_rect_back)
        target.draw(self.health_rect)
