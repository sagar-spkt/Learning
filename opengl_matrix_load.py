from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Window size
width = height = 600


def init():
    glClearColor(0, 0, 0, 1)

    # Enable depth testing for true 3D effects
    glEnable(GL_DEPTH_TEST)

    # Add lighting and shading effects
    glShadeModel(GL_SMOOTH)
    lightdiffuse = [0.8, 0.87, 0.7, 1.0]
    lightposition = [1.0, 1.0, 1.0, 0.0]
    lightambient = [0.0, 0.0, 0.0, 1.0]
    lightspecular = [1.0, 1.0, 1.0, 1.0]

    # Turn on the light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightdiffuse)
    glLightfv(GL_LIGHT1, GL_POSITION, lightposition)
    glLightfv(GL_LIGHT1, GL_AMBIENT, lightambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, lightdiffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, lightspecular)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)


def zap():
    # Camera position
    global camx, camy, camz
    camx = camy = camz = 5


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glColor3f(1, 0, 0)

    glutSolidCube(1)
    glPopMatrix()
    glutSwapBuffers()


def keyboard(key, x, y):
    key = key.decode('utf-8')
    if key == chr(27):
        sys.exit()
    if key == 'z':
        zap()
    if key == 'a' or key == 'A':
        pass


def special_key(key, x, y):
    pass


def idle():
    glutPostRedisplay()


def reshape(w, h):
    if h == 0:
        h = 1

    # Fill the entire graphics window
    glViewport(0, 0, w, h)

    # Set the projection matrix... our 'view'
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set how we view the world and position our eyeball
    gluPerspective(35, w/h, 1, 1000)

    # Set the matrix for the object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # ar = width / height
    # glViewport(0, 0, width, height)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glFrustum(-ar, ar, -1, 1, 2, 100)
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    # Place the camera position, the direction of view
    # and which axis is UP
    gluLookAt(camx, camy, camz, 0, 0, 0, 0, 0, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Home 3D')
    glutReshapeFunc(reshape)
    glutDisplayFunc(plot_func)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_key)
    glutIdleFunc(idle)
    init()
    zap()
    glutMainLoop()


main()
