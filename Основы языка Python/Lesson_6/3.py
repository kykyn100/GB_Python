class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": int(wage), "Премия": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


vasya = Position('Вася', 'Пупкин', 'Инженер', '30000', '7500')
anya = Position('Аня', 'Смутьянова', 'Секретарь', '20000', '5000')
senya = Position('Семен', 'Глухов', 'Начальник', '50000', '10000')

workers = [vasya, anya, senya]

for i in workers:
    print(f'Сотрудник: {i.get_full_name()}\n'
          f'Должность: {i.position}\n'
          f'Доход: {i.get_total_income()} рублей.\n')