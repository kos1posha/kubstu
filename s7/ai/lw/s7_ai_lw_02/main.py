from types import NoneType
from neural_network.neuron import Neuron
from bmp_helper import BmpHelper


def main() -> NoneType:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letter = 'a'
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


if __name__ == '__main__':
    main()
