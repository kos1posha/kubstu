import sys
from k_means import KMeansIterator
from point import generate_points

from PySide6 import QtWidgets as qtw
from qt import KMeansControl


def main_plot() -> None:
    a_cluster = generate_points(10, 10, 15, 10, 15)
    b_cluster = generate_points(10, -5, 5, -5, 5) + generate_points(10, 0, 10, -10, 0) + generate_points(10, -10, 0, 0, 10)
    c_cluster = generate_points(10, -10, -15, -10, -15)

    points = a_cluster + b_cluster + c_cluster
    k_means = KMeansIterator(points, 3, 1000)
    k_means(True)


def main() -> None:
    app = qtw.QApplication(sys.argv)
    app.setStyle('fusion')
    control = KMeansControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
