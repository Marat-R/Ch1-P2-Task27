# Напишите функцию где исходный список содержит положительные и отрицательные
# числа. Требуется положительные поместить в один список, а отрицательные - в другой.

list1 = [1,2,3,4,5,5,6,-1,-2,-3,-4,-5,-6,-6]
list_plus = []
list_minus = []

def list_split(list1):
    for i in list1:
        if i > 0 and i not in list_plus:
            list_plus.append(i)
        elif i < 0 and i not in list_minus:
            list_minus.append(i)

list_split(list1)

print(list_plus)
print(list_minus)