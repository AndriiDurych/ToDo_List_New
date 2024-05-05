import start, game, rules, statistics
import random
print("Вітаю вас з початком гри ToDo_List")

while True: # цикл гри, в якому перевіряються введені команди та інші дії
    print(start.start_Todo())  # виводить нагадування зі списком команд
    command = start.start_input() # вводить команду користувачем і перетворює її на список
    if command == 'вихід':   # перевіряє на правильність вводу команди
        print("Гра закінчена!!!")
        break
    elif command == 'правила': # перевіряє на правильність вводу команди та виводить правила
        rules.rules()
        continue
    elif command == 'статистика': # перевіряє на правильність вводу команди та виводить статистику
        print(statistics.static())
    elif command == 'старт': # перевіряє на правильність вводу команди та починає гру
        klych = str(game.klch())
        k = list(klych)
        l2 = 1
        while True:  # забеспечує постійне введення користувачем відповідей
            guess = game.game()
            list_pr = ['1', '2', '3', '4', '5', '6']
            a = 1111
            r = ''
            t = ''
            k = list(klych)
            gues = list(guess)
            if guess == 'вихід': # перевіряє на правильність вводу команди
                print("Ви вийшли з гри. Спробувати ще раз?")
                break
            elif len(guess) != 4: # перевіряє на правильність вводу команди
                print("Ви ввели некорректну здогадку. Дивіться правила гри!!!")
                break
            elif a == 1111: # перевіряє на правильність вводу команди
                for i in range(4):
                    if gues[i] in list_pr:
                        a = 1111
                    else:
                        a = 0
                        break
            if a == 0:
                print("Ви ввели некорректну здогадку. Дивіться правила гри!!!")
                break
            for i in range(4): # вираховує підказку для гравця
                if gues[i] == k[i]:
                    r += '+'
                    k[i] = 'н'
                    gues[i] = 'е'
            for i in range(4):
                if gues[i] in k:
                    t += '-'
                    for i in range(4):
                        if gues[i] == k[i]:
                            k[i] = 'н'
                            gues[i] = 'е'
            r += t
            print(r) # Виводить підказку
            if r == '++++':
                l1 = "Перемога"
                print(f"Ви виграли!!!\n Ключ: {klych}\n Зіграти ще раз?")
                statistics.stat(l1, l2)
                break
            l2 += 1
    else:
        print("Ви ввели неправильну команду!!!")

