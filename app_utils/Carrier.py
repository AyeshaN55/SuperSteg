import os
from PIL import Image
import numpy as np
import sys

class Carrier:

    def __init__(self, image_path):
        if os.path.splitext(image_path)[1].lower() != ".png":
            # validating image format (png only)
            print("Image fromat error\nexitting...")
            sys.exit(1)
        self.name = os.path.basename(image_path)
        self.path = os.path.dirname(image_path)
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print('Error loading image\nexitting...')
            sys.exit(1)
        self.mat = np.array(image)[..., :3]
        image.close()
        self.height = self.mat.shape[0]
        self.width = self.mat.shape[1]

    def create_image(self):
        carrier_image = Image.new('RGB', (self.width, self.height))
        for row in range(self.height):
            for col in range(self.width):
                carrier_image.putpixel((col, row), tuple(self.mat[row][col]))
        carrier_image.save('./encrypted_' + self.name)
        carrier_image.show()
