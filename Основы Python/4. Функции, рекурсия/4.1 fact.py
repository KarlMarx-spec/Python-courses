# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fact(n):
    x = 1;
    if (n!=0):
        if (n<0):
            print("Число должно быть больше нуля");
        if (n>0):
            for i in range(1,n+1):
                x=x*i;
            print("Ответ ", x);
    else:
        print("Ответ 0");


try:
    n = int(input("Введите число для вычисления факториала "));
except ValueError:
    print("Некорректные данные");
else:
    fact(n);






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
