from PIL import Image


def NSD(a, b):  # return NSD according to euklid's algorythm
    if b < a:
        a, b = b, a
    while b != 0:
        modulo = a % b
        a = b
        b = modulo
    return a


def colored_image():  # show and save image with visualization of NSD
    image = Image.new("RGB", (750, 750))
    for x in range(1, 750):
        for y in range(1, 750):
            result = NSD(x, y)
            colors = []
            for z in range(3):  # NSD are divided into RGB format here
                if result > 256:
                    colors.append(256)
                    result = result - 256
                else:
                    colors.append(result)
                    result = 0
            image.putpixel((x, y), tuple(colors))
    image.show()
    image.save("highest_divisors.png")

colored_image()
