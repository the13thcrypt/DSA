from math import gcd, sqrt

def no_of_common_factors(a, b):
    c = gcd(a, b)
    count = 0
    for i in range(1, int(sqrt(c)) + 1):
        if c % i == 0:
            count = count + 1
            if i != c // i:
                count = count + 1
    return count

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = no_of_common_factors(a, b)
print(f"Number of common factors: {result}")