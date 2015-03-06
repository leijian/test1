import time
import sys

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ', flush=True)
        a, b  = b, a+b
    print()

def test2(n):
    i = 0
    while i<n:
        print("hellword"*i)
        i=i+1

test2(2000)
time.sleep(10)
test2(10)