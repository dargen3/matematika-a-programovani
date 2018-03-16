from PIL import Image
from math import sin, cos, radians

def spiral(image):
    for angle in range(1, 360*50*20*10):
        try:
            angle = angle / 100
            x = int(sin(radians(angle)) * angle / 50)
            y = int(cos(radians(angle)) * angle / 50)
            image.putpixel((x + 500, y + 500), (255, 255, 255))
        except IndexError:
            pass



def squares(image):
    colors = [(0, 0, 255), (0, 255, 0)]
    index = 0
    for x in range(10):
        original_index = index
        for y in range(100):
            index = original_index
            for z in range(10):
                for m in range(100):
                    try:
                        if image.getpixel((x * 100 + y, z * 100 + m)) == (255, 255, 255) and z * 100 + m:
                            if image.getpixel((x * 100 + y, z * 100 + m + 1)) != (255, 255, 255):
                                index += 1
                    except IndexError:
                        pass
                    image.putpixel((x * 100 + y, z * 100 + m), colors[index % 2])
                index += 1
        index = original_index + 1





image = Image.new("RGB", (1000, 1000))
spiral(image)
squares(image)

image.show()
image.save("spiral_and_squares.png")