# -*- coding: utf-8 -*-
import numpy as np
from config import Settings
from operations import vector
from operator import itemgetter
from operations.triangle import Triangle

from OpenGL.GLUT import *
from OpenGL.GL import *

settings = Settings()

class Scene(object):
    """docstring for Scene"""

    def __init__(self, calice_input, ilumination_input):
        super(Scene, self).__init__()
        
        self.r = 0
        self.t = 0

        self.points = []
        self.triangles = []
        self.triangles_view_objects = []
        self.triangles_screen_objects = []
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


        self.z_buffer = []
        self.load_vertices(calice_input)
        self.load_ilumination(ilumination_input)

    def init_zbuffer(self, height, width):
        self.z_buffer = np.array([[99999999]*height for i in range(0, width)])

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

    def create_triangle_screen_objects(self):
        for t in self.triangles:
            p1, p2, p3 = self.screen_coordinates[t[0] - 1], self.screen_coordinates[t[1] - 1], self.screen_coordinates[t[2] - 1]
            self.triangles_screen_objects.append(Triangle(p1, p2, p3))

    def call_triangle_rasterization(self):
        for t in self.triangles_screen_objects:  
            self.draw_triangle_rasterization(t.v1, t.v2, t.v3)


    def draw_triangle_rasterization(self, p1, p2, p3):
        l = sorted((p1, p2, p3), key=itemgetter(1))
        #   /* here we know that v1.y <= v2.y <= v3.y */
        
        # Caso dos vertices serem colineares. (acho que nem deveria existir, mas sem ele nao funciona) 
        if l[0][1] == l[1][1] and l[0][1] == l[2][1]:
            list_x_sorter = sorted((p1, p2, p3), key=itemgetter(0))
            self.r+=1
            for x in range(list_x_sorter[0][0], list_x_sorter[2][0]+1):
                glVertex2f(x, l[0][1])

        elif l[1][1] == l[2][1]:
            self.fill_bottom_flat_triangle(l[0], l[1], l[2])
            self.t+=1
        elif l[0][1] == l[1][1]:
            self.fill_top_flat_triangle(l[0], l[1], l[2])
            self.t+=1
        else:
            p4 = np.array([int(l[0][0] + (float(l[1][1] - l[0][1]) / float(l[2][1] - l[0][1])) * (l[2][0] - l[0][0])), int(l[1][1])])
            self.t+=1
            self.fill_bottom_flat_triangle(l[0], l[1], p4)
            self.fill_top_flat_triangle(l[1], p4, l[2])

        # print self.r, self.t


    def fill_bottom_flat_triangle(self, v1, v2, v3):
        invslope1 = float(v2[0] - v1[0]) / (v2[1] - v1[1])
        invslope2 = float(v3[0] - v1[0]) / (v3[1] - v1[1])

        curx1 = float(v1[0])
        curx2 = float(v1[0]) + 0.5

        if invslope1 > invslope2:
            aux = invslope1
            invslope1 = invslope2
            invslope2 = aux

        scanlineY = v1[1]
        scanlineY_max = v2[1]

        for vy in range(int(scanlineY), int(scanlineY_max)):
            for vx in range(int(curx1), int(curx2)):
                glColor3f(1,1,1)
                glVertex2f(vx, vy)

            curx1 += invslope1
            curx2 += invslope2

    def fill_top_flat_triangle(self, v1, v2, v3):

        invslope1 = float(v3[0] - v1[0]) / (v3[1] - v1[1])
        invslope2 = float(v3[0] - v2[0]) / (v3[1] - v2[1])

        curx1 = float(v3[0])
        curx2 = float(v3[0]) + 0.5

        if invslope1 < invslope2:
            aux = invslope1
            invslope1 = invslope2
            invslope2 = aux

        scanlineY = v3[1]
        scanlineY_max = v1[1]
          
        for vy in range(int(scanlineY), int(scanlineY_max), -1):
            for vx in range(int(curx1), int(curx2)):
                glColor3f(1,1,1)
                glVertex2f(vx, vy)
            
            curx1 -= invslope1
            curx2 -= invslope2
