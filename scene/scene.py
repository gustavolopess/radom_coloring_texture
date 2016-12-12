# -*- coding: utf-8 -*-
import numpy as np
from config import Settings
from operations import vector

settings = Settings()

class Scene(object):
    """docstring for Scene"""

    def __init__(self, calice_input, ilumination_input):
        super(Scene, self).__init__()
        self.points = []
        self.triangles = []
        self.points_normal = []
        self.triangles_normal = []
        self.view_coordinates = []
        self.screen_coordinates = []
        self.random_factor = 0.0
        self.n_factor = 0.0
        self.pl = 0.0
        self.ka = 0.0
        self.ia = 0.0
        self.kd = 0.0
        self.od = 0.0
        self.ks = 0.0
        self.il = 0.0

        self.load_vertices(calice_input)
        self.load_ilumination(ilumination_input)

    def load_vertices(self, calice_input):
        with open(calice_input) as calice_config:
            lines = calice_config.readlines()

        number_points = int(lines[0].split(" ")[0])
        triangles = int(lines[0].split(" ")[1])

        for x in range(1, number_points + 1):
            self.points.append(np.array([
                float(lines[x].splitlines()[0].split(" ")[0]),
                float(lines[x].splitlines()[0].split(" ")[1]),
                float(lines[x].splitlines()[0].split(" ")[2])
            ]))

            self.points_normal.append(np.array([0.0, 0.0, 0.0]))

        for x in range(number_points + 1, len(lines)):
            self.triangles.append(np.array([
                int(lines[x].splitlines()[0].split(" ")[0]),
                int(lines[x].splitlines()[0].split(" ")[1]),
                int(lines[x].splitlines()[0].split(" ")[2])
            ]))


    def load_ilumination(self, ilumination_input):
        '''Carrega os dados de illuminação'''
        with open(ilumination_input, 'r') as illumination:
            lines = illumination.readlines()
            self.n_factor = float(lines[-1])
            self.pl = np.array([float(lines[0].split(" ")[0]),
                                float(lines[0].split(" ")[1]),
                                float(lines[0].split(" ")[2])
                                ])
            self.ka = float(lines[1])
            self.ia = np.array([float(lines[2].split(" ")[0]),
                                float(lines[2].split(" ")[1]),
                                float(lines[2].split(" ")[2])
                                ])
            self.kd = float(lines[3])
            self.od = np.array([float(lines[4].split(" ")[0]),
                                float(lines[4].split(" ")[1]),
                                float(lines[4].split(" ")[2])
                                ])
            self.ks = float(lines[5])
            self.il = np.array([float(lines[4].split(" ")[0]),
                                float(lines[4].split(" ")[1]),
                                float(lines[4].split(" ")[2])
                                ])


    '''a iluminação de phong é caracterizada pela junção dos vetores de iluminação
    de ambiente, difusa e especular'''
    def pixel_phong_ilumination(self, focused_px, N, V):
        lightDir = self.pl - focused_px
        lightDir = -vector.normalize(lightDir)
        normal = vector.normalize(N)
        viewDir = vector.normalize(V)





    def illumination_values(self):
        '''função de depuração só pra checar se os valores recebidos estão corretos'''
        print self.pl
        print self.ka
        print self.ia
        print self.kd
        print self.od
        print self.ks
        print self.il
        print self.n_factor