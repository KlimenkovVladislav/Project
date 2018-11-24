# coding=utf-8
polsovateli = {}
while True:
    def regestraciya():
        ima = input('Введите ваше имя: ')
        parol=input('Введите ваш пароль: ')
        pisma = {}
        polsovatel = [parol,pisma]
        polsovateli[ima] = polsovatel
        print('''Вы зарегестрировали ваш электронный ящик.
Здравствуйте ''', ima, '.')
        return ima


    def vhod():
        ima = input('Введите ваше имя: ')
        parol=input('Введите ваш пароль: ')
        if polsovateli[ima][0]==parol:
            print('''Вы вошли в ваш электронный ящик.
Здравствуйте ''', ima, '.')
            return ima
        else:
            print('Вы ввели неправельное имя пользователя или пароль.')
            oshibka='Ошибка'
            return oshibka



    def otpravit_pismo(ima):
        ima_poluchatela = input('Введите имя получателя: ')
        if ima_poluchatela in polsovateli:
            text_pisma = input('Введите текст письма: ')
            polsovateli[ima_poluchatela][1][text_pisma] = ima
            print('Ваше письмо отправлено.')
        else:
            print('Получателя с таким именем не обнаружено.')


    def posmotret_pisma(ima):
        print('Ваши письма: ', polsovateli[ima][1])


    while True:
        print('''Добро пожаловать в электронную почту.
Выберите следующее действие: войти в свой почтовый ящик (1),
зарегестрировакть свой почтовый ящик (2),
Выйти из электронной почты (3).''')
        deistvie_1 = input('Введите число: ')
        if deistvie_1 == '1':
            ima = vhod()
            if ima=='Ошибка':
                continue
            else:
                while True:
                    print('''Вы находитесь в вашем почтовом ящике.
Выберите следующее действие: отправить письмо (1),
посмотреть ваши письма (2), 
выйти из почтового ящика (3).''')
                    deistvie_2 = input('Введите число: ')

                    if deistvie_2 == '1':
                        otpravit_pismo(ima)

                    if deistvie_2 == '2':
                        posmotret_pisma(ima)

                    if deistvie_2 == '3':
                        print('Вы вышли из вашего почтового ящика.')
                        break

        if deistvie_1 == '2':
            ima = regestraciya()
            while True:
                print('''Вы находитесь в вашем почтовом ящике.
Выберите следующее действие: отправить письмо (1),
посмотреть ваши письма (2), 
выйти из почтового ящика (3).''')
                deistvie_2 = input('Введите число: ')

                if deistvie_2 == '1':
                    otpravit_pismo(ima)

                if deistvie_2 == '2':
                    posmotret_pisma(ima)

                if deistvie_2 == '3':
                    print('Вы вышли из вашего почтового ящика.')
                    break
        if deistvie_1 == '3':
            print('Вы вышли из электронной почты.')
            break