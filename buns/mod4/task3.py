def evklid(num1, num2):
    if num1 == 0:
        return num2
    return evklid(num2 % num1, num1)

a = int(input())
b = int(input())
print(evklid(a,b))
