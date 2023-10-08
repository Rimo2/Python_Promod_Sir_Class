num1 = int(input('Enter the 1st no:\n'))
num2 = int(input('Enter the 2nd no:\n '))

action = input('What action you want to perform: ')

if action == '+':
    result = num1 + num2
    print('The result is ' + str(result))

elif action == '-':
    result = num1 - num2
    print('The result is ' + str(result))

elif action == '*':
    result = num1 * num2
    print('The result is ' + str(result))

elif action == '/':
    result = num1 / num2
    print('The result is ' + str(result))

elif action == '%':
    result = num1 % num2
    print('The result is ' + str(result))

else:

    print('Provide proper input')