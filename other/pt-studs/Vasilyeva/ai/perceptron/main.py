import os
import sys

from PIL import Image, ImageDraw, ImageFont
from PySide6 import QtWidgets as qtw

from qt import PerceptronControl


def create_letter_images():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_dir = 'letters'
    fonts = {
        'tnr': 'ttf/times new roman.ttf',
        'arial': 'ttf/arial.ttf',
        'consolas': 'ttf/consolas.ttf'
    }

    px = 30
    os.makedirs(letters_dir, exist_ok=True)
    for letter in letters:
        for font_name, font_file in fonts.items():
            letter_dir = os.path.join(letters_dir, letter)
            os.makedirs(letter_dir, exist_ok=True)
            image = Image.new('RGB', (px, px), color='white')
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font_file, 30)
            l, t, r, b = font.getbbox(letter)
            x, y = (px - r - l) / 2, (px - b - t) / 2
            draw.text((x, y), letter, font=font, fill='black')
            image_path = os.path.join(letter_dir, f'{font_name}.png')
            image.save(image_path)


def main():
    app = qtw.QApplication(sys.argv + ['-platform', 'windows:darkmode=1'])
    app.setStyle('fusion')
    control = PerceptronControl()
    control.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    main()
