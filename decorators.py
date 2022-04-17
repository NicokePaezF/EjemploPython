from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        tine_elapsed = final_time - initial_time
        print("Pasaron " + str(tine_elapsed.total_seconds()) + " Segundos")

    return wrapper


# Decorator
@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre="Nicoke"):
    print("Hola " + nombre)


suma(15, 25)
random_func()
saludo("Nicoke")
