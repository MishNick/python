sentence = str(input("Введите предложение: "))
consonant = "bcdfghjklmnpqrstvwxz"
vowel = "aeiouy"
a = 0
b = 0
for i in sentence:
    if i in consonant:
        a += 1
    elif i in vowel:
        b += 1
    else:
        a += 0
        b += 0
print(a,b)
