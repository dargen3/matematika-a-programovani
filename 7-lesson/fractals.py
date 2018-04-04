from PIL import Image
from math import sqrt
from os import system


def distance(x, y):
    return sqrt((x.real - y.real)**2 + (x.imag - y.imag)**2)

def color(x, y, method, c_real=-0.13, c_imag=0.75):
    if method == "Newton":
        if x == 0 and y == 0:
            return 0, 0, 0
        z = complex(x, y)
        for a in range(20):
            z = z - (z ** 3 - 1)/(3* z ** 2)
        min_distance = distance(complex(1, 0), z)
        best_root_index = 0
        for index, root in enumerate([complex(-0.5, sqrt(3)/2), complex(-0.5, -sqrt(3)/2)]):
            actual_distance = distance(root, z)
            if actual_distance < min_distance:
                min_distance = actual_distance
                best_root_index = index + 1
        if best_root_index == 0:
            return 255, 0, 0
        elif best_root_index == 1:
            return 0, 255, 0
        elif best_root_index == 2:
            return 0, 0, 255
    if method == "Mandelbrot":
        z = 0
        c = complex(x, y)
        for x in range(30):
            z = z ** 2 + c
            if distance(z, complex(0, 0)) > 2:
                return 0,0,255
        return 0,255,0
    if method == "Julia":
        z = complex(x, y)
        c = complex(c_real, c_imag)
        for x in range(30):
            z = z ** 2 + c
            if distance(z, complex(0, 0)) > 2:
                return 0,0,255
        return 0,255,0



def fractal(method, x_min, x_max, y_min, y_max, name, cr=None, ci=None):
    value = 1000
    image = Image.new("RGB", (value, value))
    for x in range(1, value):
        for y in range(1, value):
            cx = x / (1/(x_max - x_min)) + x_min*value
            cy = y / (1/(y_max - y_min)) + y_min*value
            if method == "Newton":
                yy = cy - value/2
                xx = cx - value/2
            elif method == "Mandelbrot":
                yy = -1.25 + 2.5 * cy/value
                xx = -2 + 2.5 * cx/value
            elif method == "Julia":
                yy = -3 + 6 * cy/value
                xx = -3 + 6 * cx/value
            image.putpixel((x, y), color(xx, yy, method, cr, ci))
    image.save(name)

def make_video():
    for x in range(70):
        print(x)
        fractal("Julia", 0, 1, 0, 1, str(x)+".png", -x/100, x/100)
    system("ffmpeg -r 5 -i %0d.png -vcodec mpeg4 -y movie.mp4")


fractal("Mandelbrot", 0, 1, 0, 1, "Mandelbrot.png")
fractal("Newton", 0, 1, 0, 1, "Newton.png")
#   make_video()