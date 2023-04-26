from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from transfor3D import trasladar3D, escalar3D

A = np.array([[0.92523719, 0.26843252, 0.77794309], [0.73156748, 0.27794309, 0.57476281], [0.62113842, 0.37886158, 0.87886158], [0.72205691, 0.07476281, 0.76843252], [0.57476281, 0.23156748, 0.72205691], [0.77794309, 0.42523719, 0.73156748], [0.87886158, 0.12113842, 0.62113842], [0.76843252, 0.22205691, 0.92523719]])
# A = np.array([[0.95, 0.27, 0.78], [0.78, 0.43, 0.73], [0.62, 0.38, 0.88], [0.77, 0.22, 0.95], [0.72, 0.07, 0.77], [0.88, 0.12, 0.62], [0.73, 0.28, 0.57], [0.57, 0.23, 0.72]])
B = np.array([[0.23156748, 0.72205691, 0.57476281], [0.26843252, 0.77794309, 0.92523719], [0.12113842, 0.62113842, 0.87886158], [0.22205691, 0.92523719, 0.76843252], [0.27794309, 0.57476281, 0.73156748], [0.37886158, 0.87886158, 0.62113842], [0.07476281, 0.76843252, 0.72205691], [0.42523719, 0.73156748, 0.77794309]])
C = np.array([[0.73156748, 0.77794309, 0.42523719], [0.62113842, 0.87886158, 0.12113842], [0.77794309, 0.92523719, 0.26843252], [0.57476281, 0.73156748, 0.27794309], [0.87886158, 0.62113842, 0.37886158], [0.72205691, 0.57476281, 0.23156748], [0.76843252, 0.72205691, 0.07476281], [0.92523719, 0.76843252, 0.22205691]])
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# A = trasladar3D(A.copy(), [-1, -1, -1])
A = escalar3D(A.copy(), A[2], 0.5)
for cube, color in zip([A, B, C], ['r', 'g', 'b']):
    hull = ConvexHull(cube)
    # draw the polygons of the convex hull
    for s in hull.simplices:
        tri = Poly3DCollection([cube[s]])
        tri.set_color(color)
        tri.set_alpha(0.5)
        ax.add_collection3d(tri)
    # draw the vertices
    ax.scatter(cube[:, 0], cube[:, 1], cube[:, 2], marker='o', color='purple')
plt.show()