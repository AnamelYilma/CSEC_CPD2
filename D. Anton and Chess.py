n = int(input())
x0, y0 = map(int, input().split())
check = False
for _ in range(n):
    parts = input().split()
    piece = parts[0]
    x = int(parts[1])
    y = int(parts[2])
    if piece == 'R':
        if x == x0 or y == y0:
            check = True
    elif piece == 'B':
        if abs(x - x0) == abs(y - y0):
            check = True
    elif piece == 'Q':
        if x == x0 or y == y0 or abs(x - x0) == abs(y - y0):
            check = True
print("YES" if check else "NO")
