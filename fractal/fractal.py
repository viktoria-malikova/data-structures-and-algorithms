# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the generate_image and fract functions here below

from minipng import Image

#​​​​‌‌‌​‌‌‌‌‌​ Complete this function
def fract(img, x1, y1, x2, y2, c):
    pass

#​​​​‌‌‌​‌‌‌‌‌​ Helper function
def generate_image(level):

    #​​​​‌‌‌​‌‌‌‌‌​ Initialize image and color
    w = 3 ** level
    img = Image(w, w)
    c = [0, 192, 128]

    #​​​​‌‌‌​‌‌‌‌‌​ Example on how to draw a rectangle
    d = w // 9
    img.rectangle(d, 2 * d, 3 * d, 4 * d, c)
    #​​​​‌‌‌​‌‌‌‌‌​ Example ends

    #​​​​‌‌‌​‌‌‌‌‌​ Call fract(img, ...) here
    #​​​​‌‌‌​‌‌‌‌‌​fract(img)

    img.write_to_file('fractal.png')

if __name__ == '__main__':
    #​​​​‌‌‌​‌‌‌‌‌​ You can write your test code here
    generate_image(5)

