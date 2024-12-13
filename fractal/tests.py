# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
from fractal import fract
from minipng import Image

class Test(unittest.TestCase):


    def test_01_empty_base_case(self):
        """3 x 3 pixel image should be totally black. (1p)"""
        w = 3
        color = [255, 128, 0]
        img = Image(w, w)
        img_b = Image(w, w)
        colored = fract(img, 0, 0, w - 1, w - 1, color)
        self.assertIdentical(img, img_b)
        self.assertEqual(colored, 0)

    def test_02_base_case(self):
        """9 x 9 pixel image should have one 3 x 3 square. (1p)"""
        w = 9
        color = [255, 128, 0]
        img = Image(w, w)
        img_b = Image(w, w)
        colored = fract(img, 0, 0, w - 1, w - 1, color)
        img_b.rectangle(3, 3, 5, 5, color)
        self.assertIdentical(img, img_b)
        self.assertEqual(colored, 9)


    def assertIdentical(self, A, B):
        """ Asserts that two Images, A and B, are identical by the blackness
        of corresponding pixels. Alpha channels are not compared. """

        self.assertTrue((A.width == B.width) and (A.height == B.height),
            "Sizes of images differ. Your image has size {} x {}, but the " \
            "another image has size {} x {}.".format(A.width, A.height,
            B.width, B.height))

        if (A.width != B.width or A.height != B.height):
            return

        i = 0
        black = (0, 0, 0)
        for y in range(A.height):
            for x in range(A.width):
                rgb1 = (A.buffer[i], A.buffer[i + 1], A.buffer[i + 2])
                rgb2 = (B.buffer[i], B.buffer[i + 1], B.buffer[i + 2])

                #​​​​‌‌‌​‌‌‌‌‌​ Either both pixels must be black or both pixels are not
                #​​​​‌‌‌​‌‌‌‌‌​ black.
                self.assertTrue((rgb1 == rgb2 == black) or
                                (rgb1 != black and rgb2 != black),
                    "Images differ at pixel ({}, {}): your image has color " \
                    "{} while the other image has color {}." \
                    .format(x, y, rgb1, rgb2))
                i += 4


if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

