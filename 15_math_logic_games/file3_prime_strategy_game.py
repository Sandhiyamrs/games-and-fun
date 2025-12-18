n = int(input("Enter number: "))
print("Prime" if n>1 and all(n%i for i in range(2,n)) else "Not Prime")
