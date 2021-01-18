from itertools import count
from itertools import cycle


def generator(start, stop):
    new_list = []
    gen = count(start, 1)  # вот тут делаю итератор
    while True:
        new_list.append(next(gen))  # вот тут по одному добавляю в список
        if max(new_list) == stop:
            return new_list


def repeater(stop, u_list):
    rep_list = []
    rep = cycle(u_list)
    cnt = 0
    while True:
        rep_list.append(next(rep))
        cnt += 1
        if cnt == stop:
            return rep_list


list_start = int(input('Введите число с которого начнется генерация списка: '))
list_stop = int(input('Введите максимальное число для генерации списка: '))
user_list = generator(list_start, list_stop)
print(f'Ваш список:\n{user_list}')
repeat = int(input('Сколько элементов из списка повторить? '))
print(f'Теперь все выглядит так:\n {repeater(repeat, user_list)}')
