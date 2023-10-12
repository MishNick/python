size = int(input()) 

matrix = [] 

for i in range(size):
    matrix.append(list(range(1, size+1)))

for row in matrix:
    print(", ".join(str(num) for num in row))

for i in range(size):
    for j in range(i+1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print()
for row in matrix:
    print(", ".join(str(num) for num in row))
