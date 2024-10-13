# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if x > 1:
            if all((x % i) != 0 for i in range(2, int(x ** 0.5)+1)):
                print('Простое')
            else:
                print('Составное')
        return x
    return wrapper

@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)
