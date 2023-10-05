string = "abcdefghijklmnopqrstuvwxyz"
i = str(input("Введите букву: "))
n = int(input("Введите число: "))
if (i in string):
        a = string.find(i)
        b = a+n
else:
    print("буквы нет в алфавите")
print(string[b])
