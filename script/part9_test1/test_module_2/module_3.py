creatVar = locals()

for i in range(10000, 100000):
	creatVar["v" + str(i)] = i

def add_sum(list_int):
    sum = 0
    for i in list_int:
        sum += int(i)
    return sum