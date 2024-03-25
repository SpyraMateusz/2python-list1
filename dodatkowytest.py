def is_palindrome(text):
    """
    Sprawdza, czy podany tekst jest palindromem.

    Args:
        text (str): Tekst do sprawdzenia.

    Returns:
        bool: True, jeśli tekst jest palindromem, False w przeciwnym razie.
    """
    # Usuwanie białych znaków i zmiana na małe litery
    clean_text = "".join(c.lower() for c in text if c.isalnum())

    # Sprawdzenie, czy tekst czyta się tak samo od przodu i od tyłu
    return clean_text == clean_text[::-1]



# Importowanie funkcji is_palindrome z modułu palindrome
from palindrome import is_palindrome

# Lista przykładowych tekstów do sprawdzenia
texts = ["kajak", "A man, a plan, a canal, Panama!", "Python", "Madam, in Eden, I'm Adam"]

# Sprawdzanie, czy każdy z tekstów jest palindromem
for text in texts:
    if is_palindrome(text):
        print(f'Tekst "{text}" jest palindromem.')
    else:
        print(f'Tekst "{text}" nie jest palindromem.')
