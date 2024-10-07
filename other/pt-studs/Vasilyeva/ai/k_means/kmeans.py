import sys
import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def square_distance(self, other: 'Point') -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def distance(self, other: 'Point') -> float:
        return self.square_distance(other) ** 0.5

    @classmethod
    def mean(cls, points: list['Point']) -> 'Point':
        x_mean, y_mean = 0, 0
        for point in points:
            x_mean += point.x
            y_mean += point.y
        return Point(x_mean / len(points), y_mean / len(points))

    def __str__(self) -> str:
        return f'.(x: {float(self.x):.2f}; y: {float(self.y):.2f})'


def generate_points(count: int, x_min: float, x_max: float, y_min: float, y_max: float) -> list[Point]:
    xs = np.random.uniform(x_min, x_max, count)
    ys = np.random.uniform(y_min, y_max, count)
    return [Point(x, y) for x, y in zip(xs, ys)]


def get_bounds() -> dict[str, float]:
    return {'x_min': -100, 'x_max': 100, 'y_min': -100, 'y_max': 100}


def random_centroids(count: int, bounds: dict[str, Point]) -> list[Point]:
    return generate_points(count, **bounds)


def k_means(points: list[Point], clusters_count: int, iterations: int, centroids_initializer: callable = random_centroids):
    bounds = get_bounds()
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

        visualize_plane(centroids, clusters, bounds, f'k-means, итерация {e + 1}', is_last=e == iterations - 1)


def visualize_plane(centroids: list[Point], clusters: list[list[Point]], bounds: dict[str, float] = None, title: str = None, is_last=False):
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
    plt.show(block=False)
    if not is_last:
        plt.pause(4)
        plt.close()
