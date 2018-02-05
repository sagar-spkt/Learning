from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

spin = 0

def init():
    glClearColor(0, 0, 0, 0)
    glShadeModel(GL_FLAT);


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(spin, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glRectf(-25.0, -25.0, 25.0, 25.0)
    glPopMatrix()
    glutSwapBuffers()


def spinDisplay():
    global spin
    spin = spin + 2
    if (spin > 360):
        spin = spin - 360
    glutPostRedisplay()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            glutIdleFunc(spinDisplay)
    elif button == GLUT_MIDDLE_BUTTON:
        if state == GLUT_DOWN:
            glutIdleFunc(None)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(sys.argv[0].encode('utf-8'))
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()

main()
