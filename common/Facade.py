from modules.weather.WhetherProxy import WhetherProxy
from modules.car.CarFactory import CarFactory
from modules.car.Data import Data


# называть класс паттерном неправильно
class Facade:

    def get_speed_wind(self):
        weather = WhetherProxy()
        return weather.get_speed_wind()

    def get_data(self):
        data = Data()
        return data.get_data_car()

    def create_car(self, name, params):
        return CarFactory(name, params).create_car()
