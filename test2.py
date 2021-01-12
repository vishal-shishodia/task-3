def max_num(a,b):
    m=max(a, key=lambda x:a[x])
    print(f'student-ID with max number is: {m}')
    print(f'student with max number is: {b[m]}')

a={'1':10,'2':20,'3':30}
b={'1':'name1','2':'name2','3':'name3'}
max_num(a,b)