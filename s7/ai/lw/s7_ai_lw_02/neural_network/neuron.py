import numpy as np


import random
from types import NoneType


class Neuron:
    def __init__(self, letter: str, threshold=0.5) -> NoneType:
        self.weights = np.zeros(900, dtype=np.float32)
        self.letter = letter
        self.threshold = threshold

    def randomize(self) -> NoneType:
        self.weights = np.random.rand(900)

    def append_weight(self, i: int, value: float) -> NoneType:
        self.weights[i] = max(-1, min(self.weights[i] + value, 1))

    def train(self, signals: np.ndarray, letter: str, alpha: float) -> NoneType:
        expected = int(letter == self.letter)
        actual = self.prognose(signals)
        error = expected - actual
        
        for i in range(900):
            self.append_weight(i, alpha * error * signals[i])
    
    def prognose(self, signals: np.ndarray) -> int:
        weights_sum = np.dot(signals, self.weights) / 900
        return int(weights_sum > self.threshold)
# оптимизировал вычисления с numpy, также провел небольшой рефакторинг