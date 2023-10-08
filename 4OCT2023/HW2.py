# Take first name and last name of user and print with sep. = "-" and end with /t

firstName = input('Enter your first name:')
lastName = input('Enter your last name:')

print("Welcome " + firstName, lastName, sep='-', end='\t')
print('- The previous sentence is ended with a tab (instead of a new line)')
print('- The previous sentence is ended with a new line')
