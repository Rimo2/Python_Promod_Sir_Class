def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


inputStr = str(input('Provide your word: '))
print("The reversed string is " + reverse_string(inputStr))

if reverse_string(inputStr).lower() == inputStr.lower():
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")


############################################################################################

def reverse_string(input_string):
    return ''.join(reversed(input_string))


inputStr = str(input('Provide your word: '))
rev_string = reverse_string(inputStr)
print(rev_string)

if rev_string.lower() == inputStr.lower():
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")