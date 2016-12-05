import numpy as np


'''gera o SCC (vetor uvn resultante) equivalente aos argumentos uvn e xyz passados
onde uvn é uma matriz contendo as triplas do sist. de coordenadas da câmara e xyz é uma tripla np.array([x, y, z])
contendo o vetor a ser transformado'''
def getSCC(uvn, xyz):
    uvn, xyz = np.array(uvn), np.array(xyz)
    return uvn.dot(xyz)



