from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global width, height, axrng

width, height, axrng = 500, 500, 10


def init():
    glClearColor(1, 1, 1, 1)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)

    # Plotting functions
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(1, 2)
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
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow(b'py_skel')
    glutReshapeFunc(reshape)
    glutDisplayFunc(plot_func)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
