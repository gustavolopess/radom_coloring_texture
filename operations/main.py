# -*- coding: utf-8 -*-
import numpy as np
import Scene
import camera
import vector
from settings import debug


def create_camera_and_start_camera():
    '''Carrega as da camera'''

    with open("input/camera.txt", 'r') as camera_config:
        configs = camera_config.readlines()

    camera_position = np.array([float(configs[0].split(" ")[0]),
                                float(configs[0].split(" ")[1]),
                                float(configs[0].split(" ")[2])
                                ])

    camera_n = np.array([float(configs[1].split(" ")[0]),
                         float(configs[1].split(" ")[1]),
                         float(configs[1].split(" ")[2])
                         ])

    camera_v = np.array([float(configs[2].split(" ")[0]),
                         float(configs[2].split(" ")[1]),
                         float(configs[2].split(" ")[2])
                         ])

    camera_d = float(configs[3].split(" ")[0])
    camera_hx = float(configs[3].split(" ")[1])
    camera_hy = float(configs[3].split(" ")[2])

    cam = camera.Camera(camera_position, camera_n, camera_v,
                        camera_d, camera_hx, camera_hy, 800, 600)

    return cam

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
    sc = Scene.Scene()
    sc.load_illumination_points_triangles_color()

    if debug:
        print "#" * 50
        print "LUMINOSITY INPUTS"
        sc.illumination_values()
        print "#" * 50
    print("(1) - Points and Triangles fully loaded.")

    # Load Camera Atributes
    cam = create_camera_and_start_camera()
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

        normalized_normal = vector.normalize(normal)
        sc.triangles_normal.append(normalized_normal)

        sc.points_normal[p1] += normalized_normal
        sc.points_normal[p2] += normalized_normal
        sc.points_normal[p3] += normalized_normal

    normalyzed_points_normal = []

    for n in sc.points_normal:
        normalyzed_points_normal.append(vector.normalize(n))

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
