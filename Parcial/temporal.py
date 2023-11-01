lista = ["Emmett", "Marty", "Biff"]

swap = True

while(swap):
    swap = False
    for i in range (len(lista) - 1):
        if (lista [i]) > (lista[i+1]):
            swap = True
            lista[i], lista[i+1] = lista[i+1], lista[i]

print(lista)