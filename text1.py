#WAP TO PRINT FIRST N PERFECT NUMBER
u=int(input())
n=1
dc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds=ds+i
    if ds==n:
        print(n)
        dc+=1
    if dc==u:
        break
    n=n+1
        


u=int(input())
n=1
dc=0
while True:
    i=1
    ds=0
    while i<=n//2:
        if n%i==0:
            ds=ds+i
        i=i+1    
    if ds==n:
        print(n)
        dc+=1
    if dc==u:
        break
    n=n+1
   
#WAP TO PRINT NTH PERFECT NUMBERS
u=int(input())
n=1
dc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds=ds+i
    if ds==n:
        dc+=1
    if dc==u:
        print(n)
        break
    n=n+1
     



u=int(input())
n=1
dc=0
while True:
    i=1
    ds=0
    while i<=n//2:
        if n%i==0:
            ds=ds+i
        i=i+1    
    if ds==n:
        dc+=1
    if dc==u:
        print(n)
        break
    n=n+1
   

# WAP TO PRINT 1 T0 3 RNAGE PN
n=1
dc=0
while True:
    i=1
    ds=0
    while i<=n//2:
        if n%i==0:
            ds=ds+i
        i=i+1    
    if ds==n:
        dc+=1
        if dc>=1 and dc<=3:
            print(n)
    if dc==3:
        break
    n=n+1











































