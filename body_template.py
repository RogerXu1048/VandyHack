#body.py: Body class for gravitational simulation
from codinglib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b): #initializes a Body object (9 lines)
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b
        '''self.anything = that parameter'''

    def get_mass(self):     #returns the mass of a Body object (1 line)
        return self.mass
        '''return the mass of an unspecified Body object'''

    def get_x(self): #returns the x position of a Body object (1 lines)
        return self.x
        '''return the x position of an unspecified Body object'''

    #returns the y position of a Body object (1 line)
    def get_y(self):
        return self.y
        '''return the y position of an unspecified Body object'''

    #updates the position of a Body object for a given timestep (2 lines)
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep
        '''x = x + vx*timestep, just like before, but for an unspecified Body object
        do it for y too'''

    #updates velocities of a Body object for a given timestep (2 lines)
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep
        '''just like our position updates, but between velocity and acceleration
        instead of position and velocity'''

    #has Body object draw itself (4 lines)
    def draw(self, cx, cy,pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        disable_stroke()
        enable_fill()
        draw_circle(pixels_per_meter * self.x + cx, pixels_per_meter * self.y + cy, self.pixel_radius)
        '''set the appropriate fill color, disable stroke, enable fill, and draw a circle

        circle's center should be the (pixels per meter * the unspecified x) away from the center x value
        its center should be the (pixels per meter * the unspecified y) away from the center y value
        its radius should be the unspecified pixel radius'''
