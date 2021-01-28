with open("1.txt", "a+") as f:
    user_input = "None"
    while user_input != '':
        user_input = input('Введите что-нибудь. Для остановки '
                           'просто нажмите  Enter.\n --> ')
        f.write(user_input + '\n')