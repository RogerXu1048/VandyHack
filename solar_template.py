#solar.py
#This uses the first four planets of the solar system and the sun
from codinglib import*
from body_template import Body
from system_template import System
'''import all of codinglib, the System class from system program, and the Body class from your body program (3 lines)
the window width and height should both be 600, but you just need to specify something                   (2 lines)'''
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
AU = 1.49598e11 #number of meters per astronomical unit
EM = 5.9736e24  #mass of the Earth in kilograms

TIME_SCALE = 3.0e6              #how many real seconds for each second of simulation
PIXELS_PER_METER = 120 / AU    #distance scale for the simulation

FRAME_RATE = 30
TIMESTEP = 1.0 / FRAME_RATE     #time between drawing each frame

#Solar system data from http://hyperphysics.phy-astr.gsu.edu/hbase/solar/soldata2.html
'''
initialize the sun, mercury, earth, and mars each as a instance of the Body class                     (5 lines)
the parameters are listed in the Body class, of course
the yellow one's the sun, mercury is orange, venus purple, earth blue-green, mars red

mo' planets mo' credit

initialize the solar system as a instance of the System class                                         (1 line)
the lone parameter it takes is the list of bodies
'''
Sun=Body(1.9891e30,0,0,0,0,30,1,1,0)
Mercury=Body(3.3e23,5.79e10,0,0,47400,4,1,0.8,0)
Earth=Body(5.976e24,1.496e11,0,0,29800,12,0,1,1)
Mars=Body(6.42e23,2.279e11,0,0,24100,6,1,0,0)
Venus=Body(4.87e24,1.082e11,0,0,35000,11,1,0,1)
solar_system=System([Sun,Mercury,Earth,Mars,Venus])
def main():
    #give it a black background and enable smoothing                                                       (2 lines)
    #clear the screen                                                                                      (1 line)
    set_clear_color(0,0,0)
    enable_smoothing()
    clear()
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER) #draw the system
    solar_system.update(TIMESTEP * TIME_SCALE) #and update the relevant numbers

'''start the graphics software with main as a parameter, then a title, width is your window width,
height is your window height, and window height    (1 line)'''

start_graphics(main, "Solar system simulation", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate = FRAME_RATE)
