from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):

    def __init__(self, name, attr):
        self.name = name
        self.v = attr

    @property
    def calc(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, attr):
        self.name = name
        self.h = attr

    @property
    def calc(self):
        return 2 * self.h + 0.3


a = Coat('Черное пальто', 12)
b = Suit('Костюм в полосочку', 3)
print(f'Для пошива {a.name} потребуется {a.calc:.3} едениц ткани.')
print(f'Для пошива {b.name} потребуется {b.calc:.3} едениц ткани.')
total = a.calc + b.calc
print(f'Общее количество ткани, которое требуется: {total:.3}')