import math
#1
#1.1
# numb = int(input("Введите число, факториал которого нужно найти: "))
# number3 = math.factorial(numb)
# print(number3)
#1.2
# numb = int(input("Введите число, факториал которого нужно найти: "))
def factorial(number):
    factor = 1
    i=2
    if number == 0 or number == 1:
        return factor
    while i<=number:
        factor *=i
        i +=1
    return factor

# number2 = factorial(numb)
# print(number2)
#1.2.1
def inputIntAndPositiveNum():
    while True:
        str = input("Введите положительное число, факториал которого нужно найти: ")
        if str.isdigit():
            numb = int(str)
            return numb

# def PositiveInt():
#     while True:
#         number = inputIntNum()
#         if number>=0:
#             return number

number3 = factorial(inputIntAndPositiveNum())
print(number3)
