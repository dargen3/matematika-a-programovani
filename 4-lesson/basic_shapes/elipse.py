from PIL import Image
from math import sqrt, cos, radians

def circle():
    r = 500
    image = Image.new("RGB", (r * 2, r * 2))
    for x in range(2 * (r + 1)):
        for y in range(2 * (r + 1)):
            if sqrt((x - r) ** 2 + ((y - 2 * r + x) * 3) ** 2) < int(r/2):
                value = int(cos(radians(sqrt((x - r) ** 2 + ((y - 2 * r + x) * 3) ** 2)/2))*500)
                image.putpixel((x, y), (value, value, value))
    image.show()
    image.save("elipse.png")

circle()
