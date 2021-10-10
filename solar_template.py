#solar.py
#This uses the first four planets of the solar system and the sun
from codinglib import*
from body_template import Body
from system_template import System
from math import sqrt
'''import all of codinglib, the System class from system program, and the Body class from your body program (3 lines)
the window width and height should both be 600, but you just need to specify something                   (2 lines)'''
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
AU = 1.49598e11 #number of meters per astronomical unit
EM = 5.9736e24  #mass of the Earth in kilograms

TIME_SCALE = 3.0e6            #how many real seconds for each second of simulation
PIXELS_PER_METER = 120 / AU /3   #distance scale for the simulation

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
Sun=Body(1.9891e30,0,0,0,0,25/2,1,1,0)
Mercury=Body(3.3e23,5.79e10,0,0,47400,4/2,1,0.8,0)
Earth=Body(5.976e24,1.496e11,0,0,29800,12/2,0,1,1)
Mars=Body(6.42e23,2.279e11,0,0,24100,6/2,1,0,0)
Venus=Body(4.87e24,1.082e11,0,0,35000,11/2,1,0,1)
Jupiter=Body(1.9e27,7.786e11,0,0,13100,18/2,1,1,1)
Saturn=Body(5.69e26,1.433e12,0,0,9600,13/2,0.8,0.6,1)

'''Sun1=Body(1.9891e30,-2e11,0,0,0,16,1,1,0)
Sun2=Body(1.9891e30,2e11,0,0,0,16,1,0,0)
Sun3=Body(1.9891e30,0,sqrt(3)*2e11,0,0,16,0,1,0)'''

solar_system=System([Sun,Mercury,Earth,Mars])
'''solar_system=System([Sun1, Sun2, Sun3])'''


'''def clicked():
    global drawn
    drawn = True'''

'''drawn = False

def clicked(mx, my):
    global drawn
    drawn=True'''


def main():
    #give it a black background and enable smoothing                                                       (2 lines)
    #clear the screen     #
    #                                                                                   (1 line)
    set_clear_color(0,0,0)
    enable_smoothing()
    clear()
    solar_system.draw(WINDOW_WIDTH/2 , WINDOW_HEIGHT/2 , PIXELS_PER_METER) #draw the system
    solar_system.update(TIME_SCALE * TIMESTEP) #and update the relevant numbers
    bt1 = Button(100, 600, 100, 100, False)
    bt2 = Button(100, 350, 100, 100, False)
    bt3 = Button(100, 100, 100, 100, False)
    bt1.draw_rec_button()
    bt2.draw_rec_button()
    bt3.draw_rec_button()
    if bt1.is_clicked():
        # coding_quit()
        # start_graphics(main2, "Sn", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=FRAME_RATE)

        Venus = Body(4.87e24, 1.082e11, 0, 0, 35000, 11/2, 1, 0, 1)
        solar_system.add(Venus)

    if bt2.is_clicked():
            # coding_quit()
            # start_graphics(main2, "Sn", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=FRAME_RATE)
        Jupiter = Body(1.9e27, 7.786e11, 0, 0, 13100, 18 / 2, 1, 1, 1)
        solar_system.add(Jupiter)

    if bt3.is_clicked():
            # coding_quit()                # start_graphics(main2, "Sn", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=FRAME_RATE)
        Saturn = Body(5.69e26, 1.433e12, 0, 0, 9600, 13 / 2, 0.8, 0.6, 1)
        solar_system.add(Saturn)

'''start the graphics software with main as a parameter, then a title, width is your window width,
height is your window height, and window height    (1 line)'''


start_graphics(main, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate = 60)