def checkCriteria(number):
    containsDouble = False
    digit = number % 10
    number //= 10
    for i in range(5):
        nextDigit = digit
        digit = number % 10
        number //= 10
        if digit > nextDigit:
            return False
        elif digit == nextDigit:
            containsDouble = True
    return containsDouble


testData = [[111111, True], [223450, False], [123789, False]]
hasTestPassed = all(map(lambda i: checkCriteria(i[0]) == i[1], testData))
print("Test " + "passed" if hasTestPassed else "not passed")


min = 264793
max = 803935

sum = 0
for i in range(min, max + 1):
    if (checkCriteria(i)):
        sum += 1

print(sum)
