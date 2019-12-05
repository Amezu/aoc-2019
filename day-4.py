def checkCriteria(number):
    count = 0
    containsDouble = False
    digit = number % 10
    number //= 10
    for i in range(6):
        nextDigit = digit
        digit = number % 10
        number //= 10
        if digit > nextDigit:
            return False
        elif digit == nextDigit:
            count += 1
        elif digit < nextDigit:
            if count == 1:
                containsDouble = True
            count = 0
    return containsDouble


testData = [[112233, True], [123444, False], [111122, True], [335666, True]]
hasTestPassed = all(map(lambda i: checkCriteria(i[0]) == i[1], testData))
print("Test " + ("passed" if hasTestPassed else "not passed"))

min = 264793
max = 803935

print(sum(1 for i in range(min, max+1) if checkCriteria(i)))
