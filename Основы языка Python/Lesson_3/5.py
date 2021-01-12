def sum_input(user_input):
    sub_total = 0
    for i in user_input:
        if i.isdigit():
            sub_total += int(i)
        else:
            return sub_total, 1
    return sub_total, 0


print('Программа будет сумировать введенные числа, '
      'пока вместо числа не будет введен символ "&"')
total_sum = 0
stop_point = 0
while stop_point == 0:
    user_input = input('Введите строку чисел разделяя их пробелами: ')
    input_list = user_input.split()
    sub_sum, stop_point = sum_input(input_list)
    total_sum += sub_sum
    print(f'Сумма введенного: {total_sum}')
