#Author: William Toth
#Date: 02/15/20
#Purpose: To test system and body classes by modelling the solar system

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 5000000         # real seconds per simulation second
PIXELS_PER_METER = (3 / 1e7) / 400  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)

sun = Body (1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0) #Yellow sun
mercury = Body (0.330e24, 57.9e9, 0, 0, 47.4e3, 2, 1, 0.5, 0) #Orange mercury
venus = Body (4.87e24, 108.2e9, 0, 0, 35.0e3, 4, 0, 0.7, 0) #Green venus
earth = Body(5.9736e24, 149.6e9, 0, 0, 29.8e3, 7, 0, 0, 1) #Blue earth
mars = Body (642e24, 227.9e9, 0, 0, 24.1e3, 3, 0.8, 0, 0) #Red mars

solar = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)