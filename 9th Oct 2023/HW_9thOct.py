# Take an input and then perform action on it based on user's choice

str1 = input('Provide your desired string:\n')
str2 = input('What do you want to do with it? :\n')

if str2 == 'cap':
    print('The capitalized version of your input is: ' + str1.capitalize())
    # Returns a copy of the string with its first character capitalized.

elif str2 == 'upper':
    print('The upper case version of your input is: ' + str1.upper())

elif str2 == 'lower':
    print('The lower case version of your input is: ' + str1.lower())

elif str2 == 'swap':
    print('The swap case version of your input is: ' + str1.swapcase())

elif str2 == 'title':
    print('The title case version of your input is: ' + str1.title())
    # Returns a title cased version of the string,
    # where words start with an uppercase character and
    # the remaining characters are lowercase.

elif str2 == 'swap':
    print('The swap case version of your input is: ' + str1.swapcase())

else:
    print('Provide proper input')
