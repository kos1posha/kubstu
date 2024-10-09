import sys

import numpy as np
from matplotlib import pyplot as plt

from point import Point, generate_points, find_bounds


def random_centroids(count: int, bounds: dict[str, Point]) -> list[Point]:
    return generate_points(count, **bounds)


class KMeansIterator:
    def __init__(self, points: list[Point], clusters_count: int, max_iterations: int = 100, centroids_initializer: callable = random_centroids) -> None:
        self.points = points
        self.max_iterations = max_iterations
        self.bounds = find_bounds(points)
        self.centroids = centroids_initializer(clusters_count, self.bounds)
        self.clusters = [[] for _ in range(clusters_count)]
        self.current_iteration = 0

    def __iter__(self) -> 'KMeansIterator':
        return self

    def __next__(self) -> tuple[list[Point], list[list[Point]]]:
        if self.current_iteration == self.max_iterations:
            raise StopIteration
        for i, cluster in enumerate(self.clusters):
            if cluster:
                self.centroids[i] = Point.mean(cluster)
                cluster.clear()
        for point in self.points:
            min_dist, min_dist_i = sys.maxsize, -1
            for i, centroid in enumerate(self.centroids):
                temp_dist = point.square_distance(centroid)
                if temp_dist < min_dist:
                    min_dist, min_dist_i = temp_dist, i
            self.clusters[min_dist_i].append(point)
        self.current_iteration += 1
        return self.centroids, self.clusters

    def __call__(self, visualize: bool = False) -> None:
        for e, _ in enumerate(self):
            if visualize:
                self.visualize(f'k-means, итерация {e + 1}')

    def visualize(self, title: str = None) -> None:
        plt.figure()

        colors = plt.cm.rainbow(np.linspace(0, 1, len(self.clusters)))
        for i, cluster in enumerate(self.clusters):
            xs, ys = zip(*[point.as_tuple() for point in cluster]) if cluster else ([], [])
            plt.scatter(xs, ys, color=colors[i])
            plt.scatter(*self.centroids[i].as_tuple(), color=colors[i], marker='X', s=100)

        plt.xlabel('X')
        plt.ylabel('Y')
        mng = plt.get_current_fig_manager()
        if self.bounds:
            plt.xlim(self.bounds['x_min'], self.bounds['x_max'])
            plt.ylim(self.bounds['y_min'], self.bounds['y_max'])
        if title:
            mng.set_window_title(title)
        plt.show()
