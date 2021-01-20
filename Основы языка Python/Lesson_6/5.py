class Stationery:

    title = 'Название'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    title = 'Ручка'

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}.')


class Pencil(Stationery):

    title = 'Карандаш'

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}.')


class Handle(Stationery):

    title = 'Маркер'

    def draw(self):
        print(f'Запуск отрисовки с помощью {self.title}.')


thing = Stationery()
thing.draw()

thing_a = Pen()
thing_a.draw()

thing_b = Pencil()
thing_b.draw()

thin_c = Handle()
thin_c.draw()