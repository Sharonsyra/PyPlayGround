# Scalars


a = 8
b = 3.142
print(type(a))
print(type(b))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print("\n")

# Check if it is scalar or not

import numpy as np

# Is Scalar Function
def isscalar(num):
    if isinstance(num, generic):
        return True
    else:
        return False

print(np.isscalar(3.1))
print(np.isscalar([3.1]))
print(np.isscalar(False))
print("\n")
print("\n")


# Vectors 


# Declaring Vectors

x = [1, 2, 3]
y = [4, 5, 6]

print(type(x))

# This does'nt give the vector addition.
print(x + y)

# Vector addition using Numpy

z = np.add(x, y)
print(z)
print(type(z))

# Vector Cross Product
mul = np.cross(x, y)
print(mul)