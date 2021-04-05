from random import randint, choice


class Car:

    speed = 0
    color = None
    name = None
    is_police = bool

    def go(self):
        print(f'Автомобиль поехал.')

    def stop(self):
        print(f'Автомобиль остановился.')

    def turn(self, direction):
        print(f'Автомобиль повернул на {direction}.')

    def show_speed(self):
        print(f'Автомобиль движется со скоростью {self.speed}')


class TownCar(Car):

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        print(f'Автомобиль движется со скоростью {self.speed}')
        if self.speed > 60:
            print('Необходимо снизить скорость до 60!')


class SportCar(Car):

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


class WorkCar(Car):

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        print(f'Автомобиль движется со скоростью {self.speed}')
        if self.speed > 40:
            print('Необходимо снизить скорость до 40!')


class PoliceCar(Car):

    is_police = True

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


def attr_gen():
    a = raw_data[0]
    b = choice(raw_data[1])
    c = choice(raw_data[2])
    return [a, b, c]


raw_data = [randint(1, 180),
            ['Синий', 'Красный', 'Желтый', 'Черный', 'Белый'],
            ['Mazda', 'Golf', 'BMW', 'AUDI', 'ZAZ'],
            ['Север', 'Юг', 'Запад', 'Восток']]

print('Проверка Родительского класса:')
car = Car()
print(f'Название автомобиля: {car.name}')
print(f'Цвет автомобиля: {car.color}')
print(f'Скорость автомобиля: {car.speed}')
print(f'Это полицейский автомобиль? - {car.is_police}')
car.go()
car.show_speed()
car.turn(choice(raw_data[3]))
car.stop()
print('*' * 40)

print('Создаем экземпляры классов и проверяем их значения:')
car_a = TownCar(*attr_gen())
print('-' * 40)
print(f'Название автомобиля: {car_a.name}')
print(f'Цвет автомобиля: {car_a.color}')
print(f'Скорость автомобиля: {car_a.speed}')
print(f'Это полицейский автомобиль? - {car_a.is_police}')
car_a.go()
car_a.show_speed()
car_a.turn(choice(raw_data[3]))
car_a.stop()

car_b = SportCar(*attr_gen())
print('-' * 40)
print(f'Название автомобиля: {car_b.name}')
print(f'Цвет автомобиля: {car_b.color}')
print(f'Скорость автомобиля: {car_b.speed}')
print(f'Это полицейский автомобиль? - {car_b.is_police}')
car_b.go()
car_b.show_speed()
car_b.turn(choice(raw_data[3]))
car_b.stop()

car_c = WorkCar(*attr_gen())
print('-' * 40)
print(f'Название автомобиля: {car_c.name}')
print(f'Цвет автомобиля: {car_c.color}')
print(f'Скорость автомобиля: {car_c.speed}')
print(f'Это полицейский автомобиль? - {car_c.is_police}')
car_c.go()
car_c.show_speed()
car_c.turn(choice(raw_data[3]))
car_c.stop()

car_d = PoliceCar(*attr_gen())
print('-' * 40)
print(f'Название автомобиля: {car_d.name}')
print(f'Цвет автомобиля: {car_d.color}')
print(f'Скорость автомобиля: {car_d.speed}')
print(f'Это полицейский автомобиль? - {car_d.is_police}')
car_d.go()
car_d.show_speed()
car_d.turn(choice(raw_data[3]))
car_d.stop()
