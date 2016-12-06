# -*- coding: utf-8 -*-
import numpy as np


'''retorna o vetor normalizado (com norma == 1)'''
def normalize(vector):
    norm = np.linalg.norm(vector)

    return vector / norm


def grand_schimidt(vector_v,vector_n):
	num = np.dot(vector_v, vector_n)
	den = np.dot(vector_n, vector_n)
	partial = float(num/den)

	return np.dot(partial, vector_n)
