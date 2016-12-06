# -*- coding: utf-8 -*- 
import numpy as np
import vector

class Camera(object):
    def __init__(self, camera_c, camera_n, camera_v, d, hx, hy):
        super(Camera, self).__init__()

        self.N = vector.normalize(camera_n)
        self.V = vector.normalize(camera_v - vector.grand_schimidt(camera_v, self.N))
        self.U = np.cross(self.N, self.V)
        self.UVN_matrice = np.array([self.U, self.V, self.N])

        print ("(2) - Camera fully loaded")
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
