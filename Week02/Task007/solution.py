x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
d1 = (x1 - y1) % 2
d2 = (x2 - y2) % 2
if (d1 == 1) & (d2 == 1):
    print("YES")
else:
    print("NO")
