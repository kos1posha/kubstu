import numpy as np
from PIL import Image


class ImageHelper:
    @staticmethod
    def image_to_array(file_path):
        image = Image.open(file_path)
        array = []
        for y in range(30):
            for x in range(30):
                array.append(0 if image.getpixel((x, y)) == (255, 255, 255) else 1)
        return np.array(array)

    @staticmethod
    def array_to_image(weights):
        image = Image.new('RGB', (30, 30))
        weights_stream = iter(weights)
        for y in range(30):
            for x in range(30):
                r = int((next(weights_stream) + 1) * 127)
                image.putpixel((x, y), (r, 0, 0))
        return image

    @staticmethod
    def perceptron_to_image(perceptron):
        neuron_images = [ImageHelper.array_to_image(neuron.weights) for neuron in perceptron.neurons]

        w, h = 30 * 3, 30 * 11
        combined_image = Image.new('RGB', (w, h))
        for i, image in enumerate(neuron_images):
            xy = (i % 3) * 30, (i // 3) * 30
            combined_image.paste(image, xy)

        return combined_image
