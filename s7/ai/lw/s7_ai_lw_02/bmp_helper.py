from neural_network.perceptron import Perceptron
import numpy as np
from PIL import Image


class BmpHelper:
    @staticmethod
    def bmp_to_array(bmp_path: str) -> np.ndarray:
        bmp = Image.open(bmp_path)
        bmp_array = []
        for y in range(30):
            for x in range(30):
                bmp_array.append(0 if bmp.getpixel((x, y)) == (255, 255, 255) else 1)
        return np.array(bmp_array)

    @staticmethod
    def array_to_bmp(weights: np.ndarray) -> Image:
        bmp = Image.new('RGB', (30, 30))
        weights_stream = iter(weights)
        for y in range(30):
            for x in range(30):
                r = int((next(weights_stream) + 1) * 127)
                bmp.putpixel((x, y), (r, 0, 0))
        return bmp

    @staticmethod
    def print_bmp_to_console(bmp_path: str, w=1) -> None:
        bmp_array = BmpHelper.bmp_to_array(bmp_path)
        bmp_stream = iter(bmp_array)
        for _ in range(30):
            for _ in range(30):
                print(str(next(bmp_stream)) * w, end='')
            print()

    @staticmethod
    def perceptron_to_bmp(perceptron: Perceptron, only_activated: bool = False) -> Image:
        neurons = perceptron.neurons if only_activated else perceptron._neurons
        neuron_bmps = [BmpHelper.array_to_bmp(neuron.weights) for neuron in neurons]

        w, h = 30 * 3, 30 * 11
        combined_image = Image.new('RGB', (w, h))
        for i, bitmap in enumerate(neuron_bmps):
            xy = (i % 3) * 30, (i // 3) * 30
            combined_image.paste(bitmap, xy)

        return combined_image
