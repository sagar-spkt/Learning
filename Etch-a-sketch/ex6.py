from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos
import sys


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-2, 2, -2, 2)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(1)

    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(0.0, 3.0)
    glVertex2f(0.0, -3.0)
    glEnd()

    glBegin(GL_POINTS)
    for a in arange(0.1, 2, 0.1):
        for t in arange(-4.4, 4.4, 0.01):
            x = 0.3*a*(t*t - 3)
            y = 0.1*a*t*(t*t - 3)
            glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Sine and Cosine')
    glutDisplayFunc(plot_func)
    init()
    glutMainLoop()


main()
