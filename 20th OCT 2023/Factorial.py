num = int(input('Enter a number: '))

if num<0:
    print('Factorial is not possible')

else:
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
print('Fact is: ',fact)