
#2

def enterNum():
    while True:
        num = int(input("Введите натуральное число: "))
        if num>1:
            return num

def fibo(number):
    fib1 = fib2 = 1
    fibnum = 2
    while fib2<number:
        fibsum = fib1+fib2
        fib1 = fib2
        fib2 = fibsum
        fibnum +=1
    if fib2 !=number:
        return -1
    return fibnum

number = enterNum()
fib= fibo(number)
print(fib)