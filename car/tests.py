# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
"""
These local tests can be used to test your implementation of the CarTrack class

Feel free to modify these tests as you wish.
"""

import unittest
from car import Car, CarTrack
import sys


class TestCar(unittest.TestCase):

    def test_01_add_car(self):
        """add_car adds correct cars to the car track and returns amount of cars"""
        test_track = CarTrack("Monaco", 15)
        test_car_1 = Car(10.0, "XXX-123")
        ret = test_track.add_car(test_car_1)
        self.assertEqual(
            ret, 1,
            "add_car should return 1 but it returns {} ".format(ret))

        cars = test_track.get_cars()
        type_error = None
        try:
            self.assertEqual(
                cars[0], test_car_1,
                "get_cars should return car {} but it returns {} ".format(test_car_1, cars[0])
            )
        except TypeError as e:
            type_error = e
        if (type_error != None):
            self.fail(
                ("Got TypeError: {}.\nHint: your " +
                "CarTrack.get_cars() should return a *list* which which " +
                "contains *many* different Car objects.").format(type_error))
            raise type_error

        test_car_2 = Car(7.0, "AAA-456")
        ret = test_track.add_car(test_car_2)

        self.assertEqual(
            ret, 2,
            "add_car should return 2 but it returns {} ".format(ret))

        cars = test_track.get_cars()
        self.assertEqual(
            cars[1], test_car_2,
            "get_cars should return car {} but it returns {} ".format(test_car_2, cars[1])
        )

    def test_02_count_avg_consumption(self):
        """count_avg_consumption returns correct average consumption"""

        test_track = CarTrack("Monaco", 15)
        test_car_1 = Car(10.0, "XXX-123")
        test_car_2 = Car(8.0, "ABC-111")
        test_car_3 = Car(6.0, "GFJ-768")
        test_track.add_car(test_car_1)
        test_track.add_car(test_car_2)
        test_track.add_car(test_car_3)
        ret = test_track.count_avg_consumption()
        self.assertEqual(
        ret, 8.0,
        "avg_consumption should return 8.0, but it returns {}".format(ret))

    def test_03_get_winner(self):
        """get_winner returns the correct car"""

        test_track = CarTrack("Monaco", 15)
        test_car_1 = Car(4.5, "Ferrari")
        test_car_2 = Car(7.2, "BMW")
        test_car_3 = Car(10, "Volvo")
        test_car_4 = Car(6.7, "Toyota")

        test_track.add_car(test_car_1)
        test_track.add_car(test_car_2)
        test_track.add_car(test_car_3)
        test_track.add_car(test_car_4)

        test_car_4.drive(20)
        test_car_1.drive(18)
        test_car_2.drive(15)
        test_car_3.drive(33)


        ret = test_track.get_winner()

        self.assertEqual(
            ret.id, test_car_3.id,
            "get_winner should return {}, but your function returns {}".format(test_car_3.id, ret.id))

    def test_04_count_rounds(self):
        """count_rounds returns the correct amount of rounds driven"""

        test_track = CarTrack("Monaco", 15)
        test_car = Car(6.7, "Toyota")

        test_track.add_car(test_car)

        test_car.drive(33)

        #​​​​‌‌‌​‌‌‌‌‌​ rounds = 33 km / 15 km => 2 full rounds
        ret = test_track.count_rounds(test_car)
        self.assertEqual(
            ret, 2,
            "Function should return 2, but your function returns {}".format(ret))


if __name__ in ("__main__", "tests"):
    import sys
    if sys.version_info.major < 3:
        class VersionError(BaseException): pass
        raise VersionError("You are using Python version {:d}.{:d}, please use version 3 instead."
                           .format(sys.version_info.major, sys.version_info.minor))


#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line
if __name__ == "__main__":
    unittest.main(verbosity = 2)
