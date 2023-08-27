def isArrayInSortedOrder(A):

    if len(A)==1:
        return True
    return A[0]<=A[1] and  isArrayInSortedOrder(A[1:])
A = [1,2,3,4,5]
print(isArrayInSortedOrder(A))
