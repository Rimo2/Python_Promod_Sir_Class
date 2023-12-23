phone_book = {"Batman": 9873367227, "Super-man": 90083736363, "Ironman": 997726657,
              "Dr.Strange": 9876656456, "Batman": 90}

print(phone_book["Dr.Strange"])
print(phone_book["Batman"]) # This is taking the latest value

phone_book2 = dict(Spiderman= 9039373637,Loki = 9837363536, Blackwidow = 9038373537)
print(phone_book2['Spiderman'])
print(phone_book2["Loki"])


Subhasish_details = dict(nickName = "Rimo", age = 32, gender = "Male",
                         address= "BF 60, Rabindrapally, Keshtopur,Kolkata - 700101",
                         pin = 700101, state = "West Bengal")

print(Subhasish_details["age"])
print(Subhasish_details.get("address"))
print(Subhasish_details.items())

set_dic = set(Subhasish_details.items())
print(set_dic)

Subhasish_details.pop('age') # Removes age
print("#######################################################################")
print(Subhasish_details)
print("#######################################################################")
print(Subhasish_details["nickName"])
print("#######################################################################")
print(Subhasish_details.values())