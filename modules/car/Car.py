# класс нарушает принцип YAGNI
# нужен для намереного усложнения/применения паттернов, aka AR class

class Car:
    name = ''
    max_speed = ''
    drag_coef = ''
    time_to_max = ''

    def delete(self):
        pass

    def get(self, name):
        pass

    def get_prev(self, name):
        pass
