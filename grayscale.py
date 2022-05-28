from PIL import Image
import numpy as np
import os

GRAYSCALE_MULTIPLIER = np.array(
    [[1/3, 1/3, 1/3],
    [1/3, 1/3, 1/3],
    [1/3, 1/3, 1/3]]
)

def get_pngs():
    pngs = []
    for name in os.listdir():
        if name.endswith(".png"):
            pngs.append(name)
    return pngs

def grayscale_image(name, output_name=None):
    if output_name is None:
        output_name = name
    image = Image.open(name)
    image_array = np.array(image)
    grayscaled = Image.new("L", image.size)
    grayscaled_pixels = grayscaled.load()

    for y, row in enumerate(image_array):
        for x, cell in enumerate(row):
            new_cell_value = np.array(image_array[y][x]).T
            new_cell_value = np.matmul(GRAYSCALE_MULTIPLIER, new_cell_value)[0]
            grayscaled_pixels[y, x] = int(new_cell_value)

    grayscaled.save(output_name)


if __name__ == "__main__":
    pngs = get_pngs()
    for png in pngs:
        grayscale_image(png)
