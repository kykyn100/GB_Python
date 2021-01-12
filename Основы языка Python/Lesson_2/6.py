products_list = []
position = 0
blank = {"название": "", "цена": "", "количество": "", "ед": ""}

print('Программа для структурирования и анализа товаров.')

while True:
    menu_point = input('Выберите действие:\n'
                       '1. Добавить товар в программу.\n'
                       '2. Вывести список товаров.\n'
                       '3. Провести аналитику по товарам.\n'
                       '4. Выход.\n'
                       '--> ')
    if menu_point == '1':
        new_product = []
        new_blank = {}
        position += 1
        for i in blank.keys():
            user_input = input(f'Заполните поле "{i}": ')
            new_blank[i] = user_input
        new_product = [position, new_blank]
        products_list.append(tuple(new_product))
    elif menu_point == '2':
        for i in products_list:
            print(i)
    elif menu_point == '3':
        new_report = {}
        for product in range(len(products_list)):
            for new_key in products_list[product][1].keys():
                new_report.setdefault(new_key)
                new_report[new_key] = []
        for product in range(len(products_list)):
            for key, value in products_list[product][1].items():
                if value not in new_report[key]:
                    new_report[key].append(value)
                    '''
                    Как я понял из примера в задании, повторений в значениях 
                    быть не должно, а set() делать мне уже лень. =) 
                    По этому такая проверка ¯\_(ツ)_/¯.
                    '''
        for key, value in new_report.items():
            print(f'{key}: {value}')
        print()
    elif menu_point == '4':
        quit()
    else:
        print('Неверный ввод.')
