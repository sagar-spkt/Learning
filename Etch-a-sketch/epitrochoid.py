from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos, pi
import sys


def init():
    glClearColor(0.35, 0.79, 0.60, 1)
    gluOrtho2D(-20, 20, -20, 20)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(1)

    a, b, c = 12, 2.25, 5
    glBegin(GL_POINTS)
    for t in arange(-4*pi, 4*pi, 0.001):
        x = (a + b) * cos(t) - c * cos((a / b + 1.0) * t)
        y = (a + b) * sin(t) - c * sin((a / b + 1.0) * t)
        glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Epitrochoid')
    glutDisplayFunc(plot_func)
    init()
    glutMainLoop()


main()
