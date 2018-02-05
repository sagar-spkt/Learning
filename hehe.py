from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *
from math import sin, cos, tan
import sys


global width, height, axrng

width, height, axrng = 500, 500, 2


def init():
    glClearColor(1, 1, 1, 0)
    glColor3f(0, 0, 0)


def plot_func():
    verts = [[-2.0, 2.0], [-2.0, -2.0], [2.0, 2.0],
             [2.0, -2.0], [-1.0, 1.0], [-1.0, -1.0],
             [1.0, 1.0], [1.0, -1.0]]
    x, y = -1.5, 0.75
    glClear(GL_COLOR_BUFFER_BIT)
    for n in range(0, 100000):
        v = randint(0, len(verts) - 1)
        x = (tan(y**2 * x) + verts[v][0])/2
        y = (tan(y) + verts[v][1])/3

        if n > 30:
            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()
            glFlush()


def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if w <= h:
        gluOrtho2D(-axrng, axrng, -axrng*h/w, axrng*h/w)
    else:
        gluOrtho2D(-axrng*w/h, axrng*w/h, -axrng, axrng)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global width, height

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'The Chaos Game')
    glutReshapeFunc(reshape)
    glutDisplayFunc(plot_func)
    init()
    glutMainLoop()


main()
