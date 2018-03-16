from PIL import Image
from math import sqrt



def circle(image, r, value, moving):
    for x in range(2 * (r + 1) + moving):
        for y in range(2 * (r + 1) + moving):
            if sqrt((x - (r + moving)) ** 2 + (y - (r + moving)) ** 2) < r:
                image.putpixel((x, y), (value, value, value))

image = Image.new("RGB", (500, 500))
circle(image, 250, 255, 0)
image.save("circle.png")



def cirle_in_circle(image, r):
    circle(image, r, 255, 0)
    circle(image, r-10, 0, 10)

image = Image.new("RGB", (500, 500))
cirle_in_circle(image, 250)
image.save("circle_in_circle.png")
