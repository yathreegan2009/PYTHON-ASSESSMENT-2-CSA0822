import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]


# Using +
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


# Using join()
def build_join(parts):
    return ";".join(parts) + ";"


# Using f-string
def build_fstring(parts):
    text = ""
    for i, p in enumerate(parts):
        text += f"{p};"
    return text


start = time.perf_counter()
a = build_plus(items)
t1 = time.perf_counter() - start

start = time.perf_counter()
b = build_join(items)
t2 = time.perf_counter() - start

start = time.perf_counter()
c = build_fstring(items)
t3 = time.perf_counter() - start

print("Same text:", a == b == c)
print("Plus time:", t1)
print("Join time:", t2)
print("F-string time:", t3)
