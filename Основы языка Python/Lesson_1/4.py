print('Программа для определения наибольшей цифры в целом положительном числе.')
numbers = int(input('Введите целое положительное число: '))
max_num = 0

while numbers > 0:
    num = numbers % 10
    numbers = numbers // 10
    if num > max_num:
        max_num = num
print(f'Самая большая цифра в числе - {max_num}')

