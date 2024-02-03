#4
import random
count = int(input("Введите кол-во арбузов: "))

def addElements(num):
    list = []
    for i in range(num):
        # print("Введите вес арбуза номером - ", i+1 ,":")
        # # list[i] = input()
        list.append(random.randint(1,100))
    return list

weight = list(addElements(count))

#4.1
# max = max(weight)
# index1 = weight.index(max)
# min = min(weight)
# index2 = weight.index(min)
# print(f"Максимальный вес арбуза принадлежит номеру {index1+1} : {max}. Минимальный вес арбуза принадлежит номеру {index2+1} : {min}")
#4.2
def maximum(weight):
    max= weight[0]
    indexmax= 0
    for el in weight:
        if  el>max:
            max = el
            indexmax = weight.index(el)
    print(f"Максимальный вес арбуза принадлежит номеру {indexmax+1} : {max}.")

def minimum(weight):
    min = weight[0]
    indexmin= 0
    for el in weight:
        if el<min:
            min = el
            indexmin= weight.index(el)
    print(f"Максимальный вес арбуза принадлежит номеру {indexmin + 1} : {min}.")

maximum(weight)
minimum(weight)