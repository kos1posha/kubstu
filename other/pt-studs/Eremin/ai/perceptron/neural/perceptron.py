import numpy as np

from concurrent import futures

from matplotlib import pyplot as plt


class Neuron:
    def __init__(self, letter: str, threshold: float = 0.15) -> None:
        self.weights = np.zeros(900, dtype=np.float32)
        self.letter = letter
        self.threshold = threshold

    def randomize(self) -> None:
        self.weights = -1 + np.random.rand(900) * 2

    def train(self, signals: np.ndarray, letter: str, alpha: float, epochs: int = 1) -> None:
        expected = int(letter == self.letter)
        for _ in range(epochs):
            actual = self.predict(signals)
            error = expected - actual
            self.weights = np.clip(self.weights + (signals * alpha * error), -1, 1)

    def predict(self, signals: np.ndarray, threshold: float = None) -> int:
        threshold = threshold or self.threshold
        weights_sum = np.dot(signals, self.weights) / 900
        return int(weights_sum > threshold)

    def visualize(self):
        im = self.weights.reshape(30, 30)
        fig, ax = plt.subplots()
        cax = ax.imshow(im, cmap='viridis', interpolation='nearest', vmin=-1, vmax=1)
        plt.colorbar(cax)

        def hover(event):
            if event.inaxes == ax:
                x, y = int(event.xdata), int(event.ydata)
                if 0 <= x < 30 and 0 <= y < 30:
                    ax.set_title(f'Вес: {im[y, x]:.2f}')
                    plt.draw()

        plt.get_current_fig_manager().set_window_title(f'Нейрон: {self.letter}')
        fig.canvas.mpl_connect('motion_notify_event', hover)
        plt.show()

    def __repr__(self) -> str:
        return f'Neuron: {self.letter}'


class Perceptron:
    def __init__(self, neurons: list[Neuron]) -> None:
        self._neurons = neurons
        self._activated_neurons = None

    def set_activated_neurons(self, indexes) -> None:
        self._activated_neurons = indexes

    @property
    def neurons(self) -> list[Neuron]:
        if not self._activated_neurons:
            return self._neurons
        return [self._neurons[i] for i in self._activated_neurons]

    def randomize(self) -> None:
        for neuron in self.neurons:
            neuron.randomize()

    def train(self, signals: np.ndarray, letter: str, alpha: float, epochs: int = 1) -> None:
        neuron_train = lambda neuron: neuron.train(signals, letter, alpha, epochs)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(neuron_train, self.neurons))

    def predict(self, signals: np.ndarray, threshold: float = None) -> list[int]:
        neuron_predict = lambda neuron: neuron.predict(signals, threshold)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            return list(executor.map(neuron_predict, self.neurons))
