import random


def main():
    print("Я загадал слово, попробуй угадать его ")
    error = 0
    word_list = ["Друзья", "монитор"]
    word = random.choice(word_list)
    sicret_word = ["_" for i in range(len(word))]
    while error != 6:
        symbol = input("Введите букву ")
        if symbol not in word.lower():
            error += 1
            drow(error)
        for i in range(len(word)):
            if word[i].lower() == symbol:
                sicret_word[i] = symbol
            continue
        print("".join(sicret_word))
        print()
        if "_" not in "".join(sicret_word):
            new_game = input("Еще раз? д/н")
            if new_game == "д":
                main()
            break

def drow(n):
    if n == 1:
        print("-------\n|     |\n|     o\n|\n|\n|\n|\n|\n--")
    elif n == 2:
        print("-------\n|     |\n|     o\n|     |\n|\n|\n|\n|\n--")
    elif n == 3:
        print("-------\n|     |\n|     o\n|    /|\n|\n|\n|\n|\n--")
    elif n == 4:
        print("-------\n|     |\n|     o\n|    /|\\\n|\n|\n|\n|\n--")
    elif n == 5:
        print("-------\n|     |\n|     o\n|    /|\\\n|    /\n|\n|\n|\n--")
    else:
        print("-------\n|     |\n|     o\n|    /|\\\n|    / \\\n|\n|\n|\n--")
        print("You lose!")
        new_game = input("Еще раз? д/н")
        if new_game == "д":
            main()


if __name__ == "__main__":
    main()