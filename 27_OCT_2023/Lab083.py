my_list =[1,2,3,4,5]
print(my_list)
my_list[1]= 20
print(my_list)

# list is mutable in nature
# Tuple is not mutable. Its content can not be changed. But it can have duplicate content


car = ("Ford GT","Raptor", "Lambo")
car = ("Ford GT","Raptor", "Lambo","Thar","Lambo")
print(len(car))
# car[1] = "XUV 500"
# TypeError: 'tuple' object does not support item assignment

# We can convert list to tuple

tuple1 = ()
tuple2 = (1,2,3,4,5,6,7,8,9,0)
tuple3 = tuple(["Rimo","Subh","Asish"])
print(tuple3)

print('###########################################################')

hero_1=("Batman","Superman", "Diana")
hero_2 = ("Ironman","Captain America")

best_team = hero_1+hero_2
print(best_team)
print(best_team[0][2])
print(best_team[1][1])

print('###########################################################')

a,b = 23,24
c,d,e = (26,27,28)
print(c)