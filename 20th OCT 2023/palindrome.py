# Palindrome Checker:

inputStr = str(input('Provide your word: '))

characters = []
rst = ""

for char in inputStr:
    characters.append(char)
    l = len(characters)

for i in range(len(characters) - 1, -1, -1):
    rst = rst + characters[i]


print("The reversed word is: "+rst)
if rst.lower() == inputStr.lower():
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
