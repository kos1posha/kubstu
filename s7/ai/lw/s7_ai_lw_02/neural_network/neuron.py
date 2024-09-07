import numpy as np


import random
from types import NoneType


class Neuron:
    def __init__(self, letter: str, activator=0.5) -> NoneType:
        self.weights = [0.0] * 900
        self.letter = letter
        self.activator = activator

    def randomize(self) -> NoneType:
        for i in range(len(self.weights)):
            self.weights[i] = -1 + random.random() * 2

    def append_weight(self, i: int, value: float) -> NoneType:
        self.weights[i] = max(-1, min(self.weights[i] + value, 1))

    def train(self, signals: np.ndarray, letter: str, alpha: float) -> NoneType:
        expected = int(letter == self.letter)
        actual = self.prognose(signals)
        e = expected - actual
        for i in range(900):
            self.append_weight(i, alpha * e * signals[i])

    def prognose(self, signals: np.ndarray) -> int:
        weights_sum = np.dot(signals, self.weights) / 900
        return int(weights_sum > self.activator)
