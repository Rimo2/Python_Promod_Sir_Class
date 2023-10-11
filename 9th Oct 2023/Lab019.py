string1 = input('Enter your name in small: ')
result = string1.capitalize();
print('The capitalised version of your name is '+result)

print('The id of string1 is '+str(id(string1)))
print('The id of result is'+ str(id(result)))

print('----------------------------------------------------')
string2= input('Enter your name with mixed cases: ')
result2= string2.swapcase()
print('The swapped version of your name is '+result2)

print('----------------------------------------------------')
string3= input('Enter your name with mixed cases: ')
result3= string3.lower()
print('The lowercase version of your name is '+result3)

print('----------------------------------------------------')

string4= input('Enter your name with mixed cases: ')
result4= string3.upper()
print('The uppercase version of your name is '+result4)

print('----------------------------------------------------')

#Replace

string5= input('Enter your sentence: ')
result5 = string5.replace("can't","can")
print('The revised sentence is '+result5)