from math import sin, cos, pi


def rotar(points: list[list[int]], piv: list[int], degrees: int) -> list[list[int]]:
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


def escalar(points: list[list[int]], escala: float) -> list[list[int]]:
    '''Escala la figura 2D con la escala dada'''
    for i in range(len(points)):
        points[i][0] = points[i][0] * escala
        points[i][1] = points[i][1] * escala

    return points


if __name__ == "__main__":
    puntos = [[20, 20], [60, 20], [40, 60], [40, 40]]

    puntos = escalar(puntos.copy(), 0.3)
    print("Rotar")
    print(puntos)

    puntos = rotar(puntos.copy(), puntos[3].copy(), 30)
    print("Escalar")
    print(puntos)
