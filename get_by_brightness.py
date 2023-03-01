import os
import sys
from PIL import Image, ImageStat


def get_image_brightness( file ):
    try:
        im = Image.open(file).convert('L')
    except IOError:
        return 0
    stat = ImageStat.Stat(im)
    print(file)
    return stat.mean[0]


image_dir = "landscape"

images = os.listdir(image_dir)
images.sort()

images = {image: get_image_brightness(image_dir + '/' + image) for image in images}

print("FINISHED")

# Sort by brightness
images = sorted(images.items(), key=lambda x: x[1])

# Print the sorted list
for image in images:
    print(image[0])
