list1 = [10,6,38,2,5,12,0,7]
list2 = [44,0,8,2,5,9,55]

list3 = []

for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)

print ("os numeros iguais são " +str(list3) )