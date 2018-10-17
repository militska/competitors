from common.Facade import Facade
from components.Singleton import Singleton
from competition.DefaultStrategy import DefaultStrategy
from competition.ContextStrategy import ContextStrategy


class Competition(metaclass=Singleton):
    speed_wind = 0
    cars = []
    facade = None
    strategy_competition = DefaultStrategy()

    def __init__(self):
        print("* * * Competitions.__init__ * * *")
        self.facade = Facade()
        self.set_init_data()

    def set_cars(self):
        facade = self.facade
        data = facade.get_data()
        for car_name in data:
            self.cars.append(
                facade.create_car(car_name, data[car_name])
            )

    def set_init_data(self):
        self.speed_wind = self.facade.get_speed_wind()
        self.set_cars()

    def start(self, distance):
        for car in self.cars:
            contx = ContextStrategy(self.strategy_competition)
            competitor_time = contx.execute(context=self, car=car, distance=distance)

            print("Car <%s> result: %f" % (car.name, competitor_time))
