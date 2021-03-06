from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos, pi
import sys


def init():
    glClearColor(0.35, 0.79, 0.60, 1)
    gluOrtho2D(-2, 2, -2, 2)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(1)

    a, b = 0.5, 11
    glBegin(GL_POINTS)
    for t in arange(0, 2*pi, 0.001):
        x = a * (2.0 * cos(t) - cos(2.0 * t))
        y = a * (2.0 * sin(t) - sin(2.0 * t))
        glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Cardiod')
    glutDisplayFunc(plot_func)
    init()
    glutMainLoop()


main()
