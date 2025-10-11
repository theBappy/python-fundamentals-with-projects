from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(input_val):
    if input_val == 0:
        return 0
    elif input_val == 1:
        return 1
    return fib_memo(input_val - 1) + fib_memo(input_val - 2)

if __name__ == "__main__":
    print('======== Fibonacci Series ========')
    for i in range(1, 11):
        print(f"Fibonacci ({i}): {fib_memo(i)}")