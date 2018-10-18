from modules.weather.WhetherProxy import WhetherProxy
from modules.car.CarFactory import CarFactory
from modules.car.Data import Data


# называть класс паттерном неправильно
class Facade:

    car_factory = None

    def __init__(self):
        self.car_factory = CarFactory()

    def get_speed_wind(self):
        weather = WhetherProxy()
        return weather.get_speed_wind()

    def get_data(self):
        data = Data()
        return data.get_data_car()

    def create_car(self, name, params):
        return self.car_factory.create(name, params)
