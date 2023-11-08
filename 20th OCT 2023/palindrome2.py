# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121

inputStr = str(input('Provide your word: '))


def is_palindrome(string):
    reversed_string = string[::-1]
    print("The reversed string is: " + reversed_string)
    if reversed_string.lower() == string.lower():
        return True
    else:
        return False


if is_palindrome(inputStr):
    print("This is palindrome")

else:
    print("It is not palindrome")
