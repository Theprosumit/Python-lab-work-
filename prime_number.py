#to cheack whether the number is prime or not
n=int(input("enter any number")) 
c=True 
if n==1:
   print(n, "is prime number")
else:
   for i in range(2,n):
       if n%i==0:
          c=False
          break 
if c:
   print(n, "is prime number")
else: 
   print (n, "is not a prime number")