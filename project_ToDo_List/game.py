def game(): # забезперчує ввід відповіді гравцем
    user_input = input("Введіть можливе число '****' або 'вихід':\n")
    return user_input

def guess_number(number): # перетворює відповідь на список
    number_list = list(number)
    return number_list

def klch(): # створює випадковий ключ
    import random
    a1 = random.randint(1, 6)
    a2 = random.randint(1, 6)
    a3 = random.randint(1, 6)
    a4 = random.randint(1, 6)
    a = a1 * 1000 + a2 * 100 + a3 * 10 + a4
    return a
