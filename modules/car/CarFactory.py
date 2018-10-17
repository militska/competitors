from modules.car.Car import Car


class CarFactory:
    name = ''
    params = []

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def create_car(self):
        car = Car()
        car.name = self.name
        car.max_speed = self.params['max_speed']
        car.drag_coef = self.params['drag_coef']
        car.time_to_max = self.params['time_to_max']
        return car
