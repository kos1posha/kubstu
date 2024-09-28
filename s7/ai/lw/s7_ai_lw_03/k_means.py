import sys

import numpy as np
from matplotlib import pyplot as plt

from point import Point, generate_points, find_bounds


def random_centroids(count: int, bounds: dict[str, Point]) -> list[Point]:
    return generate_points(count, **bounds)


def k_means(points: list[Point], clusters_count: int, iterations: int, centroids_initializer: callable = random_centroids):
    bounds = find_bounds(points)
    centroids = centroids_initializer(clusters_count, bounds)
    clusters = [[] for _ in range(clusters_count)]

    for e in range(iterations):
        for i, cluster in enumerate(clusters):
            if cluster:
                centroids[i] = Point.mean(cluster)
                cluster.clear()
        for point in points:
            min_dist, min_dist_i = sys.maxsize, -1
            for i, centroid in enumerate(centroids):
                temp_dist = point.square_distance(centroid)
                if temp_dist < min_dist:
                    min_dist, min_dist_i = temp_dist, i
            clusters[min_dist_i].append(point)

        visualize_plane(centroids, clusters, bounds, f'k-means, итерация {e}')


def visualize_plane(centroids: list[Point], clusters: list[list[Point]], bounds: dict[str, float] = None, title: str = None):
    plt.figure()

    colors = plt.cm.rainbow(np.linspace(0, 1, len(clusters)))
    for i, cluster in enumerate(clusters):
        xs, ys = zip(*[point.as_tuple() for point in cluster]) if cluster else ([], [])
        plt.scatter(xs, ys, color=colors[i])
        plt.scatter(*centroids[i].as_tuple(), color=colors[i], marker='X', s=100)

    plt.xlabel('X')
    plt.ylabel('Y')
    mng = plt.get_current_fig_manager()
    if bounds:
        plt.xlim(bounds['x_min'], bounds['x_max'])
        plt.ylim(bounds['y_min'], bounds['y_max'])
    if title:
        mng.set_window_title(title)
    plt.show()
