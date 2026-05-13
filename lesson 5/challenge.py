
def mbledhi(lista):
    rezultati = 0
    for i in lista:
        if i %2 ==0:
            rezultati = rezultati+i
    return rezultati

lista = [2, 5, 7, 8]

print(mbledhi(lista))