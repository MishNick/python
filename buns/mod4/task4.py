def form_polidrome(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    odd_count = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    if odd_count > 1:
        return False
    else:
        return True

def find_palindrome(word):
    if not form_polidrome(word):
        print("Невозможно составить палиндром из данного слова.")
        return
    
    palindrome_chars = []
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    for letter, count in letter_count.items():
        if count % 2 != 0:
            palindrome_chars.append(letter)
        
        for _ in range(count // 2):
            palindrome_chars.append(letter)
    
    palindrome = "".join(palindrome_chars) + "".join(palindrome_chars[::-1])
    
    print("Палиндром, составленный из заданного слова:", palindrome)

word1 = "векокве"
find_palindrome(word1)
