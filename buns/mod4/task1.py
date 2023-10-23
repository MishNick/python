a = str(input())
a = (list(map(int, a)))
print(a)
if len(set(a)) == 1:
    print("Все числа равны")
elif len(set(a)) == len(a):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")
