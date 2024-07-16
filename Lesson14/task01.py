# Как вы помните из прошлых лекций, тройные двойные кавычки сразу после
# заголовка класса, функции или метода превращают текст внутри в строку
# документации соответствующего объекта. Например так может выглядеть
# простейшая (без оптимизации) функция, проверяющая является ли число простым
# или составным используя нахождение остатка от деления.
def is_prime(p: int) -> bool:
    """
        Checks the number P for simplicity using finding the remainder of the division in the range [2, P).
        >>> is_prime(42)
        False
        >>> is_prime(71)
        True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)
