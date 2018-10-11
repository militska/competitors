from Facade import Facade
from Singleton import Singleton


class Competition(metaclass=Singleton):
    speed_wind = 0
    cars = []
    facade = None
    instance = None
    # для демонстрации
    need_set_car = True

    def __init__(self):
        print("* * * Competitions.__init__ * * *")
        self.set_init_data()

    def set_speed_wind(self):
        self.speed_wind = self.facade.get_speed_wind()

    def set_cars(self):
        data = self.facade.get_data()
        for car_name in data:
            car = self.facade.create_car(
                car_name,
                data[car_name]['max_speed'],
                data[car_name]['drag_coef'],
                data[car_name]['time_to_max']
            )

            self.cars.append(car)

    def set_init_data(self):
        self.facade = Facade()
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
