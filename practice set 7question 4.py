n=input("enter a no:")
for i in range(2,n):
    if(n%i)==0:
        print("not a prime no")
        break
    else:
        print("number is prime")
        