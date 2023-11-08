# Create a Function with a Parameter which can do x^y

def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        res = base
        for i in range(2, exponent + 1):
            res = res * base
    return res


num = int(input('Enter a number: '))
power = int(input('Enter the desired power: '))

out = calculate_power(num, power)
print(f"{num} to the power of {power} is : {out}")
