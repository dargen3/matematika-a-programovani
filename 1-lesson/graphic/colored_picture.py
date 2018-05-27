from PIL import Image


def colored_image():  # show and save image with RGB combination of blue and red
    image = Image.new("RGB", (256, 256))
    for x in range(0, 256):
        for y in range(0, 256):
            image.putpixel((x, y), (y, 0, x))
    image.show()
    image.save("colored_picture.png")

colored_image()
