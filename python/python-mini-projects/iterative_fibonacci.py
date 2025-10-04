

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print('======== Fibonacci Series ========')
    for i in range(1, 11):
        print(f"Fibonacci ({i}): {fib_iter(i)}")