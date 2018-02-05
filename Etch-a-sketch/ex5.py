from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos
import sys


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-3, 3, -3, 3)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(1)
    # Plot the coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(0.0, 3.0)
    glVertex2f(0.0, -3.0)
    glEnd()

    # Plot the parametric equation
    glBegin(GL_POINTS)
    a, b, c, d, e = 2, 1, 1.5, 3.5, 6
    for t in arange(-1, 1, 0.1):
        glVertex2f(sin(t), sin(a*t + b) + c*sin(d*t + e))
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
