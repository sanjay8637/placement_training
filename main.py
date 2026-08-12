def swap(a, b):
    a, b = b, a
    return a, b

x = 10
y = 20

print(f"Before swap: x = {x}, y = {y}")
x, y = swap(x, y)
print(f"After swap: x = {x}, y = {y}")
