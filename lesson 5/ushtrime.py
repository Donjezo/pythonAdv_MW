list =[2,5,7,8]
list2 =[2,5,7,8,10,14]



def mbledhjaNumravQift(list):
    rezultati = 0

    for i in list:
        if i % 2 == 0:
            rezultati = rezultati + i

    return rezultati


print(mbledhjaNumravQift(list))
print(mbledhjaNumravQift(list2))