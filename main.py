import sfml as sf

from player import *
from spritesheet import *

# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 480), "pySFML Window")

try:
    # Create player
    player = Player()

    # create some graphical text to display
    font = sf.Font.from_file("Content/8bit.ttf")
    frame_rate = sf.Text("0", font, 20)

except IOError: exit(1)

clock = sf.Clock()
frame_accum = 0
dt_accum = 0

# start the game loop
while window.is_open:
    dt = clock.restart().seconds
    
    # Calculate framerate
    frame_accum += 1
    dt_accum += dt
    if dt_accum >= 1:
        frame_rate.string = str(frame_accum)
        dt_accum = 0
        frame_accum = 0

    # process events
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()

    player.update(dt)
    
    ## Draw
    
    window.clear(sf.Color(120, 120, 120)) # clear screen
    
    # Draw the player
    window.draw(player)
    
    # Draw framerate
    window.draw(frame_rate)
    
    window.display() # update the window