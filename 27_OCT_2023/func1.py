# Multiply a no by 20

num = int(input("Enter your desired no: "))

def multiply_by_10(n):
    n = n*10 # This is same as n *=10
    num = n
    print("Value of the num inside function is : "+str(num))
    return n
multiply_by_10(num)
print("Value of num outside function: "+str(num))
