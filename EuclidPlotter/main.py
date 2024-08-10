from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class GalaxyPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('3D Galaxy Plotter')
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Create a terminal input field
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter coordinates (XXX, ZZZ, YY)')
        layout.addWidget(self.input_field)

        # Create a plot button
        plot_button = QPushButton('Plot Coordinate', self)
        plot_button.clicked.connect(self.plot_coordinate)
        layout.addWidget(plot_button)

        self.setCentralWidget(central_widget)

    def plot_coordinate(self):
        coords = self.input_field.text()
        if coords:
            x, z, y = [int(coord, 16) for coord in coords.split(',')]  # Swap Z and Y
            self.plot_3d(x, y, z)

    def plot_3d(self, x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        ax.set_xlabel('XXX')
        ax.set_ylabel('ZZZ')  # Label changed to reflect the swapped axes
        ax.set_zlabel('YY')   # Label changed to reflect the swapped axes
        plt.show()

app = QApplication(sys.argv)
window = GalaxyPlotter()
window.show()
sys.exit(app.exec_())
