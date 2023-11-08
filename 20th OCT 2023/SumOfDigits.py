# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.

# n = 12345
#
# sum = 15

# n = 123

# sum = 6

inputInt = int(input('Provide your number: '))
inpSt = str(inputInt)
outPut = 0

characters = []

for char in inpSt:
    characters.append(char)


for i in range(0,len(characters)):
    outPut = outPut + int(characters[i])

print(outPut)
