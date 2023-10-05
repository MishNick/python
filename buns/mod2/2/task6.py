a = input("Ввведите домен сайта: ")
tmp=""
for i in a :
    if i.isalpha():
        tmp=tmp+i

    elif not i.isalpha():
      print(tmp)
      tmp=""
print(tmp)
