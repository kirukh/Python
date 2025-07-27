# Alle Funktionen (Loops, Conditions, etc.)

# If-Condition
def check_number(num):
    if num > 0:
        return "Positiv"
    elif num < 0:
        return "Negativ"
    else:
        return "Null"


# For-Loop
def print_numbers(n):
    for i in range(n):
        print(i)


# While-Loop
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Fertig!")
