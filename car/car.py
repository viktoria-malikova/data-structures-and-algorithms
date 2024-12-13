# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Class to describe a car object
#​​​​‌‌‌​‌‌‌‌‌​ A car has the following attributes: max_tank, tank, consumption, mileage and id

class Car:

    def __init__(self, consumption, name = "unregistered vehicle"):
        self.max_tank = 40
        self.tank = self.max_tank # tank is full when delivered from factory
        self.consumption = consumption
        self.mileage = 0.0
        self.id = name

    #​​​​‌‌‌​‌‌‌‌‌​ Return mileage
    def get_mileage(self):
        return self.mileage

    #​​​​‌‌‌​‌‌‌‌‌​ Return tank
    def get_tank_level(self):
        return self.tank

    #​​​​‌‌‌​‌‌‌‌‌​ Drive the wanted distance
    def drive(self, distance):
        max_distance = self.tank / self.consumption * 100
        if max_distance < distance:
            self.mileage += max_distance
            self.tank = 0
            return max_distance
        else:
            self.mileage += distance
            self.tank -= distance * self.consumption / 100
            return distance

    #​​​​‌‌‌​‌‌‌‌‌​ Refuels the car
    def refuel(self, amount):
        self.tank += min(amount, self.max_tank - self.tank)
        return self.tank


#​​​​‌‌‌​‌‌‌‌‌​ Class to describe a car track
#​​​​‌‌‌​‌‌‌‌‌​ A car track has the following attributes: name, distance, cars and nof_cars
#​​​​‌‌‌​‌‌‌‌‌​ Fill in the missing methods

class CarTrack:

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance    # distance of the car track
        self.cars = []              # cars driving on the track (Car-objects)
        self.nof_cars = 0

    #​​​​‌‌‌​‌‌‌‌‌​ Returns the distance of the car track
    def get_distance(self):
        return self.distance

    #​​​​‌‌‌​‌‌‌‌‌​ Returns the list containing the cars in the car track
    def get_cars(self):
        return self.cars

    #​​​​‌‌‌​‌‌‌‌‌​ Returns the number of cars in the car track
    def get_nof_cars(self):
        return self.nof_cars

    #​​​​‌‌‌​‌‌‌‌‌​ Add a car to the car track and return the number of cars in the track
    def add_car(self, car):
        self.cars.append(car)
        return len(self.cars)

    #​​​​‌‌‌​‌‌‌‌‌​ Count and return the average consumption of the race cars
    def count_avg_consumption(self):
        yhteensa = 0
        for i in self.cars:
            yhteensa += i.consumption
        average = yhteensa/len(self.cars)
        return average

    #​​​​‌‌‌​‌‌‌‌‌​ Return the car with the biggest mileage
    def get_winner(self):
        if len(self.cars) == 0:
            return None
        else:
            max = self.cars[0]
            for i in self.cars:
                if i.get_mileage() > max.get_mileage():
                    max = i
            return max

    #​​​​‌‌‌​‌‌‌‌‌​ Count how many rounds a car drove, round down to the nearest integer
    def count_rounds(self, car):
        rounds = int(car.get_mileage() / self.distance)
        return rounds