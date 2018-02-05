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
    # Plot the coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()

    # Plot the parametric equation
    glBegin(GL_LINES)
    a, b, c, d = 1, 1, 0.25, 0.1
    for t in arange(-6.28, 6.28, 0.001):
        glVertex2f(a*cos(t), b*sin(t))
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
