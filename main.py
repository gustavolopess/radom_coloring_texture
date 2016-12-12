# -*- coding: utf-8 -*-
import numpy as np

import operations.vector
from config import Settings
from scene import scene
from scene.camera import Camera

settings = Settings()

if __name__ == '__main__':

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

    '''Carrega as entradas e pinta os valores carregados'''
    sc = scene.Scene(settings.calice_input, settings.iluminacao_input)

    if settings.debug:
        print "#" * 50
        print "LUMINOSITY INPUTS"
        sc.illumination_values()
        print "#" * 50
    print("(1) - Points and Triangles fully loaded.")

    # Load Camera Atributes
    cam = Camera(settings.camera_input)
    print("(2) - Camera fully loaded")

    # Calculate new points for inputs and pl
    new_pl_view_coordinate = cam.to_view_coordinate_system(sc.pl)
    new_view_coordinates = []

    for p in sc.points:
        new_view_coordinates.append(cam.to_view_coordinate_system(p))

    sc.view_coordinates = new_view_coordinates
    print("(3) - Converted points to view coordinate system")

    p1 = sc.triangles[0][0]
    p2 = sc.triangles[0][1]
    p3 = sc.triangles[0][2]

    for t in sc.triangles:
        p1 = t[0] - 1
        p2 = t[1] - 1
        p3 = t[2] - 1
        normal = cam.get_triangle_normal(
            sc.points[p1], sc.points[p2], sc.points[p3])

        normalized_normal = operations.vector.normalize(normal)
        sc.triangles_normal.append(normalized_normal)

        sc.points_normal[p1] += normalized_normal
        sc.points_normal[p2] += normalized_normal
        sc.points_normal[p3] += normalized_normal

    normalyzed_points_normal = []

    for n in sc.points_normal:
        normalyzed_points_normal.append(operations.vector.normalize(n))

    sc.points_normal = normalyzed_points_normal
    print("(4) - Calculated points normals and triangles normals already normalyzed")

    screen_coord_list = []
    for vp in sc.view_coordinates:
        screen_coord_list.append(cam.to_screen_coordinate_system(vp))

    sc.screen_coordinates = screen_coord_list
    print("(5) - Calculated screen coordinates for object")

    # print sc.points_normal[0]
    # print len(sc.points_normal)
    # print sc.triangles_normal
    # print len(sc.triangles_normal)
