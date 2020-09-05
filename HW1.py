###
### Adopted from https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/
### CSC 322 Fall 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

window = 0
dimention = 1200
width = dimention
height = int(width*2/3)

def drawSquare(x, y, width, height):
    glBegin(GL_QUADS)  # start drawing a square
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing


def drawTriangle(x, y, width, height):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glEnd()


def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    glColor3f(0.0, 0.0, 1.0)  # set color to blue
    drawSquare(50, 50, 200, 200)  # draw a square at (50,50) with width 200, height 200

    glColor3f(1.0, 0.0, 0.0)  # set color to red
    drawTriangle(300, 50, 200, 200)  # draw a triangle at (300,50)

    glutSwapBuffers()  # important for double buffering\

def drawStar(x = dimention/2, y = dimention/3, a = dimention):
    glBegin(GL_POLYGON)
    R = a/5
    r = R * math.sqrt(2)*math.cos(math.pi*72/180)


    for n in range(5):
        # glVertex2f(x + R * math.cos(math.pi * (90 + 72 * n) / 180),
        #            y + R * math.sin(math.pi * (90 + 72 * n) / 180))
        glVertex2f(x + r * math.cos(math.pi * (126 + 72 * n) / 180),
                   y + r * math.sin(math.pi * (126 + 72 * n) /180))
    glEnd()


    '''The for loop result was not turn out as expectation
    Thus, I have to draw separate 1 pentagon and 5 triangles
    '''
    glBegin(GL_TRIANGLES)
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 4) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 4) / 180))
    glVertex2f(x + R * math.cos(math.pi * (90 + 72 * 0) / 180),
               y + R * math.sin(math.pi * (90 + 72 * 0) / 180))
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 0) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 0) / 180))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 0) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 0) / 180))
    glVertex2f(x + R * math.cos(math.pi * (90 + 72 * 1) / 180),
               y + R * math.sin(math.pi * (90 + 72 * 1) / 180))
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 1) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 1) / 180))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 1) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 1) / 180))
    glVertex2f(x + R * math.cos(math.pi * (90 + 72 * 2) / 180),
               y + R * math.sin(math.pi * (90 + 72 * 2) / 180))
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 2) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 2) / 180))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 2) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 2) / 180))
    glVertex2f(x + R * math.cos(math.pi * (90 + 72 * 3) / 180),
               y + R * math.sin(math.pi * (90 + 72 * 3) / 180))
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 3) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 3) / 180))
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 3) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 3) / 180))
    glVertex2f(x + R * math.cos(math.pi * (90 + 72 * 4) / 180),
               y + R * math.sin(math.pi * (90 + 72 * 4) / 180))
    glVertex2f(x + r * math.cos(math.pi * (126 + 72 * 4) / 180),
               y + r * math.sin(math.pi * (126 + 72 * 4) / 180))
    glEnd()


# Function draw VietNam national flag
# Red background and a yellow star in the middle
def drawFlag():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()    # reset position
    refresh2d(width, height)

    glColor3f(1.0, 0.0, 0.0)  # set color to red
    drawSquare(0 ,0, width, height) #background

    glColor3f(1,1,0)  # set color to yellow
    drawStar()

    glutSwapBuffers()

def sky():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()    # reset position
    refresh2d(width, height)

    # glColor3f(1.0, 0.0, 0.0)  # set color to red
    # drawSquare(0 ,0, width, height) #background

    for n in range(100):
        glColor3f(random.random(), random.random(), random.random())  # set random color
        drawStar(random.random()*dimention, random.random()*dimention, random.random()*100) #set random position and dimention

    glutSwapBuffers()


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, int(height))  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("CSC 322 Fall 2020 HW1")  # create window with title
glutDisplayFunc(sky)  # set showScreen function callback
glutIdleFunc(sky)  # draw all the time
glutMainLoop()  # start everything
