import random
import statistics
import matplotlib.pyplot as plt


# Funcția generează vector
def genereaza_vector(n):
    return list(range(1, n + 1))


# Căutare randomizată
def cautare_randomizata(vector, valoare):
    n = len(vector)
    indici = list(range(n))
    random.shuffle(indici)
    pasi = 0
    for idx in indici:
        pasi += 1
        if vector[idx] == valoare:
            return idx, pasi


# 30 de rulări pentru același input
vector = genereaza_vector(1000)
valoare_cautata = 777
rulari = 30
lista_pasi = []
for _ in range(rulari):
    _, pasi = cautare_randomizata(vector, valoare_cautata)
    lista_pasi.append(pasi)


# Statistici
minim = min(lista_pasi)
maxim = max(lista_pasi)
medie = statistics.mean(lista_pasi)
print("\nRezultate pentru 30 de rulări:")
print(f"Minim pași: {minim}")
print(f"Maxim pași: {maxim}")
print(f"Media pașilor: {medie:.2f}")


# Experimente pentru dimensiuni diferite
valori_n = [100, 1000, 10000]
medii = []
for n in valori_n:
    vector = genereaza_vector(n)
    valoare = random.choice(vector)
    pasi_total = []
    for _ in range(30):
        _, pasi = cautare_randomizata(vector, valoare)
        pasi_total.append(pasi)
    medie = statistics.mean(pasi_total)
    medii.append(medie)
    print(f"n = {n:5d} -> media pașilor = {medie:.2f}")


# Grafic 1 - Pașii pentru fiecare rulare
plt.figure(figsize=(8, 5))
plt.plot(range(1, rulari + 1), lista_pasi, marker='o')
plt.xlabel('Rulare')
plt.ylabel('Număr pași')
plt.title('Variația numărului de pași')
plt.grid(True)
plt.savefig('las_vegas_rulari.png')
plt.show()


# Grafic 2 - Media pașilor vs dimensiunea vectorului
plt.figure(figsize=(8, 5))
plt.plot(valori_n, medii, marker='o', label='Media pașilor')
plt.xlabel('Dimensiunea vectorului')
plt.ylabel('Număr mediu de pași')
plt.title('Media pașilor în funcție de dimensiunea vectorului')
plt.legend()
plt.grid(True)
plt.savefig('las_vegas_medii.png')
plt.show()