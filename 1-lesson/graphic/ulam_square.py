from PIL import Image
from math import sqrt
from numba import jit


@jit(nopython=True)
def is_prime(potencial_prime):  # return boolean value, whether number is prime number
    if potencial_prime == 1:
        return False
    elif potencial_prime == 2:
        return True
    elif potencial_prime % 2 == 0:
        return False
    for x in range(3, int(sqrt(potencial_prime))+1, 2):
        if potencial_prime % x == 0:
            return False
    return True


def should_print(picture, number, x, y):  # decide, if pixel x, y should be printed
    if is_prime(number):
        picture.putpixel((x, y), (255, 255, 255))
    return number + 1


def ulam_square():  # show and save picture with something like ulam spiral but square.
    # Pixels are printed always from right top corner down and after it left to left bottom corner.
    image = Image.new("RGB", (1001, 1001))
    x = 1
    y = 0
    number = 1
    length = 1
    limit = number + 1000000
    start = 1
    while number < limit:
        for a in range(length):
            number = should_print(image, number, x, y)
            y += 1
        for b in range(length + 1):
            number = should_print(image, number, x, y)
            x -= 1
        length += 1
        y = 0
        start += 1
        x = start
    image.show()
    image.save("ulam_square.png")

ulam_square()
