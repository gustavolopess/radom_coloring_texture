# -*- coding: utf-8 -*-
import numpy as np

import operations.vector
from operations.triangle import Triangle
from config import Settings
from scene import scene
from scene.camera import Camera
import logging

from OpenGL.GLUT import *
from OpenGL.GL import *

# if __name__ == '__main__':
def run(width, height):
    
    settings = Settings()
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    info = logging.info
    '''Recebe o fator de aleatorização da textura aleatoria do usuario bem como os canais'''
    # fator_aleatorizacao = -1

    # while fator_aleatorizacao < 0.0 or fator_aleatorizacao > 1.0:
    #     fator_aleatorizacao = float(raw_input(
    #         "Insira o fator de aleatorização, entre 0 e 1:\n"))

    # canais = raw_input(
    #     "Insira os canais que deseja aleatorizar separados por espaço ex:R G B ou R B\n")

    # red = False
    # green = False
    # blue = False

    # # Definindo os canais de aleatorização
    # if "R" in canais:
    #     red = True

    # if "G" in canais:
    #     green = True

    # if "B" in canais:
    #     blue = True

    # print "Aleatorização definida para: ", red, green, blue
    '''passos:'''
    info("1) camera")
    info("\t1.1) normalizar N")
    info("\t1.2) V = V - proj N (V)")
    info("\t1.3) U = N x V")
    info("\t1.4) alfa = UNV = {U, N, V}")
    cam = Camera(settings.camera_input)


    info("2) cena")
    sc = scene.Scene(settings.calice_input, settings.iluminacao_input)

    info("\t2.1) passar a posição da fonte de luz de coordenadas de mundo para coordenadas de vista")
    pl_view = cam.to_view_coordinate_system(sc.pl)
    
    if settings.debug:
        print "#" * 50
        print "\nLight Position: ", pl_view, "\n"
        print "#" * 50
        

    info("\t2.2) para cada ponto do objeto, projete-o para coordenadas de vista")
    points_view = []
    for p in sc.points:
        points_view.append(cam.to_view_coordinate_system(p))
    sc.view_coordinates = points_view
    
    # with open("value_view.txt", 'w') as view_txt:
    #     for p in sc.view_coordinates:
    #         view_txt.write("%s, %s, %s\n"%(p[0], p[1], p[2]))

    info("\t2.3) inicializar as normais de todos os pontos do objeto com zero")
    info("\t2.4) para cada triângulo calcular a normal do triângulo e normalizá-la. somar ela à normal\
    de cada um dos 3 pontos (vértices do triângulo) e cria os Triangulos com vertices em coordenada de vista")

    for t in sc.triangles:
        p1, p2, p3 = sc.view_coordinates[t[0] - 1], sc.view_coordinates[t[1] - 1], sc.view_coordinates[t[2] - 1]

        tr_normal = cam.get_triangle_normal(p1, p2, p3)
        tr_normal = operations.vector.normalize(tr_normal)
        
        sc.triangles_view_objects.append(Triangle(p1, p2, p3, tr_normal))  
        
        sc.points_normal[t[0] - 1] += tr_normal
        sc.points_normal[t[1] - 1] += tr_normal
        sc.points_normal[t[2] - 1] += tr_normal

    info("\t2.5) normalizar todas as normais")
    normalized_points_normal = []
    for pn in sc.points_normal:
        normalized_points_normal.append(operations.vector.normalize(pn))
    sc.points_normal = normalized_points_normal

    info("\t2.6) Inicializa z-buffer.")

    sc.init_zbuffer(width, height)

    info("\t2.6) para cada ponto do obj, projete-o para coord de tela 2D, sem descartar os pontos em coord 3D")
    view_2d = []
    for vp in sc.view_coordinates:

        view_2d.append(cam.to_screen_coordinate_system(vp))
    sc.screen_coordinates = view_2d

    # with open("value_screen.txt", 'w') as view_txt:
    #     for p in sc.screen_coordinates:
    #         view_txt.write("%s, %s\n"%(p[0], p[1]))

    info("\t2.7) Cria os Triangulos em coordenada de Tela")
    sc.create_triangle_screen_objects()
    
    info("\t2.7) Realiza a varredura nos triangulos em coordenada de tela.")
    sc.call_triangle_rasterization()
    
    return sc