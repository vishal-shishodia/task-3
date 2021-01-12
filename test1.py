def checksum(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum
    
lst=[1,2,3,4,5]
print(checksum(lst))