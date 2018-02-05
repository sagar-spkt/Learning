from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos
import sys


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-5, 5, -5, 5)


def draw_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-5, 0)
    glVertex2f(5, 0)
    glVertex2f(0, -5)
    glVertex2f(0, 5)
    glEnd()
    glBegin(GL_POINTS)
    for x in arange(-5, 5, 0.001):
        glColor3f(1, 0, 0)
        glVertex2f(x, sin(x))
        glColor3f(1, 0, 1)
        glVertex2f(x, cos(x))
        glColor3f(1, 1, .5)
        glVertex2f(x, 3*sin(x))
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Sine and Cosine')
    glutDisplayFunc(draw_func)
    init()
    glutMainLoop()


main()
