class DefaultStrategy:

    # def execute(self, context, car, distance):
    def execute(self, **kwargs):
        competitor_time = 0
        for distance in range(kwargs.get('distance')):
            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / kwargs.get('car').time_to_max) * kwargs.get('car').max_speed
                if _speed > kwargs.get('context').speed_wind:
                    _speed -= (kwargs.get('car').drag_coef * kwargs.get('context').speed_wind)

            competitor_time += float(1) / _speed

        return competitor_time
