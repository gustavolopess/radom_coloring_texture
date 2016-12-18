from OpenGL.raw.GLUT import glutBitmapCharacter

from OpenGL.raw.GLUT.constants import GLUT_RGB

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from background import run
import argparse, sys
from config import Settings
width, height = 800, 600

settings = Settings()

colors_to_randomize = {
    'R': False,
    'G': False,
    'B': False
}

random_factor = 0

window = None


PROMPT = ("ESC - EXIT","C - CHANGE OBJECT FILE")

def checkArgs():
    global colors_to_randomize, random_factor

    parser = argparse.ArgumentParser(description="random texture through coloring")
    parser.add_argument('random_factor', metavar='F', help='random factor (between 0 and 1)')
    parser.add_argument('--colors', metavar='C', default='RGB', help='type colors which must be randomized (e.g: RGB)')

    args = parser.parse_args()

    if not (0 <= float(args.random_factor) <= 1):
        print "Invalid arg %r (must be in [0, 1] interval)" % args.random_factor
        print "type python %s -h for informations." % sys.argv[0]
        sys.exit(1)

    for c in args.colors:
        if str(c).upper() not in ['R', 'G', 'B']:
            print "Invalid arg %r (option %r doesn't exist)" % (args.colors, c)
            print "type python %s -h for informations." % sys.argv[0]
            sys.exit(1)
        colors_to_randomize[str(c).upper()] = True

    random_factor = args.random_factor


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 1.0)

    sc = run(width, height, colors_to_randomize, float(random_factor), settings)

    glEnd()
    glFlush()
    glutSwapBuffers()


def change_object():
    global settings
    new_path = raw_input()
    settings.object_input = new_path
    glutPostRedisplay()


def init():
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0.0, width, height, 0.0, -5.0, 5.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':
    checkArgs()

    print "To change the object input you must type the path to object's file"
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow('Projeto - PG 2')

    glutDisplayFunc(render)
    glutIdleFunc(change_object)

    glClearColor(1, 1, 1, 1)
    init()
    glutMainLoop()