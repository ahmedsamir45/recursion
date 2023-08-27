def gcd(x,y):
    if x%y == 0:
        return y
    else :
        return gcd(y, x % y)

x = int(input("enter the bigest number :")) 
y = int(input("enter the next number :"))
print(gcd(x,y)) 
 