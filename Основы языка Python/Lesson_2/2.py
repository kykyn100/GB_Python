my_list = []


while True:
    print('Заполните список элементами '
          'и программа поменяет их значения попарно.\n'
          'P.S. В случае если список не четный,'
          ' последний элемент остается неизменным.\n')
    print(f'Сейчас список выглядит так:\n{my_list}')
    user_answer = input(f'Выбирите действие:\n'
                        f'1. Добавить элемент в список.\n'
                        f'2. Поменять значения элементов.\n'
                        f'3. Выйти из программы.\n'
                        f'-->')
    if user_answer == '1':
        user_element = input('Введите новый элемент: ')
        my_list.append(user_element)
    elif user_answer == '2':
        i = 0
        if len(my_list) % 2 != 0:
            for i in range(0, (len(my_list) - 1), 2):
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        else:
            for i in range(0, len(my_list), 2):
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    elif user_answer == '3':
        quit()
    else:
        print('Неверный ввод.\n')
