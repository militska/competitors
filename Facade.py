from WhetherProxy import WhetherProxy
from Car import Car
from Data import Data


# называть класс паттерном неправильно
class Facade:

    def get_speed_wind(self):
        weather = WhetherProxy()
        return weather.get_speed_wind()

    def get_data(self):
        data = Data()
        return data.get_data_car()

    # предача параметров таким образом не оч корретно, лучше массивом или объектом
    def create_car(self, name, max_speed, drag_coef, time_to_max):
        car = Car()
        car.name = name
        car.max_speed = max_speed
        car.drag_coef = drag_coef
        car.time_to_max = time_to_max
        return car
