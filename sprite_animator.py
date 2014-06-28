import sys
import sfml as sf

from player import Player

def calculate_frame_loop_args(row):
    start = (row - 1) * 6
    end = start + 5
    return start, end

# Check arguments
if len(sys.argv) != 3:
    sys.stderr.write("Here's how to use it -- Just type:\n\n")
    sys.stderr.write("\tpython3 sprite_animator.py <row> <frame_delay>\n\n")
    sys.stderr.write("So if you wanted to animate row 4 with a frame delay of 0.1 seconds,\n")
    sys.stderr.write("you'd type  python3 sprite_animator 4 0.1\n\n")
    sys.exit()

# Process arguments
row_number = int(sys.argv[1])
frame_delay = float(sys.argv[2])
frame_start, frame_end = calculate_frame_loop_args(row_number)

# Create the main window
window = sf.RenderWindow(sf.VideoMode(65, 90), "pySFML Window")
window.key_repeat_enabled = False
view = window.default_view

# Create and configure Player
player = Player(0, 0)
player._sprite.set_frame_loop(12, 17)
player._sprite.set_frame_loop(frame_start, frame_end)
player._sprite._frame_delay = frame_delay
    
# Timey stuff
clock = sf.Clock()

# start the game loop
while window.is_open:
    for event in window.events:
        # close window: exit
        if type(event) is sf.CloseEvent:
            window.close()

    dt = clock.restart().seconds

    ## Update
    player._sprite.update(dt)

    ## Draw
    window.clear(sf.Color(120, 120, 120)) # clear screen
    window.view = view
    
    # Draw the world
    window.draw(player)

    #### Draw GUI stuff, reset view
    window.view = window.default_view
   
    window.display() # update the window


