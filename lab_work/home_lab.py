from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import speech_recognition as sr
import sys

# Window size
width = height = 600
auto_rotate = False


def listen():
    mic_name = 'Microphone (WO Mic Device)'

    sample_rate = 48000

    chunk_size = 2048

    r = sr.Recognizer()

    mic_list = sr.Microphone.list_microphone_names()

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said: " + text)
            return text

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results")


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


def auto():
    global auto_rotate
    auto_rotate = not auto_rotate


def zap():
    # Camera position
    global camx, camy, camz, angh, angv
    camx = camy = camz = 5
    angh = angv = 0


def plot_func():
    global angh
    if auto_rotate:
        t = glutGet(GLUT_ELAPSED_TIME) / 1000
        angh = (t * 30) % 360
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(angh, 0, 0, 1)
    glRotate(angv, 1, 0, 0)
    # glTranslate(0, angh/100, 0)

    # Main block
    glPushMatrix()
    glScale(1, 2, 1.5)
    glColor3f(0.35, 0.83, 0.47)
    glutSolidCube(1)
    glPopMatrix()

    # Paali
    glPushMatrix()
    glRotate(15, 0, 1, 0)
    glTranslate(0.692, 0, 0.16)
    glScale(0.4, 2, 0.01)
    glColor3f(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

    # Peti
    glPushMatrix()
    glTranslate(0.7, 0, -0.725)
    glScale(0.4, 2, 0.05)
    glColor3f(1, 1, 0)
    glutSolidCube(1)
    glPopMatrix()

    # Base
    glPushMatrix()
    glTranslate(0.8, 0.4, -0.76)
    glScale(3, 3.5, 0.02)
    glColor3f(0.97, 0.43, 0.47)
    glutSolidCube(1)
    glPopMatrix()

    # Chhano front
    glPushMatrix()
    glTranslate(0.3267, 0, 0.8956)
    glRotate(40, 0, 1, 0)
    glScale(0.853, 2.15, 0.01)
    glColor3f(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

    # Chhano back
    glPushMatrix()
    glTranslate(-0.3267, 0, 0.8956)
    glRotate(140, 0, 1, 0)
    glScale(0.853, 2.15, 0.01)
    glColor3f(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

    # Door
    glPushMatrix()
    glTranslate(0.5, 0, -0.380)
    glScale(0.0001, 0.2, 0.60)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()

    # Lower window
    glPushMatrix()
    glTranslate(0.5, 0.5, -0.379)
    glScale(0.0001, 0.2, 0.30)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslate(0.5, -0.5, -0.379)
    glScale(0.0001, 0.2, 0.30)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()

    # Window
    glPushMatrix()
    glTranslate(0.5, 0, 0.280)
    glScale(0.0001, 0.2, 0.40)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslate(0.5, 0.5, 0.280)
    glScale(0.0001, 0.2, 0.40)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslate(0.5, -0.5, 0.280)
    glScale(0.0001, 0.2, 0.40)
    glColor3f(0, 0, 1)
    glutSolidCube(1)
    glPopMatrix()

   

    glPopMatrix()
    glutSwapBuffers()


def keyboard(key, x, y):
    global auto_rotate
    key = key.decode('utf-8')
    if key == chr(27):
        sys.exit()
    if key == 'z':
        zap()
    if key == 'a' or key == 'A':
        text = listen()
        if text == 'spin':
            auto_rotate = True
        elif text == 'stop':
            auto_rotate = False
        # auto()


def special_key(key, x, y):
    global angh, angv
    if key == GLUT_KEY_LEFT:
        angh = (angh + 1) % 360
    if key == GLUT_KEY_RIGHT:
        angh = (angh - 1) % 360
    if key == GLUT_KEY_UP:
        angv = (angv + 1) % 360
    if key == GLUT_KEY_DOWN:
        angv = (angv - 1) % 360


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
