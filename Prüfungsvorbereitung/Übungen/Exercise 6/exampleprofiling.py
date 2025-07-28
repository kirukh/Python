import line_profiler


@profile
def entry():
    with open("examplejson.json", "w") as file:
        for i in range(1000):
            file.write(f'{{"number": {i}}}\n')


@profile
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


@profile
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial_recursive(10))
print(factorial_iterative(10))
entry()
