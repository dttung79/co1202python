def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    
    return True

def print_primes(n, m):
    count = 0
    for k in range(n):
        if is_prime(k):
            print(k, end=" ")
            count += 1
            if count % m == 0:
                print()

n = int(input('Enter n: '))
print_primes(n, 10)