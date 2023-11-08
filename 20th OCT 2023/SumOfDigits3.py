inputInt = int(input('Provide your number: '))
total = 0

while inputInt != 0:
    digit = inputInt % 10
    total = total+digit
    inputInt = int(inputInt/10)
print(total)