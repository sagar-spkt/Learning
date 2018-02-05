from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


class Draw:
    def draw_func(self):
        pass

    def draw(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(50, 50)
        glutCreateWindow(b'Plot')
        glutDisplayFunc(self.draw_func)
        glClearColor(0, 0, 0, 1)
        gluOrtho2D(0, 500, 0, 500)
        glutMainLoop()
