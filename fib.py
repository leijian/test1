import time
import sys

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ', flush=True)
        a, b  = b, a+b
    print()
fib(1000)
time.sleep(10)
fib(2000)