# -*- coding: utf-8 -*-
import numpy as np

'''retorna o vetor normalizado (com norma == 1)'''
def normalize(vector):
    norm = np.linalg.norm(vector)
    return vector / norm

