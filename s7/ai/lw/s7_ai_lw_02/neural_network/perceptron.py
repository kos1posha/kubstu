from neural_network.neuron import Neuron

import numpy as np
from concurrent import futures


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

    def train(self, signals: np.ndarray, letter: str, alpha: float) -> None:
        neuron_train = lambda neuron: neuron.train(signals, letter, alpha)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(neuron_train, self.neurons))

    def predict(self, signals: np.ndarray, threshold: float = None) -> list[int]:
        neuron_predict = lambda neuron: neuron.predict(signals, threshold)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            return list(executor.map(neuron_predict, self.neurons))
