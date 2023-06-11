#to check wether the numer is pelidrom or not
n=int(input("enter any number:"))
temp=n
cmp=0
while(n>0):
  dig=n%10
  cmp=cmp*10+dig
  n=n//10
if temp==cmp:
   print("number is pelidrom ")
else: 
   print("number is not a pelidrom")