from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, pi
from OpenGL.GLUT import *
import sys

# global horiz_vel, vert_vel


def init():
    global horiz_vel, vert_vel
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-200, 12000, -200, 5000)
    angle = float(input('Enter the angle of elevation: '))
    muzz_vel = float(input('Enter the muzzle velocity of the shell: '))
    rad_angle = angle*pi/180
    horiz_vel = muzz_vel*cos(rad_angle)
    vert_vel = muzz_vel*sin(rad_angle)
    print('Horizontal Velocity(m/s): ', horiz_vel)
    print('Vertical Velocity(m/s): ', vert_vel)


def plot_trajectory():
    global horiz_vel, vert_vel
    v_vel = vert_vel
    h_vel = horiz_vel
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)

    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(20000, 0)
    glVertex2f(0, 0)
    glVertex2f(0, 15000)
    glEnd()

    height = 500  # initial height of cannon
    d_time = 0.001
    dist = 0
    max_height = 0

    glBegin(GL_POINTS)
    while height > 0:
        dist += h_vel*d_time
        v_vel -= 9.8*d_time
        height += v_vel*d_time

        if max_height < height:
            max_height = height

        # glBegin(GL_POINTS)
        glVertex2f(dist, height)
    glEnd()
    glFlush()

    print('Distance travelled(m):', dist)
    print('Maximum altitude(m): ', max_height)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'How far it will go?')
    glutDisplayFunc(plot_trajectory)
    init()
    glutMainLoop()


main()
