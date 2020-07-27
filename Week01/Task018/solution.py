num = int(input())
h = num // (60 * 60) % 24
m = num // 60 % 60
s = num % 60
print(h, ":", m // 10, m % 10, ":", s // 10, s % 10, sep="")
