num = int(input())
num1 = num
a = num1 % 10
num1 = num1 // 10
b = num1 % 10
num1 = num1 // 10
c = num1 % 10
num1 = num1 // 10
num2 = a * 1000 + b * 100 + c * 10 + num1
print(num - num2 + 1)
