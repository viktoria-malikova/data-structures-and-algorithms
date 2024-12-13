# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the count_circles_and_squares function here below

import math

def count_circles_and_squares(length, circles, squares):
    #​​​​‌‌‌​‌‌‌‌‌​ Write your code here
    if length / math.sqrt(0.5) < 1:
        return False
    else:
        if length < 1:
            return (circles, squares)
        elif circles > squares:
            return count_circles_and_squares(length, circles, squares + 1)
        else:



#​​​​‌‌‌​‌‌‌‌‌​ A simple example
def main():
    length = 2
    circles, squares = count_circles_and_squares(length, 0, 0)
    print("Circles:", circles, "Squares:", squares)


if __name__ == "__main__":
    main()

