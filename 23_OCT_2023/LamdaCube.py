# Create a Lambda expression to triple power 2**3 a number

cubeOfNum = lambda value: value ** 3

x = int(input('Enter a number: '))
result = cubeOfNum(value=x)
print(f"The cube of the number {x} is {result}")
