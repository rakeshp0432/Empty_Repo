fib = [0, 1]
# finding 10 terms of the series starting from 3rd term
N = 10
term = 3
while term < N + 1:
    value = fib[term - 2] + fib[term - 3]
    fib.append(value)
    term = term + 1
print("10 terms of the fibonacci series are:")
print(fib)
