for i in range (1,10):
   # print(i)
   if i ==5:
     pass
   else:
       print(i)

# pass mean we don't want to do anything or skip

#Continue

print("################################################")

for num in range(1,10):
    if num%2 ==0:
        print(f"Found even no {num}")
        continue
    print("Odd number found --> ", num)