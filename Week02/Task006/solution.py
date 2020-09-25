n1 = int(input())
n2 = int(input())
test = (n1 - 1) % (n2 - n1 + 1)
if test == 0:
    print("YES")
else:
    print("NO")
