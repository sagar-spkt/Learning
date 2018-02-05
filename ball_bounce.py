from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# # globals for animation, ball position and direction of motion
# global anim, x, y, dx, dy

# initial ball position
x, y = 0, 0.34

hvel = vvel = 0.000

# Window dimension
width = height = 500
axrng = 10
radius = 0.5

# No animation at start
anim = False

# parameter for reshaping
xborder = yborder = axrng


def init():
    glClearColor(0, 0, 0, 1)
    glColor3ub(255, 156, 250)

    # Dimensions of the screen
    gluOrtho2D(-axrng, axrng, -axrng, axrng)


def idle():
    # We animate only if anim is 'True'
    global anim
    if anim:
        glutPostRedisplay()


def reshape(w, h):
    global x, y, xborder, yborder
    # To insure we don't have a zero height
    if h == 0:
        h = 1

    # fill the entire graphics window!
    glViewport(0, 0, w, h)

    # Set the projection matrix... our view
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set the aspect ratio of the plot so that it always looks ok
    if w <= h:
        gluOrtho2D(-axrng, axrng, -axrng*h/w, axrng*h/w)
        yborder = axrng*h/w
        xborder = axrng
    else:
        gluOrtho2D(-axrng*w/h, axrng*w/h, -axrng, axrng)
        xborder = axrng*w/h
        yborder = axrng
    if x <= -xborder:
        x = -xborder + 2 * radius
    if x >= xborder:
        x = xborder - 2 * radius
    if y <= -yborder:
        y = -yborder + 2 * radius
    if y >= yborder:
        y = yborder - 2 * radius

    # Set the matrix for the object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def bounce():
    global x, y, hvel, vvel, radius
    glClear(GL_COLOR_BUFFER_BIT)

    # changes x and y
    x += hvel
    y += vvel

    # Keep the motion mathematics safe from harm and then move tha ball based on x and y
    glPushMatrix()
    glTranslate(x, y, 0)
    glutSolidSphere(radius, 16, 16)
    glPopMatrix()

    # Collision detection!
    if x >= xborder - radius or x <= -xborder + radius:
        hvel = -hvel
    if y >= yborder - radius or y <= -yborder + radius:
        vvel = -vvel
    glutSwapBuffers()


def keyboard(key, x, y):
    global anim
    key = key.decode('utf-8')
    if key == chr(27):
        sys.exit()
    elif key == 'a':
        anim = True
    elif key == 's':
        anim = False


def special_key(key, x, y):
    global hvel, vvel
    if key == GLUT_KEY_LEFT:
        hvel -= 0.001
    if key == GLUT_KEY_RIGHT:
        hvel += 0.001
    if key == GLUT_KEY_UP:
        vvel += 0.001
    if key == GLUT_KEY_DOWN:
        vvel -= 0.001


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow('PyBounce'.encode('utf-8'))
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    glutSpecialFunc(special_key)
    init()
    glutMainLoop()


main()
