class NotNumber(Exception):

    def __init__(self, txt):
        self.txt = txt


user_input = None
raw = []
while user_input != '':
    user_input = input('Введите число, для прекращения нажмите Enter: ')
    if user_input != '':
        try:
            if user_input.isdigit():
                raw.append(user_input)
            else:
                raise NotNumber("Нужно вводить числа!")
        except NotNumber as err:
            print(err)

print(raw)
