month_list = ['Январь', 'Февраль', 'Март', 'Апрель',
              'Май', 'Июнь', 'Июль', 'Август',
              'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

seasons_list = ['Зима', 'Зима', 'Весна', 'Весна',
                'Весна', 'Лето', 'Лето', 'Лето',
                'Осень', 'Осень', 'Осень', 'Зима']

seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна',
                5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
                9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}


print('Программа для определения времени года по номеру месяца.')
while True:
    menu_point = input(f'Выберите вариант решения:\n'
                        f'1. Решение через список.\n'
                        f'2. Решение через словарь.\n'
                        f'3. Выход.\n'
                        f'--> ')
    if menu_point == '1':
        user_answer = input('Введите номер месяца: ')
        if user_answer.isdigit():
            month = int(user_answer)
            if month > 12 or month < 1:
                print('\nВ году 12 месяцев...\n')
            else:
                print(f'\nМесяц - {month_list[month - 1]}.\n'
                      f'Время года - {seasons_list[month - 1]}.\n')
        else:
            print('Неверный ввод.\n')
    elif menu_point == '2':
        user_answer = input('Введите номер месяца: ')
        if user_answer.isdigit():
            month = int(user_answer)
            if month > 12 or month < 1:
                print('\nВ году 12 месяцев...\n')
            else:
                print(f'\nЭто {seasons_dict.get(month)}.\n'
                      f'И кстати это {month_list[month - 1]}.\n')
        else:
            print('Неверный ввод.\n')
    elif menu_point == '3':
        quit()
    else:
        print('Неверный ввод.\n')
