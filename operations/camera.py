import numpy as np
import vector

class Camera(object):
    def __init__(self, camera_target, camera_up):
        super(Camera, self).__init__()

        #conversao preventiva
        camera_target, camera_up = np.array(camera_target), np.array(camera_up)

        self.N = vector.normalize(camera_target)
        self.U = np.cross(vector.normalize(camera_up), camera_target)
        self.V = np.cross(self.N, self.U)

        self.UVN_matrice = np.array([self.U, self.V, self.N])






def usage():
    cam = Camera([1,2,3], [3, 2, 1])



if __name__ == '__main__':
    usage()