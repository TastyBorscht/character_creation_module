from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет введеное число."""
    if your_number <= 0:
        return
    your_sqrt = calculatesquareroot(your_number)

    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {your_sqrt}')


calc(25.5)
