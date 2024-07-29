import time
from functools import wraps

# Zadanie 2
def measure_time(unit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            execution_time = end_time - start_time
            if unit == 'seconds':
                print(f"Czas wykonania funkcji {func.__name__}: {execution_time:.6f} sekund.")
            elif unit == 'microseconds':
                print(f"Czas wykonania funkcji {func.__name__}: {execution_time * 1e6:.6f} mikrosekund.")
            else:
                raise ValueError("Nieprawidłowa jednostka czasu. Wybierz 'seconds' lub 'microseconds'.")

            return result
        return wrapper
    return decorator


@measure_time(unit='seconds')
def some_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

result = some_function(1000000)  # Wyświetli czas wykonania funkcji some_function w sekundach

@measure_time(unit='microseconds')
def another_function(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum

result = another_function(1000000)  # Wyświetli czas wykonania funkcji another_function w mikrosekundach
