

#3
def enterNum():
    while True:
        num = int(input("Введите кол-во дней от 1 до 100: "))
        if 1<=num<=100:
            return num

def addElements(num):
    list = []
    for i in range(num):
        while True:
            print("Введите температуру(от -50 до 50 градусов) дня номером - ", i + 1, ":")
            temp  = int(input())
            if -50 <= temp <= 50:
                list.append(temp)
                break
    return list

def plusTemp(temp):
    length = 0
    maxlength = 0
    for el in temp:
        if el>0:
            length+=1
            if length>maxlength:
                maxlength = length
        else:
            length = 0
    return maxlength

count = enterNum()
temperatures = list(addElements(count))
days=plusTemp(temperatures)
print(days)