import sfml as sf

class Res:
    blue_peewee = sf.Texture.from_file("Content/bluepeewee.png")
    big_platform = sf.Texture.from_file("Content/bigplatform.png")
    small_platform = sf.Texture.from_file("Content/smallplatform.png")
    acid_platform = sf.Texture.from_file("Content/acidplatform.png")
    ufo = sf.Texture.from_file("Content/ufo.png")
    fireball = sf.Texture.from_file("Content/fireball.png")
    explosion = sf.Texture.from_file("Content/explosion.png")
    
    # Sounds
    music = sf.Sound(sf.SoundBuffer.from_file("Content/bgmusic.wav"))
    explosion_sound = sf.Sound(sf.SoundBuffer.from_file("Content/explosion.wav"))
