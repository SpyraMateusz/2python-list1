def fibonacci(n):
    """
    Zwraca n-ty element ciągu Fibonacciego.

    Args:
        n (int): Numer elementu w ciągu Fibonacciego.

    Returns:
        int: Wartość n-tego elementu ciągu Fibonacciego.
    """
    if n <= 0:
        return None  # Zwraca None dla n <= 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev = 0
        fib_current = 1
        for _ in range(2, n):
            fib_prev, fib_current = fib_current, fib_prev + fib_current
        return fib_current







# Importowanie funkcji fibonacci z modułu fibonacci
from fibonacci import fibonacci

# Określenie numeru elementu w ciągu Fibonacciego
n = 10

# Wyświetlenie n-tego elementu ciągu Fibonacciego
print(f"{n}-ty element ciągu Fibonacciego:", fibonacci(n))
