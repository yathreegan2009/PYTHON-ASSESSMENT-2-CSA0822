# Buggy function
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# Correct function
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


# Testing functions
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print(add_item("Tea"))
print(add_item("Vada"))


# Returning multiple values
def calculate(price):
    gst = price * 0.05
    total = price + gst
    return total, gst


total, gst = calculate(1000)

print("Total:", total)
print("GST:", gst)


# Global variable
x = 10

def display():
    global x
    x = 20

display()
print("Global:", x)


# Local variable
def local_example():
    y = 5
    print("Local:", y)

local_example()


# Nonlocal variable
def outer():
    a = 10

    def inner():
        nonlocal a
        a = 20

    inner()
    print("Nonlocal:", a)

outer()
