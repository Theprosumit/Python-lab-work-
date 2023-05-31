#number list,rang function,list function
#printig number from 1to using range function 
for value in range(1,6):
  print(value)
#creat number list using 'list' function
number=list(range(0,8))
print(number)
#using range function u can skip number in a range
even_number=list(range(2,11,2))
print(even_number)
# another use of range
square=[]
for value in range(1,11):
   square.append(value**2) # '**'using for exponent
print(square)
# min,max and sum function
a=min(even_number)
b=max(even_number)
c=sum(even_number)
print(a,b,c)
#list comprehension 
number=[value**2 for value in range(1,11)]
print(number)
#slicing of a list
print(square[2:4], square[:5],square[4:], square[:-3])
#copying a list
even=even_number[:]
print(even)