def stat(a,b): # відкриває файл статистики та записує туди результат

    with open('statistic.txt', 'a') as file:
        file.write(f"{a}. Кількість спроб:{b}'\n'")
    return

def static(): # зчитує статистику
    with open('statistic.txt', 'r') as file:
        return file.read()