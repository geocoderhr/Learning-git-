import random

sicret_numbers = random.randint(1, 100)
attempts = 0
max_attempts = 5


print("Добро пожаловать в игру!")
print("Я загадал число от 1 до 100. У тебя 5 попыток чтобы угадать!")


while attempts < max_attempts:
    try:
        guess = int(input("Введи ваше предположение:"))
    except ValueError:
        print("Ввод не корректный. Введи целое число!")
        continue

    attempts += 1

    if guess < sicret_numbers:
       print("Слишком мало!")
    elif guess > sicret_numbers:
        print("Слишком много!")
    else:
        print(f"Поздравляю, ты угадал число {sicret_numbers} за {attempts} попыток!")
        break
else:
    print(f"Не угадал. Загаданное число: {sicret_numbers}")