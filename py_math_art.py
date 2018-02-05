from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arange
from math import sin, cos, tan, log, sqrt
import sys

global width, height, axrng, stepsize

width, height, axrng = 500, 500, 10
stepsize = 2*axrng/width


def init():
    glClearColor(1, 1, 1, 1)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)

    for x in arange(-axrng, axrng, stepsize):
        for y in arange(-axrng, axrng, stepsize):
            r = cos(x) + sin(y)
            # r = cos(x) + sin(y) - tan(x*y)
            # r = cos(x**2) + sin(3*y) - tan(x*y/4)
            # r = cos(x)**2 + sin(y/3) - sqrt(abs(x*y))
            # r = cos(x)**2 + sin(y/3) - log(abs(x*y))
            # r = cos(x)**2 + sin(y/3) - log(abs(x))
            # r = cos(x) ** 2 + sin(y * y) ** 2 + tan(x * y) ** 2
            glColor3f(cos(y*r), cos(x*y*r), sin(r*x))
            # glColor3f(r*r, x*r, y*x*r)
            # glColor3f(cos(r), cos(r), cos(r))
            # glColor3f(tan(r**2), sin(x*r)*cos(x*y), sin(y*x)*tan(x))
            # glColor3f(x * y * sin(r), sin(x * r * y) * cos(r * y), sin(y * x) * cos(r))
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


def keyboard(key, x, y):
    if key == chr(27) or key == 'q':
        sys.exit()


def main():
    global width, height
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(500, 0)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'Math Art Patterns')
    glutReshapeFunc(reshape)
    glutDisplayFunc(plot_func)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
