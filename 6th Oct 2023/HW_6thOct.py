# Take a input from a user and print the table
# How to use the print with formatting f
# print(f''), How can print the same?

num1 = int(input('Enter the no to print its table:\n'))
num2 = int(input('Enter the no up to which you want the table:\n'))
i = 1
j = 1
while i <= num2:
    j = i * num1
    print(f'{num1} x {i} = {j}')
    i = i + 1

# Instead of this - print(str(num1)+' x '+str(i)+' = '+str(j)), I used the f'' to print the desired results
