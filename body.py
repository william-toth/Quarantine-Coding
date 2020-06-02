#Author: William Toth
#Date: 02/13/20
#Purpose: To create a class for a celestial body

from cs1lib import *

#Creating class for celestial body
class Body:

    #Initializing variables
    def __init__ (self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    #Methof that updates position of body
    def update_position (self, timestep):
        self.x = self.x + (self.vx * timestep)
        self.y = self.y + (self.vy * timestep)

    #Method that updates velocity of body
    def update_velocity (self, ax, ay, timestep):
        self.vx = self.vx + (ax * timestep)
        self.vy = self.vy + (ay * timestep)

    #Method that draws body
    def draw (self, cx, cy, pixels_per_meter):

        #Setting color of body
        set_stroke_color (self.r, self.g, self.b)
        set_fill_color (self.r, self.g, self.b)

        draw_circle (self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)