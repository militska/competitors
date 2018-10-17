class DefaultStrategy:

    def execute(self, context, car, distance):
        competitor_time = 0
        for distance in range(distance):
            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / car.time_to_max) * car.max_speed
                if _speed > context.speed_wind:
                    _speed -= (car.drag_coef * context.speed_wind)

            competitor_time += float(1) / _speed

        return competitor_time
