# Create a Function with a Parameter which can do x^y

def power(a, b):
    res = x ** y
    return res


x = int(input('Enter a number: '))
y = int(input('Enter the desired power: '))
out = power(x, y)
print(f"The value of {x} to the power {y} is : {out}")

######################################################################

result = lambda base, pow: base ** pow

x = int(input('Enter a number: '))
y = int(input('Enter the desired power: '))
out = result(x,y)

print(f"{x} to the power of {y} is : {out}")

