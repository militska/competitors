from Weather import Weather


class WhetherFacade:
    wheatherClass = None

    def __init__(self):
        self.wheatherClass = Weather()

    def get_speed_wind(self):
        return self.wheatherClass.speed_wind
