# Write a Python program to check if a number is a prime number
def check_prime_No(n):
    divisible_no = []
    for i in range(2, n):
        if n % i == 0:
            divisible_no.append(i)
    if len(divisible_no) > 0:
        print("This is a not a prime no and the list of divisible no is: " + str(divisible_no))
    else:
        print("This is a prime no")


num = int(input("Provide your desired no: "))
check_prime_No(num)
