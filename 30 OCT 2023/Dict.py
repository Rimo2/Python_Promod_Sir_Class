# Dict

my_dict ={'a':2, 'c':3, 'b': 5}
print(my_dict)
val= my_dict.pop('c')
print(val)
print(my_dict)
my_dict['c']=val
print(my_dict)

for k,v in my_dict.items():
    if k =='b':
        print("b is found"+"b is "+str(v))