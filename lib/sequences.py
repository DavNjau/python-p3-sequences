#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < length:
        nextnumber = fib[-1] + fib[-2]
        fib.append(nextnumber)
    return fib

    pass







    

