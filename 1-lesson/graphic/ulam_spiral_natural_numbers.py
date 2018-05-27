from PIL import Image


def should_print(picture, number, x, y, natural_number):  # decide if pixel x, y should be printed
    if number % natural_number == 0:
        picture.putpixel((x, y), (255, 255, 255))
    return number + 1


def ulam_spiral_natural_number(natural_number):  # show and save spiral of natural numbers, all of that, which can be divided by choosen number are printed
    image = Image.new("RGB", (1001, 1001))
    x = 500
    y = 500
    number = 1
    length = 1
    limit = number + 1000000
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
                number = should_print(image, number, x, y, natural_number)
            if side % 2 != 0:
                length += 1
    image.show()
    image.save("ulam_spiral_natural_number_{}.png".format(natural_number))


for x in range(3, 50):
    ulam_spiral_natural_number(x)
