# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import base64

#​​​​‌‌‌​‌‌‌‌‌​ Simple PNG writing function by Campbell Barton
#​​​​‌‌‌​‌‌‌‌‌​ License: MIT
#​​​​‌‌‌​‌‌‌‌‌​ http://code.activestate.com/recipes/577443-write-a-png-image-in-native-python/

#​​​​‌‌‌​‌‌‌‌‌​ This is a simple PNG writing function, intended to be as small as possible.
#​​​​‌‌‌​‌‌‌‌‌​ It only supports RGBA 32bit PNGs and the input should be a buffer of rgba
#​​​​‌‌‌​‌‌‌‌‌​ bytes. Pixels are ordered in vertical scanlines from top to bottom, and
#​​​​‌‌‌​‌‌‌‌‌​ inside each scanline from left to right.

def write_png(buf, width, height):
    import zlib, struct
    width_byte_4 = width * 4
    raw_data = b"".join(b'\x00' + buf[span:span + width_byte_4]
        for span in range(0, height * width * 4, width_byte_4))

    def png_pack(png_tag, data):
        chunk_head = png_tag + data
        return struct.pack("!I", len(data)) + chunk_head + struct.pack("!I",
            0xFFFFFFFF & zlib.crc32(chunk_head))

    return b"".join([
        b'\x89PNG\r\n\x1a\n',
        png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
        png_pack(b'IDAT', zlib.compress(raw_data, 9)),
        png_pack(b'IEND', b'')])


class Image:
    """
    Represents a RGBA bitmap image.
    Coordinates: top-left (x=0, y=0), x grows to right, y grows to bottom
    """

    def __init__(self, width = 640, height = 480):
        if (width < 4):
            width = 4
        if (height < 4):
            height = 4
        self.width = width
        self.height = height

        buffer = bytearray(width * height * 4)

        #​​​​‌‌‌​‌‌‌‌‌​ Initialize to black with full opacity
        end_i = height * width * 4
        i = 0
        while (i < end_i):
            buffer[i] = 0
            buffer[i + 1] = 0
            buffer[i + 2] = 0
            buffer[i + 3] = 255
            i += 4

        self.buffer = buffer

    def putpixel(self, x, y, c = (255, 255, 255)):
        """
        Paints a single pixel at (x, y) by color c = (r, g, b).
        """

        if (x >= 0 and x < self.width and y >= 0 and y < self.height):
            i = (y * self.width + x) * 4
            b = self.buffer
            b[i] = c[0]
            b[i+1] = c[1]
            b[i+2] = c[2]

    def rectangle(self, x1, y1, x2, y2, c = (255, 255, 255)):
        """
        Draws a filled rectangle from (x1, y1) to (x2, y2) (inclusive) by
        color c = (r, g, b).
        """

        if (x1 >= self.width or y1 >= self.height or x2 < 0 or y2 < 0 or
            x2 - x1 < 0 or y2 - y1 < 0):
            pass
        if (x1 < 0):
            x1 = 0
        if (y1 < 0):
            y1 = 0
        if (x2 >= self.width):
            x2 = self.width - 1
        if (y2 >= self.height):
            y2 = self.height - 1

        b = self.buffer
        bytes_width = (x2 - x1 + 1) * 4
        for y in range(y1, y2 + 1):
            i = (y * self.width + x1) * 4
            end_i = i + bytes_width
            while (i < end_i):
                b[i] = c[0]
                b[i+1] = c[1]
                b[i+2] = c[2]
                i += 4

    def write_to_file(self, filename, mode="normal"):
        """
        Writes the image to a PNG file.
        """
        f = open(filename, 'wb')
        if (mode == "normal"):
            f.write(write_png(self.buffer, self.width, self.height))
        elif (mode == "base64"):
            f.write(base64.b64encode(write_png(self.buffer, self.width,
                self.height)))
        else:
            raise Exception("Unknown mode \"{}\"".format(mode))
        f.close()

