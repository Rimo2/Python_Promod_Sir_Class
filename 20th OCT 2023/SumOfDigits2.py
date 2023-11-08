def sum_of_digits(n):
    total = 0
    n_str = str(n)
    for digit in n_str:
        # Convert the digit back to an integer and add it to the sum
        total = total+ int(digit)

    print("The sum of the digits are: "+str(total))


inputInt = int(input('Provide your number: '))
sum_of_digits(inputInt)
