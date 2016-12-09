from OpenGL.GLUT import *
from OpenGL.GL import *
width, height = 800, 600

points = []

def render():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(13.0)
    glBegin(GL_POINTS)

    glColor3f(0.0, 1.0, 1.0)
    print points
    for p in points:
        glVertex2f(p[0], p[1])

    glEnd()
    glFlush()
    glutSwapBuffers()


def mouse_handle(button, state, x, y):
    global points
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            points.append((float(x), float(height - y)))

        elif button == GLUT_RIGHT_BUTTON:
            try:
                points.pop()
            except:
                pass

        glutPostRedisplay()


def init():
    # glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0.0, float(width), 0.0, float(height), 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Testing')
    glutDisplayFunc(render)
    glutMouseFunc(mouse_handle)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    init()
    glutMainLoop()