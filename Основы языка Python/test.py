class Worker:

    name = None
    surname = None
    position = None
    _income = {"Оклад": None, "Премия": None}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["Оклад"] = wage
        self._income["Премия"] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {Worker.name} {Worker.surname}')

    def get_total_income(self):
        pass


slave = Worker('Вася', 'Пупкин', 'Раб', '10', '0')
print(dir(slave))
print(slave.position)
print(slave.name)
print(slave.surname)
print('*' * 10)
print(Worker.surname)
print(Worker.name)
print(Worker.position)