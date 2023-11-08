#  Count vowels and consonants in a String
from bs4 import element

inputStr = str(input('Provide your string: '))

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

filtered_list = [char for char in inputStr if char.isalpha()]

# for char in inputStr:
#     list_all.append(char)

list_vowel = [element for element in filtered_list if element in vowels]
list_consonants = [element for element in filtered_list if element not in vowels ]

# for element in filtered_list:
#     if element in vowels:
#         list_vowel.append(element)

print("All alphabetic characters are : "+str(filtered_list))
print("The list of vowels are : "+str(list_vowel))
print("The list of consonants are : "+str(list_consonants))
print("The number of all characters are: "+str(len(filtered_list)))
print("The number of vowels in the provided string is: "+str(len(list_vowel)))
print("The number of consonants in the provided string is: "+str(len(list_consonants)))
