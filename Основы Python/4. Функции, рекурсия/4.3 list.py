def ll(list1):
    if len(list1) > 2:
	    return{list1[0]: ll(list1[1:])}
    else:
        return{list1[0]: list1[1]}

n = int(input("Введите число элементов списка "));
list1 = []
print('Введите элементы списка ');
for i in range(n):
    list1.append(input());
print(ll(list1));
