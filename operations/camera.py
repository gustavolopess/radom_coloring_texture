# -*- coding: utf-8 -*-
import numpy as np
import vector
from settings import debug


class Camera(object):

    def __init__(self, camera_c, camera_n, camera_v, d, hx, hy, width, height):
        super(Camera, self).__init__()

        self.camera_position = camera_c
        self.d = d
        self.hx = hx
        self.hy = hy
        self.width = width
        self.height = height

        self.N = vector.normalize(camera_n)
        self.V = vector.normalize(
            camera_v - vector.grand_schimidt(camera_v, self.N))
        self.U = np.cross(self.N, self.V)
        self.UVN_matrice = np.array([self.U, self.V, self.N])

        if debug:
            print "#" * 50
            print "UVN MATRIX"
            print self.UVN_matrice
            print "#" * 50
            print

    '''retorna o ponto p no sistema de coordenadas da camera (camera_coordinate_system)'''

    def to_view_coordinate_system(self, p):
        point = p - self.camera_position
        return np.dot(self.UVN_matrice, point)

    def to_screen_coordinate_system(self, p):
        '''calculate projection coordinates'''
        x = (self.d / self.hx) * (p[0] / p[2])
        y = (self.d / self.hy) * (p[1] / p[2])

        '''convert to screen'''
        screen_coord = np.array(
            [(int)(((x + 1) / 2) * self.width),
             (int)(((1 - y) / 2) * self.height)]
        )
        return screen_coord

    def get_triangle_normal(self, p1, p2, p3):
        v1 = p2 - p1
        v2 = p3 - p1

        return np.cross(v1, v2)
