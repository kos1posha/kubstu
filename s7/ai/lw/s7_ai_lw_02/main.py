import os
from types import NoneType
from neural_network.neuron import Neuron
from bmp_helper import BmpHelper
from PIL import Image
from neural_network.perceptron import Perceptron


def main_neuron() -> NoneType:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letter = 'а'
    neuron = Neuron(letter)
    neuron.randomize()

    BmpHelper.array_to_bmp(neuron.weights).save(f'output\\start_neuron.bmp')

    bmp_array = BmpHelper.bmp_to_array(f'letters\\{letter}.bmp')
    while True:
        for _ in range(2):
            neuron.train(bmp_array, letter, 0.05)
        BmpHelper.array_to_bmp(neuron.weights).save(f'output\\neuron.bmp')
        user_input = input('Продолжить обучение... ').strip().lower()
        if user_input and user_input in alphabet:
            letter = user_input
            bmp_array = BmpHelper.bmp_to_array(f'letters\\{letter}.bmp')
        elif user_input == 'exit':
            break


def main_perceptron() -> NoneType:
    base_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    perceptron = Perceptron([Neuron(letter, 0.17) for letter in base_alphabet])
    perceptron.randomize()

    alphabet = 'руньла'
    BmpHelper.perceptron_to_bmp(perceptron).save(f'output\\start_perceptron.bmp')
    perceptron.set_activated_neurons([base_alphabet.index(letter) for letter in alphabet])

    for letter in alphabet:
        bmp_array = BmpHelper.bmp_to_array(f'letters\\{letter}.bmp')
        for _ in range(50):
            perceptron.train(bmp_array, letter, 0.05)
        BmpHelper.perceptron_to_bmp(perceptron).save('output\\perceptron.bmp')

    while True:
        letter = input('Введите букву для прогноза: ')
        if not letter or letter not in base_alphabet:
            continue

        signals = BmpHelper.bmp_to_array(f'letters\\{letter}.bmp')
        activated_neurons = perceptron.prognose(signals, 0.16)
        print(*[f'  {neuron} -> 1\n' for neuron, response in zip(perceptron.neurons, activated_neurons) if response == 1], sep='', end='')


if __name__ == '__main__':
    os.system('cls')
    main_perceptron()
