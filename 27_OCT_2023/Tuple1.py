# List vs Tuple

my_list = [12, 14, 15, 19, 90, 5, 5]
print(my_list)
my_list[1] = 20
print(my_list)
my_list.append(11)
print(my_list)

my_tuple = (12, 14, 15, 19, 90, 5, 5)

print(my_tuple)
print(tuple(my_list))

# my_tuple[1]= 20 --> We can't change value in tuple

a, b, c = 12, 14, 17  # Multiple value assignment
d, e, f = (18, 22, 23)  # tuple assigned to multiple variable

print(d)
print(e)

# Nested Tuple

avengers = ("Iron Man", "Captain America", "Hulk", "Spider-man", "Blackwidow", "Dr. Strange")
justice_League = ("Batman","Superman", "Wonder Woman", "Flash", "Green Lantern")

marvel_dc = (avengers,justice_League)
print(marvel_dc)

print(marvel_dc[0][0])
print(marvel_dc[1][0])

# Search in tuple

print("Spider-man" in avengers)
print("Spider-man" in justice_League)

print("Batman" in justice_League)