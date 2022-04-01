def isPrime(limit):
    if(limit==1 or limit==0):
        return False
    for i in range(2,limit):
        
        if(limit%i==0):
            return False
        return True

limit = 100
for i in range(1,limit+1):
  if(isPrime(i)):
    print(i,end=" ")