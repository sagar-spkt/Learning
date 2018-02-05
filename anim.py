from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import random as rn
from numpy import *
from time import *
import sys


axrng = 2
width = 400
height = 400
hstep = 2 * axrng / width
vstep = 2 * axrng / height


def escape_time(x, y):
    n = 0
    z = a = complex(x, y)
    while n < 25:
        z = z ** 2 + a
        zz = abs(z)
        if zz > 2:
            n = 5001
        n += 1
    return zz


def init():
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-axrng, axrng, -axrng, axrng)


def draw_bound_mandel():
    global escape
    glClear(GL_COLOR_BUFFER_BIT)
    tim = time()
    for i in range(0, 1000000):
        x = -2 * axrng * rn() + 0.5
        y = 1.25 * axrng * rn() - 1.25
        if (y < 0.625 * x + 1.25) and (y > -0.625 * x - 1.25):
            bound = 0
            leng = escape_time(x + hstep, y)
            if leng < 2:
                bound += 1
            leng = escape_time(x - hstep, y)
            if leng < 2:
                bound += 1
            leng = escape_time(x, y - vstep)
            if leng < 2:
                bound += 1
            leng = escape_time(x, y + vstep)
            if leng < 2:
                bound += 1
            if (bound > 0) and (bound < 4):
                glColor3ub(85 * bound, 50 * bound, 90 * bound)
                glBegin(GL_POINTS)
                glVertex2f(x, y)
                glEnd()
                glFlush()
    print(time() - tim)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'Julia set')
    glutDisplayFunc(draw_bound_mandel)
    init()
    glutMainLoop()

main()
