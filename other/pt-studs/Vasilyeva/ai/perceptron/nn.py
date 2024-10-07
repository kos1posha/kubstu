import numpy as np
from concurrent import futures


class Neuron:
    def __init__(self, letter, threshold=0.15):
        self.weights = np.zeros(900, dtype=np.float32)
        self.letter = letter
        self.threshold = threshold

    def randomize(self):
        self.weights = -1 + np.random.rand(900) * 2

    def train(self, signals, letter, alpha, epochs=1):
        for _ in range(epochs):
            expected = int(letter == self.letter)
            actual = self.predict(signals)
            error = expected - actual
            self.weights = np.clip(self.weights + signals * alpha * error, -1, 1)

    def predict(self, signals, threshold=None):
        threshold = threshold or self.threshold
        weights_sum = np.dot(signals, self.weights) / 900
        return int(weights_sum > threshold)

    def __repr__(self):
        return f'Нейрон {self.letter}'


class Perceptron:
    def __init__(self, neurons):
        self.neurons = neurons

    def randomize(self):
        for neuron in self.neurons:
            neuron.randomize()

    def train(self, signals, letter, alpha, epochs=1, letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        neuron_train = lambda neuron: neuron.train(signals, letter, alpha, epochs)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(neuron_train, [n for n in self.neurons if n.letter in letters]))

    def predict(self, signals, threshold=None):
        neuron_predict = lambda neuron: neuron.predict(signals, threshold)
        with futures.ThreadPoolExecutor(max_workers=8) as executor:
            return list(executor.map(neuron_predict, self.neurons))
