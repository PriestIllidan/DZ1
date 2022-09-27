# задача 2. Напишите программу для, проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def truthTest(x, y, z):
    predikat1 = not (x or y or z)
    predikat2 = not x and not y and not z 
    if predikat1 == predikat2:
        return True

x = input('Введите значение x: ')
y = input('Введите значение y: ')
z = input('Введите значение z: ')

if truthTest(x, y, z):
    print('Истинность доказана')
else:
    print('Истинность не доказана')