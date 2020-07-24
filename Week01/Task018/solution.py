num = int(input())
hours = num // (60 * 60) % 24
minutes = num // 60 % 60
seconds = num % 60
print(hours, ":", minutes // 10, minutes % 10, ":", seconds // 10, seconds % 10, sep="")
