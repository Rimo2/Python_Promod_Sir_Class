# Take a input from a user and print the table
# How to use the print with formatting f
# print(f''), How can print the same?

num1 = int(input('Enter the no to print its table: '))
num2 = int(input('Enter the upper limit: '))

for i in range(1,num2+1):
    print(f'{num1} x {i} = {num1 * i}')