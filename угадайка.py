import random


def valid(right):
    try:
        right = int(right)
        return int(right)
    except ValueError:
            print(f"А может быть все-таки введем целое число?")
            main()


def main():
    print("Привет в числовой угадайке!\n")
    right = input("Число от 1 до ")
    print("Введите число или q для выхода")
    choice_num(random_num(valid(right)))


def random_num(right):
    number = random.randrange(1, right)  # ЗАГАДАННОЕ ЧИСЛО
    return number


def choice_num(number):
    count = 1
    while True:
        x = input()
        try:
            if int(x) == int(number):
                print(f"ВЫ угадали! {number} с {count} попытки. Ещё раз?")
                count = 1
                question = input()
                if question == "да":
                    main()
                elif question != "да":
                    return None
            elif int(x) < int(number):
                count += 1
                print("Ваше число меньше загаданного, попробуйте еще разок")
            else:
                count += 1
                print("Ваше число больше загаданного, попробуйте еще разок")
        except ValueError:
            pass


if __name__ =='__main__':
    main()

