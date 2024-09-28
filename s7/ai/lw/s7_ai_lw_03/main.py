from k_means import k_means
from point import generate_points


def main():
    a_cluster = generate_points(10, 10, 15, 10, 15)
    b_cluster = generate_points(10, -5, 5, -5, 5) + generate_points(10, 0, 10, -10, 0) + generate_points(10, -10, 0, 0, 10)
    c_cluster = generate_points(10, -10, -15, -10, -15)

    points = a_cluster + b_cluster + c_cluster
    k_means(points, 3, 1000)


if __name__ == '__main__':
    main()
