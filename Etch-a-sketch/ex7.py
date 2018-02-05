from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos, pi
import sys


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-2, 2, -2, 2)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(1)
    # glRotatef(-45, 0, 0, 1)
    # Plot the coordinate axes
    # glBegin(GL_LINES)
    # glVertex2f(-3.0, -3.0)
    # glVertex2f(3.0, 3.0)
    # glVertex2f(-3.0, 3.0)
    # glVertex2f(3.0, -3.0)
    # glEnd()

    glBegin(GL_POINTS)
    a, b = 1.5, 1
    for t in arange(-250, 250, 0.001):
        x = sin(0.99*t) - 0.7*cos(3.01*t)
        y = cos(1.01*t) + 0.1*sin(15.03*t)

        # ellipse in y=x major axis
        # x = a*cos(t)*cos(pi/4)-b*sin(t)*sin(pi/4)
        # y = b*sin(t)*cos(pi/4)+a*cos(t)*sin(pi/4)
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
