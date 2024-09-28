from sys import maxsize as ms
from typing import List
import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def square_distance(self, other: 'Point') -> float:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def distance(self, other: 'Point') -> float:
        return self.square_distance(other) ** 0.5

    @classmethod
    def mean(cls, points: List['Point']):
        x_mean, y_mean = 0, 0
        for point in points:
            x_mean += point.x
            y_mean += point.y
        return Point(x_mean / len(points), y_mean / len(points))

    def __str__(self) -> str:
        return f'({self.x:.2f}; {self.y:.2f})'

    def __repr__(self):
        return self.__str__()


def generate_points(count: int, x_min: float, x_max: float, y_min: float, y_max: float):
    xs = np.random.uniform(x_min, x_max, count)
    ys = np.random.uniform(y_min, y_max, count)
    return [Point(x, y) for x, y in zip(xs, ys)]


def visualize_plane(clusters: List[List[Point]], x_min: float = None, x_max: float = None, y_min: float = None, y_max: float = None, title: str = None, centroids: List[Point] = None):
    plt.figure()

    colors = plt.cm.rainbow(np.linspace(0, 1, len(clusters)))
    for i, cluster in enumerate(clusters):
        x_coords = [point.x for point in cluster]
        y_coords = [point.y for point in cluster]
        plt.scatter(x_coords, y_coords, color=colors[i])
        if centroids:
            centroid = centroids[i]
            plt.scatter(centroid.x, centroid.y, color=colors[i], marker='X', s=150)

    plt.xlabel('X')
    plt.ylabel('Y')

    mng = plt.get_current_fig_manager()
    if x_min and x_max:
        plt.xlim(x_min, x_max)
    if y_min and y_max:
        plt.ylim(y_min, y_max)
    if title:
        mng.set_window_title(title)
    plt.show()


def find_bounds(points: List[Point]):
    x_min, x_max, y_min, y_max = ms, -ms, ms, -ms
    for point in points:
        x_min = min(x_min, point.x)
        x_max = max(x_max, point.x)
        y_min = min(y_min, point.y)
        y_max = max(y_max, point.y)
    return [x_min, x_max, y_min, y_max]


def random_centroids(points: List[Point], count: int):
    return generate_points(count, *find_bounds(points))


def k_means(points: List[Point], clusters_count: int, max_iterations: int = 100, centroids_initializer: callable = random_centroids, visualize_each_epoch: bool = False):
    ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    centroids = centroids_initializer(points, clusters_count)
    clusters = {l: {'centroid': c, 'points': []} for l, c in zip(ab, centroids)}
    bounds = find_bounds(points)

    first = True
    for i in range(max_iterations):
        if not first:
            unchanged = 0
            for _, cluster in clusters.items():
                if cluster['points']:
                    old_centroid = cluster['centroid']
                    new_centroid = Point.mean(cluster['points'])
                    cluster['centroid'] = new_centroid
                    if abs(old_centroid.x - new_centroid.x) < 0.0001 or abs(old_centroid.y - new_centroid.y) < 0.0001:
                        unchanged += 1
                else:
                    unchanged += 1
            if unchanged == len(clusters):
                break
            for _, cluster in clusters.items():
                cluster['points'].clear()

        for point in points:
            min_dist, min_key = ms, None
            for key, cluster in clusters.items():
                temp_dist = point.square_distance(cluster['centroid'])
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    min_key = key
            clusters[min_key]['points'].append(point)

        if visualize_each_epoch:
            visualize_plane([[clusters[ab[c]]['centroid'] for c in range(clusters_count)], *[clusters[ab[c]]['points'] for c in range(clusters_count)]], *bounds, title=f'k-means, итерация {i + 1}')
        first = False

    return clusters


def evaluate_wcss(clusters: dict):
    wcss = 0
    for _, cluster in clusters.items():
        centroid, points = cluster['centroid'], cluster['points']
        wcss += sum(p.square_distance(centroid) for p in points)
    return wcss


def k_means_n_trials(n_trials: int, points: List[Point], clusters_count: int, max_iterations: int = 100, centroids_initializer: callable = random_centroids):
    seen_wcss = []
    models = []
    for _ in range(n_trials):
        clusters = k_means(points, clusters_count, max_iterations, centroids_initializer)
        wcss = evaluate_wcss(clusters)
        if wcss in seen_wcss:
            continue
        models.append({'clusters': clusters, 'wcss': wcss})
        seen_wcss.append(wcss)
    return models
