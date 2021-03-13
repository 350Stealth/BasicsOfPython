def sum2(a, b):
    if not (type(a) in [int, float]):
        if not (type(b) in [int, float]):
            return "all arguments are not a numbers"
        else:
            return "1st argument is not a number"
    else:
        if not type(b) in (int, float):
            return "2nd argument is not a number"
        else:
            return a + b


aTest = -15.001
bTest = 18

print(sum2(aTest, bTest))
print(aTest + bTest)
