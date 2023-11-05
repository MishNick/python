def get_armstrong_numbers():
    for num in range(10, 100000):
        digits = [int(x) for x in str(num)]
        power = len(digits)
        if sum([digit ** power for digit in digits]) == num:
            yield num

for i, armstrong_number in enumerate(get_armstrong_numbers()):
    print(armstrong_number, end=' ')
    if i == 7:
        break
