from operator import truediv


def bubble_sort_baza(lista):
    n=len(lista)
    schimbat = True
    while schimbat:
        schimbat = False
        i = 0
        while i < n-1:
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                schimbat = True
            i += 1
    return lista
lista = [5, 3, 8, 1, 4]
lista_sortata = bubble_sort_baza(lista.copy())
print(lista_sortata)


