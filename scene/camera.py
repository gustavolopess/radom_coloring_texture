# -*- coding: utf-8 -*-
import numpy as np
import operations.vector
from config import Settings

settings = Settings()

class Camera(object):

    def __init__(self, camera_input, width=800, height=600):
        super(Camera, self).__init__()

        with open(camera_input, 'r') as camera_config:
            configs = camera_config.readlines()

        self.camera_position = np.array([float(configs[0].split(" ")[0]),
                                    float(configs[0].split(" ")[1]),
                                    float(configs[0].split(" ")[2])
                                    ])

        self.camera_n = np.array([float(configs[1].split(" ")[0]),
                             float(configs[1].split(" ")[1]),
                             float(configs[1].split(" ")[2])
                             ])

        self.camera_v = np.array([float(configs[2].split(" ")[0]),
                             float(configs[2].split(" ")[1]),
                             float(configs[2].split(" ")[2])
                             ])

        self.d = float(configs[3].split(" ")[0])
        self.hx = float(configs[3].split(" ")[1])
        self.hy = float(configs[3].split(" ")[2])

        self.N = operations.vector.normalize(self.camera_n)
        self.V = operations.vector.normalize(
            self.camera_v - operations.vector.grand_schimidt(self.camera_v, self.N))
        self.U = np.cross(self.N, self.V)
        self.UVN_matrice = np.array([self.U, self.V, self.N])

        self.width = width
        self.height = height

        if settings.debug:
            print "#" * 50
            print "UVN MATRIX"
            print self.UVN_matrice
            print "#" * 50
            print

    '''retorna o ponto p no sistema de coordenadas da camera (camera_coordinate_system)'''
    def to_view_coordinate_system(self, p):
        point = np.array([0.0,0.0,0.0])
        point[0] = p[0] - self.camera_position[0]
        point[1] = p[1] - self.camera_position[1]
        point[2] = p[2] - self.camera_position[2]

        result = np.array([self.UVN_matrice[0][0] * point[0] + self.UVN_matrice[0][1] * point[1] + self.UVN_matrice[0][2] * point[2],
                            self.UVN_matrice[1][0] * point[0] + self.UVN_matrice[1][1] * point[1] + self.UVN_matrice[1][2] * point[2],
                            self.UVN_matrice[2][0] * point[0] + self.UVN_matrice[2][1] * point[1] + self.UVN_matrice[2][2] * point[2]])

        return result

    def to_screen_coordinate_system(self, p):
        '''calculate projection coordinates'''
        x = float(self.d / self.hx) * float(p[0] / p[2])
        y = float(self.d / self.hy) * float(p[1] / p[2])
        '''convert to screen'''
        screen_coord = np.array(
            [(int)(((x + 1)  * (self.width/ 2))),
             (int)(((1 - y) * (self.height/ 2)))]
        )

        return screen_coord

    def get_triangle_normal(self, p1, p2, p3):
        v1 = p2 - p1
        v2 = p3 - p1

        return np.cross(v1, v2)



