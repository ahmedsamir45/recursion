def gcd(x,y):
    if x%y == 0:
        return y
    else :
        return gcd(y, x % y)

x = int(input("enter the  number of units:")) 

g=[]
for i in range(1,x): 
    (gcd(x,i))
    if gcd(x,i)==1:
        g.append(i)
print(f"U({x}) = ",g)

 