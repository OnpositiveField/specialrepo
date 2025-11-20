import python_math 

def use_math_functions():
    print("Вызов функции circle_area() без пользовательского ввода:")
    # Можно вызвать с input, или изменить в python_math.py, чтобы принимать параметры вместо интерактива
    python_math.circle_area()  # вызывает input()
    
    print("Вызов функции factorial() без пользовательского ввода:")
    python_math.factorial()  # вызывает input()
    
    print("Вызов функции quadratic_equation() без пользовательского ввода:")
    python_math.quadratic_equation()  # вызывает input()
    
    print("Вы можете модифицировать python_math.py, чтобы функции принимали параметры.")

if __name__ == "__main__":
    use_math_functions()
