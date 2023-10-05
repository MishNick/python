number = str(input("Введите номер телефона: "))
ct = ""
for i in number:
    if i == "-" or i ==" " or i == "(" or i == ")":
        i = ""
        ct += i
    ct+=i
print(ct)
