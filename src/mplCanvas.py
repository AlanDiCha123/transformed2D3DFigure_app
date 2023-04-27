from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull
import numpy as np

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        ax = fig.subplots()
        poly = Polygon([[20, 20], [60, 20], [40, 60]], fill=None, color="red")
        ax.set_xlim([0, 80])
        ax.set_ylim([0, 80])
        ax.add_patch(poly)
        # self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MplCanvas3D(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100, index=0):

        self.A = np.array([[0.92523719, 0.26843252, 0.77794309], [0.73156748, 0.27794309, 0.57476281], [0.62113842, 0.37886158, 0.87886158], [0.72205691, 0.07476281, 0.76843252], [0.57476281, 0.23156748, 0.72205691], [0.77794309, 0.42523719, 0.73156748], [0.87886158, 0.12113842, 0.62113842], [0.76843252, 0.22205691, 0.92523719]])
        self.B = np.array([[0.23156748, 0.72205691, 0.57476281], [0.26843252, 0.77794309, 0.92523719], [0.12113842, 0.62113842, 0.87886158], [0.22205691, 0.92523719, 0.76843252], [0.27794309, 0.57476281, 0.73156748], [0.37886158, 0.87886158, 0.62113842], [0.07476281, 0.76843252, 0.72205691], [0.42523719, 0.73156748, 0.77794309]])
        self.C = np.array([[0.73156748, 0.77794309, 0.42523719], [0.62113842, 0.87886158, 0.12113842], [0.77794309, 0.92523719, 0.26843252], [0.57476281, 0.73156748, 0.27794309], [0.87886158, 0.62113842, 0.37886158], [0.72205691, 0.57476281, 0.23156748], [0.76843252, 0.72205691, 0.07476281], [0.92523719, 0.76843252, 0.22205691]])

        array1 = [[self.A], [self.B], [self.C]]
        array2 = [['r'], ['g'], ['b']]

        fig = Figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_subplot(111, projection='3d')
        for cube, color in zip(array1[index], array2[index]):
            hull = ConvexHull(cube)
            # draw the polygons of the convex hull
            for s in hull.simplices:
                tri = Poly3DCollection([cube[s]])
                tri.set_color(color)
                tri.set_alpha(0.5)
                ax.add_collection3d(tri)
            # draw the vertices
            ax.scatter(cube[:, 0], cube[:, 1], cube[:, 2], marker='o', color='purple')

        super(MplCanvas3D, self).__init__(fig)
