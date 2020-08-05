def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

try:
    n = int(input("Введите число для вычисления числа фибоначи "));
except ValueError:
    print("Некорректные данные");
else:
    print("ответ ", fib(n))
