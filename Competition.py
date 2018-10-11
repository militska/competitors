import json
from WhetherFacade import WhetherFacade
from Car import Car


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Competition(metaclass=Singleton):
    speed_wind = 0
    cars = []
    result_table = []
    instance = None
    need_set_car = True

    def __init__(self):
        print("* * * Competitions.__init__ * * *")
        self.set_init_data()

    def set_speed_wind(self):
        weather = WhetherFacade()
        self.speed_wind = weather.get_speed_wind()

    def set_cars(self):
        json_data = open('data_cars.json').read()
        data = json.loads(json_data)

        for car_name in data:
            car_object = Car()
            car_object.name = car_name
            car_object.max_speed = data[car_name]['max_speed']
            car_object.drag_coef = data[car_name]['drag_coef']
            car_object.time_to_max = data[car_name]['time_to_max']

            self.cars.append(car_object)

    def set_init_data(self):
        self.set_speed_wind()
        if (self.need_set_car):
            self.set_init_car_data()

    def set_init_car_data(self):
        self.set_cars()

    def start(self, distance):
        for car in self.cars:
            competitor_time = 0

            for distance in range(distance):
                _wind_speed = self.speed_wind

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > self.speed_wind:
                        _speed -= (car.drag_coef * self.speed_wind)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (car.name, competitor_time))
