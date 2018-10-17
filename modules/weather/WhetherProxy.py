from modules.weather.Weather import Weather


class WhetherProxy:
    weather_class = None

    def __init__(self):
        self.weather_class = Weather()

    def get_speed_wind(self):
        return self.weather_class.speed_wind
