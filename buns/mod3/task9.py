x, y = 0, 0
dx, dy = 0, -1
n = int(input())

for _ in range(n):
    x, y = x + dx, y + dy
    if dx == 0 and dy < 0: 
        dx, dy = dy, dx
    elif dx < 0 and dy == 0: 
        dx, dy = dy, dx
    elif dx == 0 and dy > 0: 
        dx, dy = dy, dx
    elif dx > 0 and dy == 0: 
        dx, dy = dy, dx

print(x, y)
