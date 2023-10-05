def isinteger(x):
    return x % 1 == 0

a = float(input("Введите число: "))
if (isinteger(a)):
    a = int(a)
    print(f'{a:b}',f'{a:o}',f'{a:x}')
else:
    print("Неверный ввод")

