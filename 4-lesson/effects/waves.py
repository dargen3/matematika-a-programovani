from PIL import Image
from math import sqrt, sin, radians


def waves():
    image = Image.new("RGB", (1000, 1000))
    for x in range(1000):
        for y in range(1000):
            value = int(sin(radians(sqrt((x-500)**2 + (y-500)**2))**(13/3))*125)
            image.putpixel((x, y), (value, value, value))
    image.show()
    image.save("waves.png")
waves()