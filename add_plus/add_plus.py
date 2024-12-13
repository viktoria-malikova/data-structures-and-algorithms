# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286

def create_array(size):
    """Creates size * size array (two dimensional list). List items are stars"""
    array = []
    for i in range(size):
        array.append(["*" for j in range(size)])
    return array

def print_array(array):
    """Prints array"""
    for i in range(len(array)):
        print(array[i])

def array_to_list(array):
    """Converts two dimensional list into one dimensional ist."""
    list = []
    for sublist in array:
        for item in sublist:
            list.append(item)
    return list

def list_to_array(list, size):
    """Converts list to size * size array."""
    array = [[0]*size for i in range(size)]
    x = 0
    for i in range(size):
        for j in range(size):
            array[i][j] = list[x]
            x += 1
    return array


def add_plus(list, original_size):
    """Implement this recursive function."""
    raise NotImplementedError("Implement your function here.")

#​​​​‌‌‌​‌‌‌‌‌​ You can use main() test your recursive function.
def main():
    size = 7
    array = create_array(size)
    print_array(array)
    print()
    list = array_to_list(array)
    list = add_plus(list, size)
    array = list_to_array(list, size)
    print_array(array)


if __name__ == "__main__":
    main()

