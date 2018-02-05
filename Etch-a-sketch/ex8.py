from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos
import sys


def init():
    glClearColor(1, 1, 0.75, 1)
    gluOrtho2D(-2, 2, -2, 2)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, .35, 0.75)
    glPointSize(1)
    # Plot the coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(0.0, 3.0)
    glVertex2f(0.0, -3.0)
    glEnd()

    glBegin(GL_POINTS)
    for t in arange(-250, 250, 0.001):
        y = sin(0.99*t) - 0.7*cos(3.01*t)
        x = cos(1.01*t) + 0.1*sin(15.03*t)
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
