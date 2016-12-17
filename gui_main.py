from OpenGL.GLUT import *
from OpenGL.GL import *
from background import run
import argparse, sys
width, height = 800, 600

colors_to_randomize = {
    'R': False,
    'G': False,
    'B': False
}

random_factor = 0

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
    
    sc = run(width, height, colors_to_randomize, float(random_factor))
    
    glEnd()
    glFlush()
    glutSwapBuffers()


def init():
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0.0, width, height, 0.0, -5.0, 5.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


if __name__ == '__main__':
    checkArgs()

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Projeto - PG 2')
    glutDisplayFunc(render)
    glClearColor(0, 0, 0, 0)
    init()
    glutMainLoop()