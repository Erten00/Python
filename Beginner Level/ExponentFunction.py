
def reiseToPower(baseNum, powNum):
    result = 1
    for i in range(powNum):
        result = result * baseNum
    return result

print("Your number is ")
print(reiseToPower(3, 4))