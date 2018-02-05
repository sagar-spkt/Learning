from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import random as rand
from numpy import *
import sys

global width, height

width = height = 600


def init():
    glClearColor(1, 1, 1, 0)
    # glColor3f(0.3, 0.6, 0.2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3, 3, 0, 10.5)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def plot_func():
    x, y = -1.5, 0.75
    glClear(GL_COLOR_BUFFER_BIT)
    for n in range(0, 100000):
        v = rand()
        if (v >= 0) and (v <= 0.8):
            a, b, c, d, e, f = 0, 1.6, -2.5*pi/180, -2.5*pi/180, 0.85, 0.85
            glColor3f(1, 0, 0)
        elif (v > 0.8) and (v <= 0.8050):
            a = b = c = d = e = 0
            f = 0.16
            glColor3f(0, 1, 0)
        elif (v > 0.8050) and (v <= 0.9025):
            a, b, c, d, e, f = 0, 1.6, 49*pi/180, 49*pi/180, 0.3, 0.34
            glColor3f(0, 0, 1)
        elif (v > 0.9025) and (v <= 1):
            a, b, c, d, e, f = 0, 0.44, 120*pi/180, -50*pi/180, 0.3, 0.37
            glColor3f(1, 0, 1)
        xx, yy = x, y
        x = e * xx * cos(c) - f * yy * sin(d) + a
        y = e * xx * sin(c) + f * yy * cos(d) + b

        if n > 10:
            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()
            glFlush()


def keyboard(key, x, y):
    # Allows us to quit by pressing 'Esc' or 'q'
    if key == chr(27):
        sys.exit()
    if key == "q":
        sys.exit()


def main():
    global width
    global height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(width,height)
    glutCreateWindow(b'The Chaos Game... Fern!')
    glutDisplayFunc(plot_func)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()


main()