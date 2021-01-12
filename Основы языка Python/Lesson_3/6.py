def int_func(input_text):
    return input_text.title()


text = input('Введите слова, для преобразования:\n')
print(f'Преобразованный текст:\n{int_func(text)}')