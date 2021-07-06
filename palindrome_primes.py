output=[]

for n in range(10000,99999):
    a=n
    r=0
    while a>0:
        rem=a%10
        r=(r*10)+rem
        a=a//10 
            
    if n==r:
        output.append(n)
print(output)




