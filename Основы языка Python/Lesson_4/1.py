# -*- coding: utf-8 -*-

from sys import argv


def calc_income(hours, cost, bonus):
    income = (float(hours) * float(cost)) + float(bonus)
    return income


def main():
    total = calc_income(worked_hours, cost_hour, prize)
    print(f'В соответсвии с заданными параметрами,\n'
          f'сотруднику будет начисленно: {total}')


script_name, worked_hours, cost_hour, prize = argv

main()
