from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
import sys


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-5, 5, -5, 5)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    glBegin(GL_POINTS)

    for x in arange(-5, 5, 0.01):
        y = x**2
        l = 0.5*x + 3
        glColor3f(1, 0, 0)

        glVertex2f(x, y)
        glVertex2f(x, l)
        for a in arange(-5, 5, 0.01):
            if a > x**2 and x > 0 and a < l:
                glColor3f(0.5, 0.5, 0.5)
                glVertex2f(x, a)
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
