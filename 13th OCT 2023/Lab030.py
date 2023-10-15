# Comparioson operators
x = int(input('Enter the 1st no:\n'))
y = int(input('Enter the 2nd no:\n'))

action = input('What action you want to perform: ')

if action == 'all':
    print(x==y)
    print(x!=y)
    print(x>y)
    print(x<y)
    print(x>=y)
    print(x<=y)