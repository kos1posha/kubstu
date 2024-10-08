from k_means import KMeansIterator
from point import generate_points


def main() -> None:
    a_cluster = generate_points(10, 10, 15, 10, 15)
    b_cluster = generate_points(10, -5, 5, -5, 5) + generate_points(10, 0, 10, -10, 0) + generate_points(10, -10, 0, 0, 10)
    c_cluster = generate_points(10, -10, -15, -10, -15)

    points = a_cluster + b_cluster + c_cluster
    k_means = KMeansIterator(points, 3, 1000)
    k_means(True)


if __name__ == '__main__':
    main()
