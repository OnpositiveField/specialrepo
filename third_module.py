
def factorial(n):
    if __name__ == "__main__":
        use_math_functions()
    
    try:
        if n < 0:
            print("Ошибка: факториал определён только для неотрицательных чисел!")
        else:
            print(f"Факториал {n}: {math.factorial(n)}")
    except ValueError:
        print("Ошибка: введите целое число!")
