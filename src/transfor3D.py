from math import sin, cos, pi
import numpy as np

def rotar3D(points: list[list[float]], degX: float, degY: float, degZ: float) -> list[list[float]]:

    # * Para el eje Z
    radianes = (degZ / pi) * 180
    seno = sin(radianes)
    coseno = cos(radianes)

    for i in range(len(points)):
        aux = points[i].copy()
        points[i][0] = (aux[0] * coseno) - (aux[1] * seno)
        points[i][1] = (aux[0] * seno) + (aux[1] * coseno)

    # * Para el eje X
    radianes = (degX / pi) * 180
    seno = sin(radianes)
    coseno = cos(radianes)

    for i in range(len(points)):
        aux = points[i].copy()
        points[i][1] = (aux[1] * coseno) - (aux[2] * seno)
        points[i][2] = (aux[1] * seno) + (aux[2] * coseno)

    # * Para el eje Y
    radianes = (degY / pi) * 180
    seno = sin(radianes)
    coseno = cos(radianes)

    for i in range(len(points)):
        aux = points[i].copy()
        points[i][0] = (aux[2] * coseno) - (aux[0] * seno)
        points[i][2] = (aux[2] * seno) + (aux[0] * coseno)
    
    return points

def trasladar3D(points: list[list[float]], vector: list[float]) -> list[list[float]]:
    '''Traslada la figura 3D con el vector dado'''
    for i in range((len(points))):
        points[i][0] += vector[0]
        points[i][1] += vector[1]
        points[i][2] += vector[2]
    
    return points


def escalar3D(points: list[list[float]], piv: list[float], escala: float) -> list[list[float]]:
    '''Escala la figura 3D con la escala dada'''

    matrix = np.zeros((4, 4))
    matrix2 = np.zeros((4, 1))

    for i in range(4):
        if i <=2:
            matrix[i][i] = escala
            matrix[i][3] = (1 - escala) * piv[i]
        else:
            matrix[i][i] = 1
    for i in range(len(points)):
        for j in range(len(points[i]) + 1):
            if j == len(points[i]):
                matrix2[j][0] = 1
            else:
                matrix2[j][0] = points[i][j]
        aux = matrix@matrix2
        for j in range(len(points[i])):
            points[i][j] = aux[j][0]
    return points


if __name__ == "__main__":
    A = np.array([[0.92523719, 0.26843252, 0.77794309], [0.73156748, 0.27794309, 0.57476281], [0.62113842, 0.37886158, 0.87886158], [0.72205691, 0.07476281, 0.76843252], [0.57476281, 0.23156748, 0.72205691], [0.77794309, 0.42523719, 0.73156748], [0.87886158, 0.12113842, 0.62113842], [0.76843252, 0.22205691, 0.92523719]])
    print(A)
    print(escalar3D(A.copy(), A[0].copy(), 0.8))