# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
def my_sort(lst):
    """Return the sequence `lst` sorted in-place in ascending order."""

    #​​​​‌‌‌​‌‌‌‌‌​ Note: in-place means, that the method shouldn't create and return another
    #​​​​‌‌‌​‌‌‌‌‌​ list, but sort the same list object it received, and return it. It is
    #​​​​‌‌‌​‌‌‌‌‌​ allowed, however, to copy values to another list and use it to get the
    #​​​​‌‌‌​‌‌‌‌‌​ given list sorted. Note that this will take extra memory.

    #​​​​‌‌‌​‌‌‌‌‌​ The solution must be fast in order to complete the biggest sorting
    #​​​​‌‌‌​‌‌‌‌‌​ problems in time before the time runs out and the evaluator
    #​​​​‌‌‌​‌‌‌‌‌​ terminates the attempt.

    #​​​​‌‌‌​‌‌‌‌‌​ If you are implementing a recursive mergesort, remember to
    #​​​​‌‌‌​‌‌‌‌‌​ divide only up until a certain sublist size, eg. 20, and then sort
    #​​​​‌‌‌​‌‌‌‌‌​ the sublist with another method, eg. selection sort. Dividing and
    #​​​​‌‌‌​‌‌‌‌‌​ recursing up until sublists of size 1 is not effective!

    n = len(lst)

    if n > 1:
        middle = n // 2
        left = lst[0:middle]
        right = lst[middle:n]

        my_sort(left)
        my_sort(right)

        i = 0
        j = 0

        sorted_list = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        while i < len(left):
            sorted_list.append(left[i])
            i += 1

        while j < len(right):
            sorted_list.append(right[j])
            j += 1

        for i in range(len(lst)):
            lst[i] = sorted_list[i]

        return lst

    else:
        return lst





        """
        
        while i + j < len(lst):
            if j == len(right) or (i < len(left) and left[i] < right[j]):
                lst[i + j] = left[i]
                i += 1
            else:
                lst[i + j] = right[j]
                j += 1
        return lst
        
        """