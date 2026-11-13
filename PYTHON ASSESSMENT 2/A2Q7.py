import time

# Original recursive program
def original(n):
    if n <= 1:
        return 1

    return original(n - 1) + original(n - 2)


# Redesigned iterative program
def redesigned(n):
    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


n = 30

start = time.perf_counter()
result1 = original(n)
time1 = time.perf_counter() - start

start = time.perf_counter()
result2 = redesigned(n)
time2 = time.perf_counter() - start

print("Original Result:", result1)
print("Original Time:", time1)

print("Redesigned Result:", result2)
print("Redesigned Time:", time2)
