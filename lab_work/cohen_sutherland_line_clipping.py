from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

xmin, ymin, xmax, ymax = -300, -300, 300, 300
xd1 = yd1 = xd2 = yd2 = None
LEFT_EDGE, RIGHT_EDGE, BOTTOM_EDGE, TOP_EDGE = 0x1, 0x2, 0x4, 0x8


def INSIDE(a):
    return not a


def REJECT(a, b):
    return a & b


def ACCEPT(a, b):
    return not (a | b)


def encode(x, y):
    code = 0x00
    if x < xmin:
        code = code | LEFT_EDGE
    if x > xmax:
        code = code | RIGHT_EDGE
    if y < ymin:
        code = code | BOTTOM_EDGE
    if y > ymax:
        code = code | TOP_EDGE
    return code


def init():
    glClearColor(0, 0, 0, 0)
    # glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-600, 600, -600, 600)


def display():
    global xd1, yd1, xd2, yd2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)

    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmin, ymax)
    glVertex2f(xmax, ymax)
    glVertex2f(xmax, ymin)
    glEnd()

    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(xd1, yd1)
    glVertex2f(xd2, yd2)
    glEnd()
    glFlush()


def cohen_line(x1, y1, x2, y2):
    global xd1, yd1, xd2, yd2
    code1, code2 = None, None
    done = draw = False
    slope = None

    while not done:
        code1 = encode(x1, y1)
        code2 = encode(x2, y2)

        if ACCEPT(code1, code2):
            done = True
            draw = True
        else:
            if REJECT(code1, code2):
                done = True
            else:
                if INSIDE(code1):
                    # swap coordinates and codes
                    x1, y1, x2, y2 = x2, y2, x1, y1
                    code1, code2 = code2, code1
                if x2 != x1:
                    slope = (y2 - y1) / (x2 - x1)
                if code1 & LEFT_EDGE:
                    y1 += (xmin - x1) * slope
                    x1 = xmin
                else:
                    if code1 & RIGHT_EDGE:
                        y1 += (xmax - x1) * slope
                        x1 = xmax
                    else:
                        if code1 & BOTTOM_EDGE:
                            if x2 != x1:  # No need to update x for vertical lines
                                x1 += (ymin - y1) / slope
                            y1 = ymin
                        else:
                            if code1 & TOP_EDGE:
                                if x2 != x1:  # No need to update x for vertical lines
                                    x1 += (ymax - y1) / slope
                                y1 = ymax
    if draw:
        xd1, yd1, xd2, yd2 = x1, y1, x2, y2
    else:
        xd1, yd1, xd2, yd2 = 0, 0, 0, 0
    display()


def key_function(key, x, y):
    global xd1, yd1, xd2, yd2
    key = key.decode('utf-8')
    if key == 'c':
        print("Line Clipped")
        cohen_line(xd1, yd1, xd2, yd2)
        glFlush()
    if key == chr(27):
        sys.exit()


def main():
    global xd1, yd1, xd2, yd2
    xd1, yd1, xd2, yd2 = tuple(map(int, input('Enter 2 end points: ').strip().split()))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b'Cohen_Sutherland')
    glutDisplayFunc(display)
    glutKeyboardFunc(key_function)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
