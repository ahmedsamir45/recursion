def print1(n):
    if n==0:
        return 0
    else:
        print(n)
        return print1(n-1)
print(print1(4))
