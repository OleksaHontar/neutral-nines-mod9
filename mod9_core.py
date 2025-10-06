def neutral_nines_mod9(n):
    """
    Обчислює залишок по модулю 9 для числа n,
    виключаючи цифри 9, 0 та пари цифр, що в сумі дають 9.

    Автор: Олексій Гонтар
    """

    # Перетворюємо число на список цифр
    digits = [int(d) for d in str(abs(n))]

    # Створюємо список для "активних" цифр
    active_digits = []

    # Копія для пошуку пар
    temp_digits = [d for d in digits if d not in (0, 9)]

    # Пошук і виключення пар, що дають 9
    while temp_digits:
        found_pair = False
        for i in range(len(temp_digits)):
            for j in range(i + 1, len(temp_digits)):
                if temp_digits[i] + temp_digits[j] == 9:
                    a, b = temp_digits[i], temp_digits[j]
                    temp_digits.remove(a)
                    temp_digits.remove(b)
                    found_pair = True
                    break
            if found_pair:
                break
        if not found_pair:
            active_digits.extend(temp_digits)
            break

    # Обчислюємо суму "активних" цифр
    total = sum(active_digits)

    # Повертаємо залишок по модулю 9
    return total % 9


# 🔍 Приклад використання
if __name__ == "__main__":
    test_numbers = [972045, 123456, 909090, 98172, 999, 0, 1008]
    for num in test_numbers:
        result = neutral_nines_mod9(num)
        print(f"{num} → залишок по модулю 9 (без нейтральних): {result}")
