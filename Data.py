import json

# будем счиать это класс-база данных
class Data:

    def get_data_car(self):
        json_data = open('data_cars.json').read()
        return json.loads(json_data)
