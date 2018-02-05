from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
from time import sleep


def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-5, 5, -5, 5)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(3)

    glBegin(GL_LINES)
    glVertex2f(-5, 0)
    glVertex2f(5, 0)
    glVertex2f(0, 5)
    glVertex2f(0, -5)
    glVertex2f(-5, 1)
    glVertex2f(5, 0)
    glEnd()

    for x in arange(-5, 5, .001):
        y = x**2
        a = x + 3
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(x, a)
        glEnd()
        glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Function Plotter")
    glutDisplayFunc(plot_func)
    init()
    glutMainLoop()


main()
