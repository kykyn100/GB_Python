proceeds = int(input('Укажите размер выручки Фирмы: '))
costs = int(input('Укажите размер издержек Фирмы: '))

if proceeds < costs:
    print('Фирма работает в убыток.')
elif proceeds > costs:
    print('Фирма приносит прибыль.')
    profit = proceeds - costs
    print(f'Прибыль составляет: {profit}')
    prof_proceeds = (profit / proceeds) * 100
    print(f'Рентабельность выручки составляет: {prof_proceeds:.2f}')
    staff = int(input('Укажите количество сотрудников в фирме: '))
    profit_per_employee = profit / staff
    print(f'В расчете на одного сотрудника'
          f' прибыль составляет: {profit_per_employee:.2f}')
else:
    print('Фирма работает в 0.')


