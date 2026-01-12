num = int(input("Enter a number: "))
is_prime = num > 1 and all(num%i for i in range(2,num))
print("Prime!" if is_prime else "Not Prime")
