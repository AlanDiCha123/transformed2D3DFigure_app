from math import sin, cos, pi
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np


def rotar(points: list[list[float]], piv: list[float], degrees: int) -> list[list[float]]:
    '''Rota la figura 2D con el pivote dado'''
    rads: float = (degrees * pi) / 180
    seno: float = sin(rads)
    coseno: float = cos(rads)

    for i in range(len(points)):
        if points[i] != piv:
            x_aux: float = points[i][0]
            points[i][0] = piv[0] + (points[i][0] - piv[0]) * \
                coseno - (points[i][1] - piv[1]) * seno
            points[i][1] = piv[0] + (x_aux - piv[0]) * \
                seno + (points[i][1] - piv[1]) * coseno

    return points


def escalar(points: list[list[float]], escala: float) -> list[list[float]]:
    '''Escala la figura 2D con la escala dada'''
    for i in range(len(points)):
        points[i][0] = points[i][0] * escala
        points[i][1] = points[i][1] * escala

    return points


if __name__ == "__main__":
    puntos = [[20, 20], [60, 20], [40, 60], [40, 40]]
    fig, ax = plt.subplots()

    # * Original
    poly1 = Polygon(puntos[:-1], fill=False, color="black", label="Original")
    ax.add_patch(poly1)

    # * Escala figura 30%
    puntos = escalar(puntos.copy(), 0.3)
    # print("Rotar")
    # print(puntos)
    poly2 = Polygon(puntos[:-1], fill=False,
                    color="blue", label="transformada 1")
    ax.add_patch(poly2)

    # * Rota figura 30 grados a D
    puntos = rotar(puntos.copy(), puntos[3].copy(), 30)
    # print("Escalar")
    # print(puntos)
    poly3 = Polygon(puntos[:-1], fill=False,
                    color="green", label="transformada 2")
    ax.add_patch(poly3)

    ax.set_xlim([0, 60])
    ax.set_ylim([0, 60])
    plt.xticks(range(0, 61, 4))
    plt.yticks(range(0, 61, 4))
    plt.axvline(x=0, color="red")
    plt.axhline(y=0, color="red")
    plt.legend()
    plt.show()
