num = int(input())
a = num % 10
num = num // 10
b = num % 10
num = num // 10
numSum = a + b + num
print(numSum)
