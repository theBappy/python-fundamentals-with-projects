# What is the 10001st prime number?

# sieve of eratosthenes
def eratosthenes():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes"""
    D = {} 
    q = 2

    while 1:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def nth_prime(n):
    for i, prime in enumerate(eratosthenes()):
        if i == n-1:
            return prime
        
print(nth_prime(10001))

