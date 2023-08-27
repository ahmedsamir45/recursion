def TOH(numbers,start,aux,end):
    if numbers==1:
        print ('move disk 1 from rod {} to rod {}'.format(start,end))
        return
    TOH(numbers-1,start,end,aux)
    print ('move disk {} from rod {} to rod {}'.format(numbers,start,end))
    TOH(numbers-1,aux,start,end)


disk = 3
TOH(disk,'A','B','C')
              
    
