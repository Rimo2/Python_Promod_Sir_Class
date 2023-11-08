num1 = int(input("Enter the required no of iteration: "))
a = 0
b = 1
i = 0
while i < num1:
    c = a + b
    print(c)
    i = i+1
    a,b = b,c
