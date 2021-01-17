# -*- coding: utf-8 -*-


from random import randint


with open("5.txt", "w") as f:
    num = [randint(1, 100) for i in range(1, 11)]
    f.writelines(" ".join(map(str, num)))
    print(f'Сумма всех сгенерированных чисел равна {sum(num)}')
