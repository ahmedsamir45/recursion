def reverse(x):
    if len(x)==1:
        return x
    else:
        return x[-1] + reverse(x[:-1])

print(reverse('ghjk'))