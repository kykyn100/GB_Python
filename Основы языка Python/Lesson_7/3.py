class Cell:

    def __init__(self, count):
        self.count = int(count)

    def __str__(self):
        view = '*' * self.count
        return f'{view}    ({self.count})'

    def __add__(self, other):
        a = self.count
        b = other.count
        c = Cell((a + b))
        return c

    def __sub__(self, other):
        a = self.count
        b = other.count
        if self.count < other.count:
            return 'Разность меньше нуля!'
        else:
            c = Cell((a - b))
            return c

    def __mul__(self, other):
        a = self.count
        b = other.count
        c = Cell((a * b))
        return c

    def __truediv__(self, other):
        a = self.count
        b = other.count
        c = Cell(round((a / b), 0))
        return c

    def make_order(self):
        a, b = divmod(self.count, 5)
        print("*****\n" * a + "*" * b)


# Создаем экземпляры
a = Cell(7)
b = Cell(3)
c = Cell(6)
print('Вывод количества ячеек каждой клетки:')
print(f'A клетка:\n{a}')
print(f'B клетка:\n{b}')
print(f'C клетка:\n{c}')
print(f'Сложение клеток A и B:\n{a + b}')
print(f'Разность клеток A и B:\n{a - b}')
print(f'Разность клеток B и C:\n{b - c}')
print(f'Умножение клетов A и B:\n{a * b}')
print(f'Деление клеток A и B:\n{a / b}')
print('Организация ячеек клетки A по рядам:')
a.make_order()
