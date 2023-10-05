a = str(input("Введите строку из 1 и 0: "))
s1 = a.count('1')
s0 = a.count('0')
if (s1==s0):
    print("yes")
else:
    print("no")
