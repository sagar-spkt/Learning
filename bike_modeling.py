from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


angle1 = angle2 = angle3 = 0


def draw_wheels():
    glColor3f(0, 0, 0)
    glutSolidTorus(0.3, 1, 100, 100)


def draw_rims():
    glColor3f(0.75, 0.75, 0.75)
    glutSolidTorus(100, 0.1, 100, 100)


def axis():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)

    glEnd()


def skimmer():
    glPushMatrix()
    glTranslatef(-6, 0, 0)
    draw_wheels()
    # draw_rims()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3, 0, 0)
    draw_wheels()
    draw_rims()
    glPopMatrix()

    glRotatef(angle1, 1, 0, 0)
    glRotatef(angle2, 0, 1, 0)
    glRotatef(angle3, 0, 0, 1)
    axis()


def my_display():
    glClearColor(0.66, 0.83, 0.91, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 8, 0, 0, 0, 0, 1, 0)
    glTranslatef(0, 0, -8)
    skimmer()
    glutSwapBuffers()


def reshape(w, h):
    if h == 0:
        h = 1

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key,x, y):
    global angle1, angle2, angle3
    key = key.decode('utf-8')
    if key == chr(27):
        sys.exit()
    if key == 'x':
        angle1 = (angle1 + 5) % 360
    if key == 'X':
        angle1 = (angle1 - 5) % 360
    if key == 'y':
        angle2 = (angle2 + 5) % 360
    if key == 'Y':
        angle2 = (angle2 - 5) % 360
    if key == 'z':
        angle3 = (angle3 + 5) % 360
    if key == 'Z':
        angle3 = (angle3 - 5) % 360
    if key == 'c' or key == 'C':
        angle1 = angle2 = angle3 = 0
    my_display()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Camera')
    glutDisplayFunc(my_display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()