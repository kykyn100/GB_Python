print('Программа расчета количества дней тренировок бегуна.')
result = int(input('Укажите сколько километров вы пробежали в первый день: '))
goal = int(input('Укажите планируемую цель в километрах: '))
day = 1

while True:
    print(f'{day}-й день: {result:.2f}')
    day += 1
    result = result + (result / 10)
    if result < goal:
        continue
    elif result > goal:
        print(f'{day}-й день: {result:.2f}')
        break

print(f'Ответ: на {day}-й день спортсмен достиг результата -'
      f' не менее {goal} км.')
