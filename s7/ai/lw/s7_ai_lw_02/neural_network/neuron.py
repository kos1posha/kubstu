import numpy as np


class Neuron:
    def __init__(self, letter: str, threshold: float = 0.15) -> None:
        self.weights = np.zeros(900, dtype=np.float32)
        self.letter = letter
        self.threshold = threshold

    def randomize(self) -> None:
        self.weights = -1 + np.random.rand(900) * 2

    def train(self, signals: np.ndarray, letter: str, alpha: float) -> None:
        expected = int(letter == self.letter)
        actual = self.predict(signals)
        error = expected - actual
        self.weights = np.clip(self.weights + signals * alpha * error, -1, 1)

    def predict(self, signals: np.ndarray, threshold: float = None) -> int:
        threshold = threshold or self.threshold
        weights_sum = np.dot(signals, self.weights) / 900
        return int(weights_sum > threshold)

    def __repr__(self) -> str:
        return f'Neuron: {self.letter}'
