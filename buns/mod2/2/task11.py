word = str(input("Введите цифры: "))
seen = ""
a = False
for i in word:
    if i != " ":
        if i not in seen:
            seen += i
            a = False
        elif i in seen:
            a = True
        
print(a)
