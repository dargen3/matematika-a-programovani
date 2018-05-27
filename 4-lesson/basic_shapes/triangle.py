from PIL import Image
from math import sqrt


def triangle():
    image = Image.new("RGB", (500, 500))
    points = [[372, 299], [1, 200], [372, 101]]
    sqrt3 = sqrt(3)
    for x in range(500):
        for y in range(500):
            if y < 300 and y > sqrt3 / 2 - sqrt3 * (x - 200) and y > sqrt3 / 2 + sqrt3 * (x - 200):
                colors = []
                for z in range(3):
                    colors.append(int(sqrt((x - points[z][0])**2 + (y - points[z][1])**2)))
                image.putpixel((x, y), tuple(colors))
    image.show()
    image.save("tringle.png")

triangle()
