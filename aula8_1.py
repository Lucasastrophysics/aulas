def counter(n):
    count = 0
    while n!=1:
        count = count + 1
        if int(n)%2==0:
            n = n // 2
        else:
            n=3*n+1 
        if count%10==0:
            print("valor de n",n)
        if n==1:
           print("valor de n",n)        
    return count

quanto =counter(711)
print(quanto)

