def fib(n):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


count = 0
print(fib(40), count)
