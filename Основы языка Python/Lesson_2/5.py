my_list = [7, 5, 3, 3, 2]

print(f'Структура "Рейтинг" из натуральных не возрастающих чисел.\n'
      f'Вы можете добавлять в набор дополнительные натуральные числа.\n')

while True:
    print(f'В данный момент нобор чисел следующий:\n{my_list}\n')
    menu_point = input('1. Добавить натуральное число.\n'
                       '2. Выход.\n'
                       '--> ')
    if menu_point == '1':
        user_char = input('Какое число вы хотите добавить?\n -->')
        if user_char.isdigit():
            new_char = int(user_char)
            my_list.append(new_char)
            my_list.sort(reverse=True)
        else:
            print('Нужно было указать натуральное число!\n')
    elif menu_point == '2':
        quit()
    else:
        print('Неверный ввод.')
