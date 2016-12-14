from OpenGL.GLUT import *
from OpenGL.GL import *
from background import run
width, height = 800, 600

# points = sc.screen_coordinates

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 1.0)
    
    sc = run(width, height)
    
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
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Projeto - PG 2')
    glutDisplayFunc(render)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    init()
    glutMainLoop()