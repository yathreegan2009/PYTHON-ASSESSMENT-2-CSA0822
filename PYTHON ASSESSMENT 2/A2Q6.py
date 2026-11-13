from functools import lru_cache

calls = 0


# Normal recursion
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Memoization
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


calls = 0
print("Naive:", ways_naive(10))
print("Calls:", calls)

calls = 0
print("Memo:", ways_memo(10))
print("Calls:", calls)


# Iterative method
def ways_loop(n):
    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


print("Loop:", ways_loop(10))
