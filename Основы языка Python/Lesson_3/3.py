# Коментарий для создания PR


def sum_two_max(arg1, arg2, arg3):
    all_args = [arg1, arg2, arg3]
    all_args.remove(min(all_args))
    sum_max = sum(all_args)
    return sum_max


input_args = []

for i in range(1, 4):
    user_input = int(input(f'Введите {i} переменную: '))
    input_args.append(user_input)

result = sum_two_max(*input_args)
print(result)