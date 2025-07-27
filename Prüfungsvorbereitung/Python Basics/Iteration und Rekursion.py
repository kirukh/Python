# Iteration
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Rekursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Lernen wie man Interation und Rekursion verwendet
# Und wie man Iterationen zu Rekursion umwandelt und umgekehrt
