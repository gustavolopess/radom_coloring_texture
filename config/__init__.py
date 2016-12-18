from OpenGL.raw.GLUT import glutPostRedisplay
from OpenGL.GLUT import *
from OpenGL.GL import *

class Settings:
    def __init__(self):
        # debug boolean
        self.debug = True

        # camera input
        self.camera_input = 'input/camera/calice2.cfg'
        # self.camera_input = 'input/vader_camera.txt'
        self.object_input = 'input/calice2.byu'
        # self.calice_input = 'input/vader_object.txt'
        self.iluminacao_input = 'input/iluminacao.txt'

