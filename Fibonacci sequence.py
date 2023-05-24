#to print Fibonacci sequence 
n= int(input("enter the number of terms,\nthat you want to print:"))
n1,n2 =0,1 
count=0
if n<=0:
  print("entered negative number\n") 
elif n==1:
  print("the fibonacci series up to term", n)
  print(n1)
else:
  print("the fibonacc sequnce :")

while count < n:

    print (n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count +=1
