from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, tan, exp
import sys

slices = 16
stacks = 16


def resize(width, height):
    ar = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-ar, ar, -1, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    t = glutGet(GLUT_ELAPSED_TIME) / 1000
    a = t * 90
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3d(1, 1, 0.35)

    glPushMatrix()
    glTranslated(-2.4, 1.2, -6)
    glRotated(a, 1, 0, 0)
    glRotated(a, 0, 0, 1)
    glutSolidSphere(1, slices, stacks)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, 1.2, -6)
    glRotated(a, 1, 0, 1)
    glRotated(a, 0, 0, 1)
    glutSolidSierpinskiSponge(1, 1, 1)
    glPopMatrix()

    glPushMatrix()
    glTranslated(2.4, 1.2, -6)
    glRotated(a, 1, 0, 0)
    glRotated(10*sin(a), 0, 0, 1)
    glutSolidTorus(0.2, 0.8, slices, stacks)
    glPopMatrix()

    glPushMatrix()
    glTranslated(-2.4, -1.2, -6)
    glRotated(sin(a)/10, 1, 0, 0)
    glRotated(a, 0, 0, 1)
    glutSolidTeapot(1)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0, -1.2, -6)
    glRotated(a, 1, 0, 0)
    glRotated(a, 0, 0, 1)
    glutWireCone(1, 1, slices, stacks)
    glPopMatrix()

    glPushMatrix()
    glTranslated(2.4, -1.2, -6)
    glRotated(60, 1, 0, 0)
    glRotated(a, 0, 0, 1)
    glutWireTorus(0.2, 0.8, slices, stacks)
    glPopMatrix()

    glutSwapBuffers()


def key(key, x, y):
    global slices, stacks
    if key == 27 or key != 27:
        if key == 'q':
            sys.exit(0)
        elif key == '+':
            slices += 1
            stacks += 1
        elif key == '-':
            if slices > 3 and stacks > 3:
                slices -= 1
                stacks -= 1
    glutPostRedisplay()


def idle():
    glutPostRedisplay()


light_ambient = [0.0, 0.0, 0.0, 1.0]
light_diffuse = [1.0, 0.0, 1.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [2.0, 5.0, 5.0, 0.0]
mat_ambient = [0.7, 0.7, 0.7, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
high_shininess = [100]


def main():
    glutInit(sys.argv)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(10, 10)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutCreateWindow(b"GLUT Shapes")

    glutReshapeFunc(resize)
    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutIdleFunc(idle)

    glClearColor(1, 1, 1, 1)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

    glutMainLoop()


main()
