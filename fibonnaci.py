# Uses python3
def calc_fib(n):
    if n < 2:
        return n
    else:
        previous = 0
        current = 1
        for _ in range (n-1):
            previous,current = current,current+previous
        return current
n = int(input())
print(calc_fib(n))

