# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the reverse_queue function here below

from queue import Queue

def reverse_queue(queue):

    #​​​​‌‌‌​‌‌‌‌‌​ Given a queue, write a recursive function to reverse it
    #​​​​‌‌‌​‌‌‌‌‌​ Allowed operations are the ones you implemented in the queue class
    #​​​​‌‌‌​‌‌‌‌‌​ such as enqueue, dequeue & is_empty

    if queue.is_empty(): # The simplest case
        return None
    else:
        obj = queue.dequeue()
        reverse_queue(queue)
        queue.enqueue(obj)