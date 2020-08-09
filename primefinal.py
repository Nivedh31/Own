
d=int(input("Enter a value for d : "))
p=int(input("Enter a value for p : "))
b=0
ran=0
tim=[k for k in range(1,d+1)]
prim = []

part = d // p

for i in range(1,d):
    for j in range(2,i):
     if (tim[i] % j) == 0:
         break

    else:
    
            prim.append(tim[i])
            if (i<part):
                ran=i
        
for x in range(0,(ran-1)):
    a=0
    n = prim[x]
    for y in range ((x+1),len(prim)):
        if (n == (prim[y]-part)):
            
            n = prim[y]
            a=a+1
        
    if (a == (p-1)):
        b = b+1

print ("Number of Pairs = ",b)


    
    
    

        
