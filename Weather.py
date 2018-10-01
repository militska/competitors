from random import randint


class Weather:
    speed_wind = 0

    def __init__(self):
        self.speed_wind = randint(0, 40)

    def get_speed_wind(self):
        return self.speed_wind
