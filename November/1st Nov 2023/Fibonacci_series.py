# Write a Python program to get the Fibonacci series between a given range
#
# the_series=[0,1]
#
# num1 = int(input("Enter the required no of iteration: "))
# a = 0
# b = 1
# i = 0
# while a+b <= num1:
#     c = a + b
#     the_series.append(c)
#     i = i+1
#     a,b = b,c
#
# print(the_series)

def generate_fibonacci_series(max_value):
    series = [0, 1]
    a, b = 0, 1

    while a + b <= max_value:
        c = a + b
        series.append(c)
        a, b = b, c
    return series


n = int(input("Enter the required no of iteration: "))
result_series = generate_fibonacci_series(n)

print(result_series)
