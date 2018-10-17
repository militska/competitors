import json


# будем счиать это класс-база данных
class Data:

    data = None

    def __init__(self):
        self.data = open('./modules/car/data_cars.json').read()

    def get_data_car(self):
        return json.loads(self.data)
