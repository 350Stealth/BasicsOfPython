a = int(input())
b = int(input())
n1 = a // b
n2 = b // a
print(((a * n1) + (b * n2)) // (n1 + n2))
