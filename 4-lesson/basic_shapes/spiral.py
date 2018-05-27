from PIL import Image
from math import sin, cos, radians


def spiral():
    image = Image.new("RGB", (1000, 1000))
    for angle in range(1, 360*50*10):
        angle = angle / 10
        x = int(sin(radians(angle)) * angle / 50)
        y = int(cos(radians(angle)) * angle / 50)
        value = int(sin(radians(angle))*125)
        image.putpixel((x + 500, y + 500), (value, value, value))
    image.show()
    image.save("spiral.png")


spiral()
