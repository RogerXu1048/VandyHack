#system.py
#A driver that allows different bodies to interact, defines System class
from math import sqrt
from body_template import Body

UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.67384e-11
class System:
    def __init__(self, body_list): #initializes a System (1 line)
        self.body_list = body_list
        '''store the body list to the unspecified body list'''

    def draw(self, cx, cy, pixels_per_meter): #draws System by drawing each body in body list (1 extra line)
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)
        '''for each body in the unspecified body list'''


    def dist(self, n1, n2): #compute the distance between bodies n1 and n2. (1 extra line)
        dx = self.body_list[n2].get_x() - self.body_list[n1].get_x()
        dy = self.body_list[n2].get_y() - self.body_list[n1].get_y()

        '''return the distance between the two bodies'''
        return sqrt(dx*dx+dy*dy)

    def compute_acceleration(self, n): #computes the acceleration of all other bodies on body n (9 added lines)
        '''start the total x and y accelerations at 0. (2 lines here)'''
        n_x = self.body_list[n].get_x()
        n_y = self.body_list[n].get_y()
        total_ax = 0
        total_ay = 0

        #'''for index in the range of the length of the unspecified body list (1 line here)'''
        #    '''if the index is not the same as the body we are finding the accelerations for (1 line here)'''
        #        '''set r to the unspecified distance between the index & the body we're calculating for (1 line here)'''
        #        '''calculate acceleration (a) using self.body_list[i].get_mass() to get the index's mass.
        #        use this from Newton's Universal Law of Gravitation: a = G * mass / r^2 (1 line here)'''
        for i in range(len(self.body_list)):
            if n != i:
                r=self.dist(i,n)

                a = UNIVERSAL_GRAVITATIONAL_CONSTANT * self.body_list[i].get_mass() / (r*r)

                dx = self.body_list[i].get_x() - n_x
                ax = a * dx / r
                dy = self.body_list[i].get_y() - n_y
                ay = a * dy / r
                total_ax += ax
                total_ay += ay
        return (total_ax,total_ay)
        #        #Now you have the acceleration. Break it down into its x and y components and add them to running sums

        #       '''add these x and y acceleration to the total x and y accelerations (2 lines here)'''

        #'''return the total x and y accelerations, typing it as a point (1 line here)'''

    def update(self, timestep): #computes body's x & y, then uses the acceleration to update each body's velocity
        for n in range(len(self.body_list)):
            self.body_list[n].update_position(timestep)

        for n in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax, ay, timestep)
