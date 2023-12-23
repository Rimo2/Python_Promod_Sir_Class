provided_numbers = list(map(int, input("Provide your desired numbers: ").split()))
print("The list of provided numbers is: " + str(provided_numbers))

even_num = list(filter(lambda x: x % 2 == 0, provided_numbers))
print("The list of even numbers is: " + str(even_num))

odd_num = list(filter(lambda x: x % 2 != 0, provided_numbers))
print("The list of odd numbers is:" + str(odd_num))

square_num = list(map(lambda x: x ** 2, provided_numbers))
print("The list of squared num is: " + str(square_num))
