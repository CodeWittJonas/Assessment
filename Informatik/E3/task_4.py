is_prime = False

n = int(input("Please enter a number, to check if it's prime: "))
factors = [1]

if n <= 1:
    is_prime = False
elif n == 2:
    is_prime = True
elif n % 2 == 0:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)

    if len(factors) > 2:
        is_prime = False
    else:
        is_prime = True

if is_prime:
    print(str(n) + " is prime")
else:
    print(str(n) + " is not prime")
