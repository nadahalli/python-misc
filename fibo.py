# Expected implementation
def fib(n):
    t1 = 1
    t2 = 1
    for i in range(n-1):
        next = t1 + t2
        t1 = t2
        t2 = next
    return next

def fib1(n):
    a = 0
    b = 1
    for i in range(n):
        if a < b:
            a = a + b
        else:
            b = a + b
    return max(a, b)

def fib2(n):
    n0 = 1
    n1 = 1
    for i in range(int(n/2)):
        n0 = n0 + n1
        n1 = n0 + n1
    if n % 2 == 0:
        return n0
    else:
        return n1

# Closed form solution for the n-th Fibonacci number
import math
def fib3(n):
    k1 = (1 + math.sqrt(5))/2
    k2 = (1 - math.sqrt(5))/2
    return 1/math.sqrt(5) * (pow(k1, n+1) - pow(k2,n+1))

for i in range(2, 10):
    print(i, fib(i), fib1(i), fib2(i), fib3(i))
