import random
import string


def asq():
    pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
    pwd_len = int(input('Какой длины должен быть пароль? '))
    pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? +/- ')
    pwd_costruct(pwd_quantity, pwd_len, pwd_exceptions)


def asq_more(pwd_exception):
    simbol = "il1Lo0O"
    digits = ""
    upper = ""
    lower = ""
    punct = ""
    if pwd_exception == "+":
        pwd_digits = input('Включать ли в пароль цифры от 0 до 9? +/- ')
        if pwd_digits == "+":
            digits = "".join([i for i in string.digits if i not in simbol])
        pwd_uppercase = input('Включать ли в пароль прописные буквы? +/- ')
        if pwd_uppercase == "+":
            upper = "".join([i for i in string.ascii_uppercase if i not in simbol])
        pwd_lowercase = input('Включать ли в пароль строчные буквы? +/- ')
        if pwd_lowercase == "+":
            lower = "".join([i for i in string.ascii_lowercase if i not in simbol])
        pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? +/- ')
        if pwd_punctuation == "+":
            punct = "".join([i for i in string.punctuation if i not in simbol])
    else:
        digits = string.digits
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        punct = string.punctuation
    return [digits, upper, lower, punct]


def pwd_costruct(pwd_quantity, pwd_len, pwd_exceptions):
    pwd = ""
    list_pwd = []
    list_condition = asq_more(pwd_exceptions)
    for i in range(pwd_quantity):
        while len(pwd) != pwd_len:
            for j in list_condition:
                if len(j) != 0 and len(pwd) != pwd_len:
                    pwd += random.choice(j)
                else:
                    break
        list_pwd.append(pwd)
        pwd = ""
    print(list_pwd)


if __name__ == "__main__":
    asq()
