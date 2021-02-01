class Road:

    _length = None
    _width = None

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    def calc(self, mass, thick):
        self.mass = mass
        self.thick = thick
        result = (Road._width * Road._length * mass * thick) / 1000
        return result


def main():
    print('Введите данные для рассчета: ')
    for key in data.keys():
        data[key] = input(f'{key}: ')
        try:
            data[key] = int(data[key])
        except ValueError:
            print('Необходимо вводить числа!')
            main()
    val = [i for i in data.values()]
    new_road = Road(*val[:2])
    total = new_road.calc(*val[2:])
    print(f'Потребуется {int(total)}т асфальта.')


data = {'Длина дороги (м)': 0,
        'Ширина дороги (м)': 0,
        'Масса асфальта на 1 кв.мб (кг)': 0,
        'Толщина полотна (см)': 0}


main()





