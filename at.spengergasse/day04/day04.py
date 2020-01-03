def containsDoubleDigit(num):
    prev = None
    for n in str(num):
        if n == prev:
            return True
        prev = n
    return False

def isIncreasing(num):
    return sorted(list(str(num))) == list(str(num))

def containsExactDoubleDigit(num):
    prev = None
    groupLen = 0
    for n in str(num):
        if n == prev:
            groupLen += 1
        elif groupLen == 1:
            return True
        else:
            groupLen = 0

        prev = n
    if groupLen == 1:
        return True
    return False

input_range = (272091, 815432+1)
sol_part_1 = 0
sol_part_2 = 0
for num in range(*input_range):
    if containsDoubleDigit(num) and isIncreasing(num):
        sol_part_1 += 1
    if containsExactDoubleDigit(num) and isIncreasing(num):
        sol_part_2 += 1

print(sol_part_1)
print(sol_part_2)
