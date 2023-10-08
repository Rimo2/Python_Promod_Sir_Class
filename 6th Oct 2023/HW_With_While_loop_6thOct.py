# Take a input from a user and print the table
# How to use the print with formatting f
# print(f''), How can print the same?

num1 = int(input('Enter the no to print its table:\n'))
num2 = int(input('Enter the upper limit:\n'))

print(f'The table of {num1} with an upper limit of {num2} is as follows:')
i = 1
while i <= num2:
    print(f'{num1} x {i} = {num1*i}')
    i = i + 1

# Instead of this - print(str(num1)+' x '+str(i)+' = '+str(j)), I used the f'' to print the desired results
