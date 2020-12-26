print('Программа для перевода времени в секундах в формат "чч:мм:сс".')
total_seconds = int(input('Введите время в секундах: '))

total_minutes = total_seconds // 60
seconds = total_seconds % 60
hours = total_minutes // 60
minutes = total_minutes % 60

print(f'{total_seconds} секунд это: {hours:02}:{minutes:02}:{seconds:02}')

