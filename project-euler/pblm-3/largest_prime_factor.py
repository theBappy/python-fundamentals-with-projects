
# largest prime factor is the inter is the largest prime number that divides it exactly, meaning there is no remainder. eg: prime factor of 180 are 2, 2, 3, 3, 5, and 5 is the largest (180//2=90, 180//3= 60, 180 // 5 = 16)[no remainder, 5 is the largest]

import math


def factorize(n):
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


print(max(factorize(51475143)))
