from modules.car.Car import Car
from components.Singleton import Singleton


class CarFactory(metaclass=Singleton):

    def create(self, name, params):
        car = Car()
        car.name = name
        car.max_speed = params['max_speed']
        car.drag_coef = params['drag_coef']
        car.time_to_max = params['time_to_max']
        return car
