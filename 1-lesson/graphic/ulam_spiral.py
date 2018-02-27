from PIL import Image
from math import sqrt
from numba import jit

@jit(nopython=True)  # numba is JIT compilator for python, it make really faster code
def is_prime(potencial_prime):  # return boolean value, whether number is prime number
    if potencial_prime == 1:
        return False
    elif potencial_prime == 2:
        return True
    elif potencial_prime %2 == 0:
        return False
    for x in range(3, int(sqrt(potencial_prime))+1, 2):
        if potencial_prime % x == 0:
            return False
    return True

def should_print(picture, number, x, y):  # decide, if pixel x, y should be printed, or not
    if is_prime(number):
        picture.putpixel((x, y), (255, 255, 255))
    return number + 1

def ulam_spiral():  # show and save picture with ulam spiral
    image = Image.new("RGB", (1001, 1001))
    x = 500
    y = 500
    number = 1
    length = 1
    limit = 1000000
    while number < limit:
        for side in range(4):
            for a in range(length):
                if side in [0, 3]:
                    change = 1
                else:
                    change = -1
                if side in [0, 2]:
                    x = x + change
                else:
                    y = y + change
                number = should_print(image, number, x, y)
            if side % 2 != 0:
                length += 1
    image.show()
    image.save("ulam_spiral.png")

ulam_spiral()
