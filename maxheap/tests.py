# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import random
import pprint

from maxheap import MaxHeap


class CompareTasksError(Exception): pass

class Task:
    """
    Arbitrary class for testing purposes.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Task({0!r})".format(self.name)

    def _exception_operator(self, other):
        raise CompareTasksError("Comparing Task objects is not required in this exercise.")
    __lt__ = _exception_operator
    __le__ = _exception_operator #Wow
    __eq__ = _exception_operator
    __ne__ = _exception_operator
    __ge__ = _exception_operator
    __gt__ = _exception_operator


TASK_NAMES = (
    "Wash dishes",
    "Eat food",
    "Go to Maari",
    "Do math assignments",
    "Play Chopin's Etude Op. 25, No. 9 in G-flat major",
    "Watch silly reality show",
    "Apply for work",
    "Sleep",
    "Talk to your plants",
    "Go jogging while listening to some brutal black metal",
    "Clean room",
    "Dance",
    "Tell your roommate that life is pretty nice",
    "Do something crazy"
)

def generate_tasks_with_priorities(task_names=TASK_NAMES):
    """Returns a list with random length containing tuples (p, task)."""
    task_count = random.randint(3, len(task_names))
    random_tasks = random.sample(task_names, task_count)
    #​​​​‌‌‌​‌‌‌‌‌​Take p from curr iteration count provided by enumerate
    return [( task_count - (p+1), Task(task_name)) for p, task_name in enumerate(random_tasks)]


def heap_array_to_string(heap_array, msg=None):
    if msg is None:
        msg = "Starting at index 0, the heap array in your solution looks like this:"
    return msg + '\n' + pprint.pformat(heap_array)


#​​​​‌‌‌​‌‌‌‌‌​TODO: add test for initializing with sequence, take notes from grader_tests

class TestMaxHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MaxHeap()

    def test_clear(self):
        """Calling clear for a heap sets its array to an empty list and size to zero. (0p)"""
        self.heap.array = [(1, 1)]
        self.heap.size = 1

        self.heap.clear()

        self.assertListEqual(
            [],
            self.heap.array,
            "heap.clear() should set heap.array to an empty list."
        )
        self.assertEqual(
            0,
            self.heap.size,
            "heap.clear() should set heap.size to 0."
        )


    def test_empty_heap_size(self):
        """The size of an empty heap is zero. (0p)"""
        self.assertEqual(
            0,
            self.heap.size,
            "The size of an empty heap should be zero."
        )

    def test_empty_heap_is__empty(self):
        """is_empty returns True for an empty heap. (0p)"""
        self.assertTrue(
            self.heap.is_empty(),
            "Calling is_empty should return True for an empty heap instance."
        )

    def test_higher_priority_high_low(self):
        """_higher_priority returns True when comparing an element with a higher priority to an element with a lower priority. (1p)"""
        self.heap.array = [(2, 'important'), (1, 'not important')]
        self.assertTrue(
            self.heap._higher_priority(0, 1),
            "_higher_priority priority should return True when comparing {0} to {1}"
            .format(self.heap.array[0], self.heap.array[1])
        )

    def test_higher_priority_low_high(self):
        """_higher_priority returns False when comparing an element with a lower priority to an element with a higher priority. (1p)"""
        self.heap.array = [(2, 'important'), (1, 'not important')]
        self.assertFalse(
            self.heap._higher_priority(1, 0),
            "_higher_priority priority should return False when comparing {0} to {1}"
            .format(self.heap.array[1], self.heap.array[0])
        )


    def test_size_after_insert(self):
        """Inserting values into the heap increments the size counter. (1p)"""
        inserted_tasks = generate_tasks_with_priorities()
        for pair in inserted_tasks:
            self.heap.insert(pair)

        inserted_count = len(inserted_tasks)
        current_size = self.heap.size
        self.assertEqual(
            inserted_count,
            current_size,
            "After inserting {0} pairs, the size of the heap should be {0}, not {1}"
            .format(inserted_count, current_size) + '\n' +
            heap_array_to_string(self.heap.array)
        )


    def test_empty_heap_top(self):
        """Calling top on an empty heap returns None. (1p)"""
        self.assertIsNone(
            self.heap.top(),
            "Calling heap.top() should return None for an empty heap instance."
        )

    def test_empty_heap_pop(self):
        """Calling pop on an empty heap raises an exception. (1p)"""
        msg = "Calling heap.pop() should raise a RuntimeError for an empty heap instance."
        with self.assertRaises(RuntimeError, msg=msg):
            self.heap.pop()


    def test_top_after_insert(self):
        """Calling top always returns the object with the greatest priority value. (1p)"""

        inserted_tasks = generate_tasks_with_priorities()

        shuffled = list(inserted_tasks)
        random.shuffle(shuffled)

        for pair in shuffled:
            self.heap.insert(pair)

        expected_value = inserted_tasks[0][1]
        returned_value = self.heap.top()
        self.assertIs(
            returned_value,
            expected_value,
            "Calling top should have returned {0}, not {1}."
            .format(expected_value, returned_value) + '\n' +
            heap_array_to_string(self.heap.array)
        )


    def test_pop_after_insert(self):
        """Calling pop always returns the object with the greatest priority value and removes it from the heap. (1p)"""

        inserted_tasks = generate_tasks_with_priorities()

        shuffled = list(inserted_tasks)
        random.shuffle(shuffled)

        for pair in shuffled:
            self.heap.insert(pair)

        for i, pair in enumerate(inserted_tasks):
            assertmsg = "Before calling pop, the heap array in your solution looked like this:"
            heap_array_before_pop = self.heap.array[:]

            popped_value = self.heap.pop()
            expected_value = pair[1]
            self.assertIs(
                popped_value,
                expected_value,
                "Calling pop should have returned {0}, not {1}."
                .format(expected_value, popped_value) + '\n' +
                heap_array_to_string(heap_array_before_pop, assertmsg)
            )

            removed_count = i+1
            self.assertEqual(
                len(self.heap.array),
                len(inserted_tasks) - removed_count,
                "Calling pop should remove the object with the greatest priority value from the heap array." +
                '\n' +
                heap_array_to_string(heap_array_before_pop, assertmsg)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)

