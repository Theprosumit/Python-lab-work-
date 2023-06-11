#touple for permanent storing values
number=(44,55,66,77,88,99,00)
print(number[0], number[1])
#printing the touple
for num in number:
  print(num)
#we can't modified a touple but we can redefine the entire touple
number=(00,99,88,77,66,55,44,33,22,11)
for num in number:
  print(num)