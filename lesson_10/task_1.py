import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"The function {func.__name__} is completed in {execution_time} seconds")

        return result

    return wrapper


@measure_time
def my_function():
    time.sleep(4)
