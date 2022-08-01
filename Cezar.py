import string


def asq():
    function = input("Шифруем(ш)/дешифруем(д)? ")
    lang_asq = input("Какой язык используется? ru/eng ")
    step = input("Шаг ")
    text = input("Введите текст для анализа ")
    list_text = [text.index(i) for i in text.split() if i.istitle()]
    if lang_asq == "ru":
        cyrillic_lower = [(lambda c: chr(c))(i) for i in range(1072, 1104)]
        main_alphabet = "".join(cyrillic_lower)
        return function, lang_asq, step, text, main_alphabet, list_text
    else:
        main_alphabet = string.ascii_lowercase
        return function, lang_asq, step, text, main_alphabet, list_text


def main_bloc(function):
    text_new = []
    if function[0] == "ш":
        new_text = ""
        upper = [j for j in range(len(function[3].split())) if function[3].split()[j].istitle()]
        for i in function[3].lower():
            if i not in function[4]:
                new_text += i
                continue
            letter = ord(i) + int(function[2])
            if letter > ord(function[4][-1]):
                letter -= len(function[4])
                new_text += chr(letter)
            else:
                new_text += chr(letter)
        for i in range(len(new_text.split())):
            if i in upper:
                text_new.append(new_text.split()[i].title())
            else:
                text_new.append(new_text.split()[i])
        print(*text_new, end="")
    elif function[0] == "д":
        new_text = ""
        upper = [j for j in range(len(function[3].split())) if function[3].split()[j].istitle()]
        for i in function[3].lower():
            if i not in function[4]:
                new_text += i
                continue
            letter = ord(i) - int(function[2])
            if letter < ord(function[4][0]):
                letter += len(function[4])
                new_text += chr(letter)
            else:
                new_text += chr(letter)
        for i in range(len(new_text.split())):
            if i in upper:
                text_new.append(new_text.split()[i].title())
            else:
                text_new.append(new_text.split()[i])
        print(*text_new, end="")


if __name__ == "__main__":
    main_bloc(asq())
