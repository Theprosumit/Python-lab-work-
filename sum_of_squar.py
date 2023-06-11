def SumofSquares(n):
    s=0
    for i in range(n+1):
        s+=i**2
    return s

#input
n=int(input("enter n: "))
print("sum of squares of first {} natural numbers: ".format(n),SumofSquares(n))
