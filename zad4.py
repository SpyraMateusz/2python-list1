def calculate_mean(numbers):
    """
    Oblicza średnią z elementów listy liczb.

    Args:
        numbers (list): Lista liczb.

    Returns:
        float: Średnia wartość elementów listy.
    """
    if not numbers:
        return 0  # Zwraca 0, jeśli lista jest pusta
    else:
        return sum(numbers) / len(numbers)


#np

# Importowanie funkcji calculate_mean z modułu statistics
from statistics import calculate_mean

# Przykładowa lista liczb
numbers = [1, 2, 3, 4, 5]

# Obliczanie średniej i wyświetlanie wyniku
mean = calculate_mean(numbers)
print("Średnia wartość:", mean)