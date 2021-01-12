def max_occ(a):
    n=len(a)
    b=dict()
    count=0
    for i in range(n):
        if a[i]==1:
            count+=1
        else:
            b[i]=count
            count=0
        b[i]=count

    m=max(b,key=lambda x:b[x])
    print(f'maximum occurences of 1 is: {b[m]}')

a=[0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1]
max_occ(a)