# задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def dataNumber():
    try:
        n = int(input('Введите число от 1 до 7: '))
        if n > 0 and n < 6:
            print('нет')
        elif n < 8:
            print('да')
        else:
            n > 7
            print('в неделе 7 дней')
    except:
        print('некорректно введены данные')


dataNumber()
