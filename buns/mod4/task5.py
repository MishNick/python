def count_letters(filename):
    letter_count = {}
    with open(filename, 'r') as file:
        for i in file:
            for letter in i:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1
    
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    
    with open('result.txt', 'w') as file:
        for l,c in sorted_letter_count:
            file.write(f"{l}: {c}\n")

filename = "input.txt"
count_letters(filename)
