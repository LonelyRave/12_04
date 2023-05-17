import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запам'ятовуємо початковий час

        # Викликаємо функцію, яку хочемо виміряти
        result = func(*args, **kwargs)

        end_time = time.time()  # Запам'ятовуємо час після виконання функції
        execution_time = end_time - start_time  # Обчислюємо час виконання

        print(f"The function {func.__name__} is completed in {execution_time} seconds")

        return result

    return wrapper

@measure_time
def my_function():

    time.sleep(4)
