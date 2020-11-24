from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# init global variables 
dimension = 800
width = dimension
height = dimension
layer0 = [0,0]
layer1 = [0,0]
layer2 = [0,0]
layer3 = [0,0]
color_1 = (random.random(), random.random(), random.random())
color_2 = (random.random(), random.random(), random.random())
color_3 = (random.random(), random.random(), random.random())
bird_move = 0

def drawRectangle(x, y, width, height):
    glBegin(GL_QUADS) 
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing

def drawFillEllipse(x, y, radiusX, radiusY):
    glBegin(GL_POLYGON)
    for i in range(360):
        rad = math.pi*i/180
        glVertex2f(x + math.cos(rad)*radiusX, y + math.sin(rad)*radiusY)
    glEnd()

def drawEllipse(x, y, radiusX, radiusY):
    glLineWidth(1)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        rad = math.pi*i/180
        glVertex2f(x + math.cos(rad)*radiusX, y + math.sin(rad)*radiusY)
    glEnd()

def blueSky():
    # draw bluesky background
    glColor3f(135/255, 206/255, 235/255)
    drawRectangle(0 ,0 , width, height)

def sun(radius):
    x= (layer0[0] + 0.9*width)
    y= (layer0[1]+0.8*height)
    glColor3f(1.0, 1.0, 0.0)
    drawFillEllipse(x, y, radius, radius)
    glColor3f(0.0, 0.0, 0.0)
    drawEllipse(x, y, radius, radius)

def drawTriangle(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x-width/2, y)
    glVertex2f(x+width/2, y)
    glVertex2f(x, y + height)
    glEnd()

def mountain():
    # draw further moutain - first layer
    glColor3f(*color_1)  # set random color 1
    drawTriangle(layer1[0]+width/2, layer1[1]+0, width*0.7, height*0.65)

    # draw 2 closer moutain - second layer
    glColor3f(*color_2)  # set random color 2
    drawTriangle(layer2[0]+width*0.2, layer2[1]+0, width*1, height*0.55)

    glColor3f(*color_3)  # set random color 3
    drawTriangle(layer2[0]+width*0.8, layer2[1]+0, width*1, height*0.55)

def blades():
    glColor3f(140/255, 251/255, 35/255)
    drawRectangle(0 ,0 , width, layer3[1]+height*0.17)

def grass():
    glColor3f(140/255, 251/255, 35/255)
    for i in range(-100, 200):
        drawRectangle(layer3[0]+ i*width/100,layer3[1]+height*0.17,width/200,height/20)
    
def tree():
    glColor3f(112/255, 41/255, 45/255)
    drawRectangle(layer3[0]+ width*0.7, layer3[1]+height*0.1, width*0.05, height*0.1)
    glColor3f(0/255, 94/255, 0/255)
    drawFillEllipse(layer3[0]+ width*0.725, layer3[1]+height*0.3, width*0.1, height*0.15)
    glColor3f(0/255, 0/255, 0/255)
    drawEllipse(layer3[0]+ width*0.725, layer3[1]+height*0.3, width*0.1, height*0.15)

def Foreground():
    blades()
    grass()
    tree()

def birds():
    glColor3f(0/255, 0/255, 0/255)
    glLineWidth(3)
    global bird_move
    for i in range(5):
        glBegin(GL_LINE_STRIP)
        glVertex2f(layer0[0]+width*0.0+i*width*0.06+bird_move*width*0.01, layer0[1]+height*0.7-i*height*0.025)
        glVertex2f(layer0[0]+width*0.03+i*width*0.06+bird_move*width*0.01, layer0[1]+height*0.69-i*height*0.025)
        glVertex2f(layer0[0]+width*0.06+i*width*0.06+bird_move*width*0.01, layer0[1]+height*0.7-i*height*0.025)
        glEnd()

def landscape():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)
    
    blueSky()
    sun(30)
    mountain()
    Foreground()
    birds()

    glutSwapBuffers()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def motion_func(x, y):
    layer0[0] = x/50 
    layer0[1] = y/50

    layer1[0] = x/16 
    layer1[1] = y/16

    layer2[0] = x/12
    layer2[1] = y/12

    layer3[0] = x/5
    layer3[1] = y/5
   
def update(value):
    global bird_move
    bird_move+=1
    if bird_move > 150:
        bird_move = -50

# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, int(height))  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("Motion Parallax Landscape")  # create window with title
glutTimerFunc(50, update, 0)
glutDisplayFunc(landscape)  # set showScreen function callback
glutPassiveMotionFunc(motion_func)   # passive mouse event handler
glutIdleFunc(landscape)  # draw all the time
glutMainLoop()  # start everythingc