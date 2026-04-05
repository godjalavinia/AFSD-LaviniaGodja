import random
import time

def bubble_sort(lista):
    comparatii = 0
    mutari = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            comparatii += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                mutari += 1
    return lista, comparatii, mutari

def quick_sort(lista):
    comparatii = 0
    mutari = 0
    apeluri = 1
    if len(lista) <= 1:
        return lista, comparatii, mutari, apeluri
    pivot = lista[len(lista) // 2]
    stanga = []
    mijloc = []
    dreapta = []
    for x in lista:
        comparatii += 1
        if x < pivot:
            stanga.append(x)
            mutari += 1
        elif x > pivot:
            dreapta.append(x)
            mutari += 1
        else:
            mijloc.append(x)
    s1, c1, m1, a1 = quick_sort(stanga)
    s2, c2, m2, a2 = quick_sort(dreapta)
    return s1 + mijloc + s2, comparatii + c1 + c2, mutari + m1 + m2, apeluri + a1 + a2


def merge_sort(lista):
    comparatii = 0
    mutari = 0
    apeluri = 1
    if len(lista) <= 1:
        return lista, comparatii, mutari, apeluri
    mijloc = len(lista) // 2
    stanga, c1, m1, a1 = merge_sort(lista[:mijloc])
    dreapta, c2, m2, a2 = merge_sort(lista[mijloc:])
    rezultat = []
    i = j = 0
    while i < len(stanga) and j < len(dreapta):
        comparatii += 1
        if stanga[i] < dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1
        mutari += 1
    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])
    return rezultat, comparatii + c1 + c2, mutari + m1 + m2, apeluri + a1 + a2

def genereaza_lista(n, tip):
    if tip == "aleator":
        return [random.randint(0, 1000) for _ in range(n)]
    if tip == "sortat":
        return list(range(n))
    if tip == "invers":
        return list(range(n, 0, -1))
    if tip == "duplicate":
        return [random.randint(1, 5) for _ in range(n)]
    if tip == "aproape":
        lista = list(range(n))
        for _ in range(n // 10):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            lista[i], lista[j] = lista[j], lista[i]
        return lista

def este_sortata(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

def testeaza(algoritm, lista):
    start = time.time()
    rezultat = algoritm(lista)
    end = time.time()
    return rezultat, end - start

random.seed(42)
dimensiuni = [100, 500, 1000]
tipuri = ["aleator", "sortat", "invers", "duplicate", "aproape"]
rulari = 3
print(f"{'Algoritm':<12} {'Dim':<6} {'Tip':<10} {'Timp':<10} {'Comp':<10} {'Mutari':<10}")
for dim in dimensiuni:
    for tip in tipuri:
        lista_initiala = genereaza_lista(dim, tip)
        for nume, alg in [
            ("Bubble", bubble_sort),
            ("Quick", quick_sort),
            ("Merge", merge_sort)
        ]:
            timp_total = 0
            comp_total = 0
            mut_total = 0
            for _ in range(rulari):
                copie = lista_initiala.copy()
                rezultat, timp = testeaza(alg, copie)
                lista_sortata = rezultat[0]
                if not este_sortata(lista_sortata):
                    print("Eroare la sortare!")
                    continue
                timp_total += timp
                comp_total += rezultat[1]
                mut_total += rezultat[2]
            print(f"{nume:<12} {dim:<6} {tip:<10} {timp_total/rulari:<10.5f} {comp_total//rulari:<10} {mut_total//rulari:<10}")
