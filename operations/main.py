# -*- coding: utf-8 -*- 
import numpy as np
import Scene
import camera

def create_camera_and_start_camera():
    with open("input/camera.txt", 'r') as camera_config:
        configs = camera_config.readlines()

    camera_position = np.array([int(configs[0].split(" ")[0]), 
                                int(configs[0].split(" ")[1]), 
                                int(configs[0].split(" ")[2])
                                ])

    camera_n = np.array([int(configs[1].split(" ")[0]), 
                        int(configs[1].split(" ")[1]), 
                        int(configs[1].split(" ")[2])
                        ])

    camera_v = np.array([int(configs[2].split(" ")[0]), 
                        int(configs[2].split(" ")[1]), 
                        int(configs[2].split(" ")[2])
                        ])

    camera_d = float(configs[3].split(" ")[0])
    camera_hx = float(configs[3].split(" ")[1])
    camera_hy = float(configs[3].split(" ")[2])

    cam = camera.Camera(camera_position, camera_n, camera_v, camera_d, camera_hx, camera_hy)


if __name__ == '__main__':
    # Load Scene atributes 
    sc = Scene.Scene()
    sc.load_illumination_points_triangles_color()
    print ("(1) - Points and Triangles fully loaded.")
    
    # Load Camera Atributes 
    create_camera_and_start_camera()

