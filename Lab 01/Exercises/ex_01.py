# For the given program, find the memory address(es) of the variable n for 5 iterations. Note down
# the observations.

# Print in triangle
x = int(input("Enter the number of stars: "))
for n in range(0, x):
    print(id(n), end=' ')
    n += 1
    print(id(n), end=' ')
    print("*" * (0 + n))

for n in range(-x, 0):
    print(id(n), end=' ')
    n += 1
    print(id(n), end=' ')
    print("*" * (0 - n + 1))

# Observations:
# 11753864 11753896 *
# 11753896 11753928 **
# 11753928 11753960 ***
# 11753960 11753992 ****
# 11753992 11754024 *****
# 11753704 11753736 *****
# 11753736 11753768 ****
# 11753768 11753800 ***
# 11753800 11753832 **
# 11753832 11753864 *

# Notes on observations:
# The memory address of n changes with each increment since integers in Python are immutable and every 
# update creates a new object. The addresses increase in a regular stride, showing Python’s allocation 
# pattern, with some reuse due to integer caching.