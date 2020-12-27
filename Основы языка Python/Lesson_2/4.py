user_input = input('Введите чего-нибудь, а я разделю это на части по пробелам'
                   '(Но если слово будет длинее 10 букв, я его обрежу):'
                   '\n--> ')
words = []
words = user_input.split()

for i, word in enumerate(words):
    print(f'{i + 1} слово - "{word[0:10]}"')
