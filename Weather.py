from random import randint


# методы пустышки, нужны для демонстрации пркоси и фасада

class Weather:
    speed_wind = 0

    def __init__(self):
        self.speed_wind = randint(0, 40)

    def get_speed_wind(self):
        return self.speed_wind

    def get_random_wind(self):
        pass

    def get_name_current_wind(self):
        pass

    def rename_name_current_wind(self):
        pass

    def get_next_wind(self):
        pass
