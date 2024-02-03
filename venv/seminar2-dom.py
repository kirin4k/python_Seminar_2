import math
import random
#
# #1
# num = int(input("Введите число монет: "))
# arr = []
# for i in range(num):
#     arr.append(random.randint(0,1))
# print(arr)
#
# count0= 0
# count1= 0
# for el in arr:
#     if el ==0:
#         count0 +=1
#     if el==1:
#         count1 +=1
#
# if count0<count1:
#     print(count0)
# else:
#     print(count1)

#2
# numbS= int(input("Введите значение Х+У: "))
# numbP= int(input("Введите значение Х*У: "))
#
# for x in range((numbS//2)+1):
#     for y in range((numbS-x)+1):
#         if x+y == numbS:
#             if x*y == numbP:
#                 print(x, y)



#3
# numb = int(input("Введите число степень которого хотите узнать: "))
# numberN = int(input("Введите число до которого будет подсчет: "))
#
# num = 0
# i = 0
# while num*numb<numberN:
#     num = numb**i
#     print(num)
#     i+=1
