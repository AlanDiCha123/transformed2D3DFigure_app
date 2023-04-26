from math import sin, cos, pi
import numpy as np

def rotar3D(points: list[list[float]], piv: list[float], degrees: int) -> list[list[float]]:

    radianes = (degrees / pi) * 180

    seno = sin(radianes)
    coseno = cos(radianes)

    # * Filling matrix T 
    # m_T = np.zeros((4, 4))
    # for i in range():
    #     if i <= 2:
    #         m_T[i][3] = - points[0][i]
    #         m_T[i][i] = 1
    #     else:
    #         m_T[i][i] = 1
    
    # * Filling matrix T inverse
    m_T_i = np.linalg.inv(m_T)

    # * Filling matrix Rx
    m_Rx = np.zeros((4, 4))
    m_Rx[0][0] = 1
    m_Rx[3][3] = 1
    m_Rx[1][1] = coseno
    m_Rx[1][2] = -seno
    m_Rx[2][1] = seno
    m_Rx[2][2] = coseno

    # * Filling matrix Rx inverse
    m_Rx_i = np.linalg.inv(m_Rx)

    # * Filling matrix Ry
    m_Ry = np.zeros((4, 4))
    m_Ry[0][2] = seno
    m_Ry[2][0] = -seno
    for i in range(len(m_Ry)):
        if i % 2 == 0:
            m_Ry[i][i] = coseno
        else:
            m_Ry[i][i] = 1
    
    # * Filling matrix Ry inverse
    m_Ry_i = np.linalg.inv(m_Ry)

    # * Filling matrix Rz
    m_Rz = np.zeros((4, 4))
    m_Rz[0][1] = seno
    m_Rz[1][0] = -seno
    for i in range(len(m_Rz)):
        if i <= 1:
            m_Rz[i][i] = coseno
        else:
            m_Rz[i][i] = 1


    for i in range(len(points)):
        for i in range():
            m_T = np.zeros((4, 4))
            if i <= 2:
                m_T[i][3] = - points[0][i]
                m_T[i][i] = 1
            else:
                m_T[i][i] = 1
        for j in range(len(points)):
            points
            aux = m_T_i@m_Rx_i@m_Ry_i@m_Rz@m_Ry@m_Rx@m_T
    # TODO: Fix these



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
