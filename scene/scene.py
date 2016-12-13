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
    '''
        | ; Pl - Posicao da luz em coordenadas de mundo
        | ; ka - reflexao ambiental
        | ; Ia - vetor cor ambiental
        | ; kd - constante difusa
        | ; Od - vetor difuso
        | ; ks - parte especular
        | ; Il - cor da fonte de luz
        | ; n  - constante de rugosidade
    '''
    '''
        final_color = ambient_component + diffuse_component + specular_component
    '''

    def pixel_phong_ilumination(self, focused_px, N, V):
        saturate = lambda x: max(0, min(1, x))

        L = -vector.normalize(self.pl - focused_px)
        N = vector.normalize(N)
        NL = saturate(np.dot(N, L))
        R = vector.normalize(2 * NL * N - L)
        RV = saturate(np.dot(R, V))

        ambient_component = self.ka * self.ia
        diffuse_component = self.kd*NL
        specular_component = self.ks*pow(RV, self.n_factor)

        color = self.od*ambient_component + self.od*(self.il*(diffuse_component + specular_component))

        final_color = np.array([ int(color[0]%255), int(color[1]%255), int(color[2]%255) ])
        return final_color


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
