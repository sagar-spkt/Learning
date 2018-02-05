from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

global width
global height
global hcenter
global vcenter
global axrng
global hstep
global vstep
global yinit
global xinit
global mandel
global tmprng
global julhcenter
global julvcenter
global julflag
global julx
global july

width = 400
height = 400

mandel = 1


def init():
    global hcenter
    global vcenter
    global axrng
    global hstep
    global vstep
    global yinit
    global xinit
    global yfinal
    global xfinal
    global mandel
    global julhcenter
    global julvcenter

    glClearColor(0.0, 0.0, 0.0, 0.0)
    hstep = 2 * axrng / (width + 1)
    vstep = 2 * axrng / (height + 1)

    if mandel == 1:
        yinit = vcenter + axrng
        xinit = hcenter - axrng
        yfinal = vcenter - axrng
        xfinal = hcenter + axrng
    else:
        yinit = julvcenter + axrng
        xinit = julhcenter - axrng
        yfinal = julvcenter - axrng
        xfinal = julhcenter + axrng

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xinit, xfinal, yfinal, yinit)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


def keyboard(key, x, y):
    key = key.decode('utf-8')
    global mandel
    global tmprng
    global axrng
    global hcenter
    global vcenter
    global julflag
    if mandel == 1:
        tmprng = axrng
    if key == chr(27):
        sys.exit()
    if key == "z":
        zap()
    if key == "j":
        mandel = 0
        axrng = 2.0
    if key == "m":
        mandel = 1
        axrng = tmprng
        julflag = 0
        init()
    if key == "q":
        sys.exit()


def zap():
    # Reset everything
    global hcenter
    global vcenter
    global axrng
    global mandel
    global julflag
    hcenter = 0.0
    vcenter = 0.0
    axrng = 2.0
    mandel = 1
    julflag = 0
    init()

def drawmandel():
    glClear(GL_COLOR_BUFFER_BIT)
    y = yinit
    # toggle Julia Set or M-Set
    # mandel == 0 is the Julia Set
    # julx and july contain the Julia Set
    # seed coordinates
    if mandel == 0:
        a = complex(julx, july)
    while y > yfinal:
        y-= vstep
        x = xinit
        while x < xfinal:
            x+=hstep
            n = 0
            # Choose M-Set or Julia Set
            # If Julia Set is toggled, “a” already contains
            # the complex number seed
            if mandel == 1:
                z = a = complex(x, y)
            else:
                z = complex(x, y)
            # Escape time… increase this value above 25
            # for a more detailed plot. Decrease
            # this value for more speed.
            while n < 25:
                n += 1
                z = z ** 2 + a
                zz = abs(z)
                # This is the escape distance. For some
                # M-Set/Julia Sets such as sin() or exp() you
                # may need to set this value higher than 2
                # 50 works well for sin() functions
                if zz > 2:
                    # Weird colors outside the M-Set
                    # glColor3f(3*sin(3*z.real),cos(3*z.real),4*cos(zz))
                    # glBegin(GL_POINTS)
                    # glVertex2f(x,y)
                    # glEnd()
                    # glFlush()
                    n = 5001
            # The same goes for this zz < 2 statement as above
            if zz < 2:
                # Coloration inside the M-Set
                glColor3f(3 * sin(3 * zz), cos(3 * z.real), 2 * sin(zz))
                glBegin(GL_POINTS)
                glVertex2f(x, y)
                glEnd()
                glFlush()


def mouse(button, state, x, y):
    global hcenter
    global vcenter
    global axrng
    global julhcenter
    global julvcenter
    global julflag
    global julx
    global july
    # Detect the left/right mouse buttons and the click
    # Followed by resetting the origin
    # Left mouse button zooms in, right button zooms out
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if mandel == 1:
            hcenter = xinit + (xfinal - xinit) * x / width
            vcenter = yinit + (yfinal - yinit) * y / height
            axrng = axrng / 2
            init()
    else:
        # We use different center point variables here
        # to keep the Julia Set and M-Set calculations
        # separate
        julhcenter = xinit + (xfinal - xinit) * x / width
        julvcenter = yinit + (yfinal - yinit) * y / height
        # We use a flag variable here so that the first
        # Julia Set plot is normal size regardless of the
        # Zoom factor on the M-Set. We don’t want to
        # cause a zoom on the first Julia Set
        if julflag == 0:
            # Print the value of the Julia Set seed
            print
            "Julia", julhcenter, julvcenter
            # Store the pixel coordinates in julx and july
            # for the Julia Set seed
            julx = julhcenter
            july = julvcenter
            # Set the following variables to zero
            # so the first Julia Set is centered in
            # the graphics display window
            julhcenter = 0.0
            julvcenter = 0.0
            # Show the Julia Set!
            init()
        else:
            # NOW we can zoom on the Julia Set
            julhcenter = xinit + (xfinal - xinit) * x / width
            julvcenter = yinit + (yfinal - yinit) * y / height
            axrng = axrng / 2
            init()
        # Set the flag so subsequent mouse clicks zoom
        # into the Julia Set
        julflag = 1
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # This section is similar to the previous
        # Section except that here we zoom out!
        if mandel == 1:
            hcenter = xinit + (xfinal - xinit) * x / width
            vcenter = yinit + (yfinal - yinit) * y / height
            axrng = 2 * axrng
            init()
        else:
            julhcenter = xinit + (xfinal - xinit) * x / width
            julvcenter = yinit + (yfinal - yinit) * y / height
            # Again, we don't want to initially zoom into
            # the Julia Set... we want a "normal" Julia First
            if julflag == 0:
                print("Julia", julhcenter, julvcenter)
                julx = julhcenter
                july = julvcenter
                julhcenter = 0.0
                julvcenter = 0.0
                init()
            else:
                julhcenter = xinit + (xfinal - xinit) * x / width
                julvcenter = yinit + (yfinal - yinit) * y / height
                axrng = 2 * axrng
                init()
            julflag = 1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Mandelbrot Set")
    glutDisplayFunc(drawmandel)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    zap()
    glutMainLoop()

main()