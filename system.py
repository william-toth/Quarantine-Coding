#Author: William Toth
#Date: 02/13/20
#Purpose: To create a class for a system of celestial bodies

#Defining value for universal gravitational constant
G = 6.67384e-11

#Creating class for system of bodies
class System:

    #Initializing variables
    def __init__ (self, body_list):
        self.body_list = body_list

    #Method that updates position and velocity of bodies in the system
    def update (self, timestep):
        for body in self.body_list:
            body.update_position (timestep)

        for body in self.body_list:
            (ax_total, ay_total) = self.compute_acceleration (body)
            body.update_velocity (ax_total, ay_total, timestep)

    #Method that draws bodies in the system
    def draw (self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw (cx, cy, pixels_per_meter)

    #Methof to compute acceleration of each body
    def compute_acceleration (self, n):
        ax = 0
        ay = 0
        for i in self.body_list:

            #To avoid planets attracting themselves
            if i == n:
                continue

            #Calculating Radius
            r = ((n.x - i.x) ** 2 + (n.y - i.y) ** 2)**0.5

            #Calculating acceleration between two bodies
            a = (G * i.mass / r**2)

            #Calculating and adding up partial components of acceleration
            ax_partial = a * (i.x-n.x) / r
            ax = ax + ax_partial
            ay_partial = a * (i.y - n.y) / r
            ay = ay + ay_partial

        return (ax, ay)