# -*- coding: utf-8 -*-
from itertools import count
with open("3.txt") as f:
    cnt = count(0)
    ave_salary = 0
    for i in f.readlines():
        next(cnt)
        line = i.split(" ")
        ave_salary += int(line[1])
        if int(line[1]) < 20000:
            print(f'{line[0]} получает меньше 20 тыс. рублей.')
    print(f'Средняя зарплата сотрудников '
          f'равна {int(ave_salary / next(cnt))} тыс. рублей.')