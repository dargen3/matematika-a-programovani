from PIL import Image


def pascal_triangle(n):
    triangle = [[1], [1, 1]]
    for n_line in range(n-2):
        line = [1]
        for item in range(1,len(triangle[-1])):
            line.append(triangle[-1][item-1] + triangle[-1][item])
        line.append(1)
        triangle.append(line)
    return triangle

def print_square(middle_x, middle_y, image, value):
    for x in range(middle_x - 5, middle_x + 5):
        for y in range(middle_y - 5, middle_y + 5):
            image.putpixel((x, y), (value, value, value))


def pascal_picture(n, modulo):
    image = Image.new("RGB", (1000, 1000))
    triangle = pascal_triangle(n)
    for index, line in enumerate(triangle):
        y = (index + 1) * 10 - 5
        x = 500 - len(line) * 5
        for z in range(len(line)):
            print_square(x + z * 10, y, image, int((256 / modulo) * (line[z] % modulo)))
    image.show()

pascal_picture(90, 3)