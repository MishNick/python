sentence = str(input("Введите предложение: "))
word = ""
ct = 0
for i in sentence:
    if i == " ":
        i = sentence[ct-1]
        word += i
        print(ct)
    ct+=1
        
        

print(word+sentence[-1])
