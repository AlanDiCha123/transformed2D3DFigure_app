from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.patches import Polygon


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
