import time

def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Function launched at {timestamp} with result {result}"

        with open("log.txt", "a") as file:
            file.write(log_message + "\n")

        return result

    return wrapper

@log_result
def sum_args(*args):
    result = sum(args)
    return result
