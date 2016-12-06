# -*- coding: utf-8 -*-
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
        print self.UVN_matrice


    '''retorna o ponto p no sistema de coordenadas da camera (SCC)'''
    def toSCC(self, p):
        p = np.array(p)
        return np.dot(self.UVN_matrice, p)


    '''converte um ponto (x,y,z) num ponto (x,y) equivalente à projeção ortográfica do ponto no plano'''
    @staticmethod
    def toOrthoProj(p):
        p = np.array(p)
        homog = np.array([1])
        p = np.concatenate([p, homog])

        transf_matrice = np.array([[1, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 0],
                                   [0, 0, 1]])

        return np.dot(transf_matrice, p)




def usage():
    cam = Camera([1,2,3], [3, 2, 1])



if __name__ == '__main__':
    usage()
