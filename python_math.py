import math
import cmath

def circle_area():
    try:
        r = float(input("Введите радиус круга: "))
        area = math.pi * r ** 2
        print(f"Площадь круга: {area:.4f}")
    except ValueError:
        print("Ошибка: радиус должен быть числом!")

def factorial():
    try:
        n = int(input("Введите целое неотрицательное число: "))
        if n < 0:
            print("Ошибка: факториал определён только для неотрицательных чисел!")
        else:
            print(f"Факториал {n}: {math.factorial(n)}")
    except ValueError:
        print("Ошибка: введите целое число!")

def quadratic_equation():
    try:
        a = float(input("Введите коэффициент a (≠0): "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        if a == 0:
            print("Ошибка: a не должно быть равно нулю!")
            return
        d = b ** 2 - 4 * a * c
        # обработка комплексных корней, если дискриминант < 0
        sqrt_d = cmath.sqrt(d)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
    except ValueError:
        print("Ошибка: все коэффициенты должны быть числами!")

def main():
    menu = (
        "\nВыберите действие:\n"
        "1: Площадь круга\n"
        "2: Факториал\n"
        "3: Квадратное уравнение\n"
        "0: Выход\n"
    )
    while True:
        print(menu)
        choice = input("Ваш выбор: ")
        if choice == "1":
            circle_area()
        elif choice == "2":
            factorial()
        elif choice == "3":
            quadratic_equation()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор!")

if __name__ == "__main__":
    main()
