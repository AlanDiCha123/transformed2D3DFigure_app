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
    def __init__(self, parent=None, width=5, height=4, dpi=100, index=0, points=np.zeros((1,1))):


        colors = [['r'], ['g'], ['b']]

        fig = Figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_subplot(111, projection='3d')
        for cube, color in zip([points], colors[index]):
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
