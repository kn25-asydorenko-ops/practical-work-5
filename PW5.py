def solve():
    # Зчитування вхідних даних
    try:
        n = int(input("Введіть довжину послідовності n: "))
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")
        return

    MOD = 12345

    # Обробка базових випадків
    if n == 1:
        ans = 2
    elif n == 2:
        ans = 4
    elif n == 3:
        ans = 7
    else:
        # Ініціалізація перших трьох значень
        f1, f2, f3 = 2, 4, 7
        
        # Обчислення для значень від 4 до n
        for _ in range(4, n + 1):
            f_current = (f1 + f2 + f3) % MOD
            f1, f2, f3 = f2, f3, f_current
        ans = f3

    print(f"Кількість шуканих послідовностей: {ans}")

if __name__ == "__main__":
    solve()