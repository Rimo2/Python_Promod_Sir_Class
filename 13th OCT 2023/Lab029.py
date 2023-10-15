# Arithmetic operator

num1 = int(input('Enter the 1st no:\n'))
num2 = int(input('Enter the 2nd no:\n'))

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

elif action == '**':
    result = num1 ** num2
    print('The result is ' + str(result))
    # This is exponential --> num1 to the power of num 2

elif action == '//':
    result = num1 // num2
    print('The result is ' + str(result))
    # This is basically round of

elif action == 'all':
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 % num2
    result5 = num1 / num2
    result6 = num1 // num2
    result7 = num1 ** num2
    print('The summation is ' + str(result1))
    print('The summation is ' + str(result2))
    print('The summation is ' + str(result3))
    print('The summation is ' + str(result4))
    print('The summation is ' + str(result5))
    print('The summation is ' + str(result6))
    print('The summation is ' + str(result7))
    # This is basically round of

else:

    print('Provide proper input')
