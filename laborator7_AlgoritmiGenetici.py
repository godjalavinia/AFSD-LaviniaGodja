import random
import matplotlib.pyplot as plt


# 1. DEFINIREA PROBLEMEI
candidati = [
    {"nume": "Ana",      "cost": 10, "scor": 60},
    {"nume": "Bogdan",   "cost": 20, "scor": 100},
    {"nume": "Carmen",   "cost": 15, "scor": 90},
    {"nume": "Dan",      "cost": 12, "scor": 70},
    {"nume": "Elena",    "cost": 18, "scor": 95},
    {"nume": "Florin",   "cost": 25, "scor": 120},
    {"nume": "George",   "cost": 8,  "scor": 40},
    {"nume": "Horia",    "cost": 30, "scor": 150},
    {"nume": "Ioana",    "cost": 16, "scor": 85},
    {"nume": "Julia",    "cost": 14, "scor": 75}
]
BUGET_MAXIM = 80
print("Lista candidatilor:\n")
for i, c in enumerate(candidati):
    print(f"{i+1}. {c['nume']} | Cost: {c['cost']} | Scor: {c['scor']}")
print("\nBuget maxim:", BUGET_MAXIM)


# 2. REPREZENTAREA UNEI SOLUTII
# Cromozom binar:
# 1 = candidatul este selectat
# 0 = candidatul nu este selectat

# Exemplu:
# [1,0,1,0,0,1,0,0,1,0]
# inseamna ca sunt selectati:
# Ana, Carmen, Florin, Ioana

NUMAR_GENE = len(candidati)


# 3. FUNCTIA DE FITNESS
def calculeaza_fitness(cromozom):
    cost_total = 0
    scor_total = 0
    for gena, candidat in zip(cromozom, candidati):
        if gena == 1:
            cost_total += candidat["cost"]
            scor_total += candidat["scor"]

    # Penalizare daca depasim bugetul
    if cost_total > BUGET_MAXIM:
        penalizare = (cost_total - BUGET_MAXIM) * 10
        return scor_total - penalizare
    return scor_total


def calculeaza_cost(cromozom):
    return sum(
        gena * candidat["cost"]
        for gena, candidat in zip(cromozom, candidati)
    )


def calculeaza_scor(cromozom):
    return sum(
        gena * candidat["scor"]
        for gena, candidat in zip(cromozom, candidati)
    )


# 4. POPULATIA INITIALA
DIMENSIUNE_POPULATIE = 30
def genereaza_cromozom():
    return [random.randint(0, 1) for _ in range(NUMAR_GENE)]


def genereaza_populatie():
    return [genereaza_cromozom() for _ in range(DIMENSIUNE_POPULATIE)]


populatie = genereaza_populatie()
# Evaluare initiala
fitness_initial = [calculeaza_fitness(c) for c in populatie]
cel_mai_bun_initial = populatie[
    fitness_initial.index(max(fitness_initial))
]
print("\nCea mai buna solutie initiala:")
print(cel_mai_bun_initial)
print("Fitness:", calculeaza_fitness(cel_mai_bun_initial))


# 5. OPERATORI GENETICI
# SELECTIE - Turneu
def selectie(populatie):
    candidat1 = random.choice(populatie)
    candidat2 = random.choice(populatie)
    if calculeaza_fitness(candidat1) > calculeaza_fitness(candidat2):
        return candidat1
    return candidat2


# CROSSOVER - un punct
def crossover(parinte1, parinte2):
    punct = random.randint(1, NUMAR_GENE - 1)
    copil1 = parinte1[:punct] + parinte2[punct:]
    copil2 = parinte2[:punct] + parinte1[punct:]
    return copil1, copil2


# MUTATIE
RATA_MUTATIE = 0.05
def mutatie(cromozom):
    for i in range(NUMAR_GENE):
        if random.random() < RATA_MUTATIE:
            cromozom[i] = 1 - cromozom[i]


# 6. RULAREA PE MAI MULTE GENERATII

NUMAR_GENERATII = 100
istoric_best = []
istoric_medie = []
cea_mai_buna_solutie = None
cel_mai_bun_fitness = -999999
for generatie in range(NUMAR_GENERATII):
    generatie_noua = []
    while len(generatie_noua) < DIMENSIUNE_POPULATIE:
        # Selectie parinti
        parinte1 = selectie(populatie)
        parinte2 = selectie(populatie)

        # Crossover
        copil1, copil2 = crossover(parinte1, parinte2)

        # Mutatie
        mutatie(copil1)
        mutatie(copil2)
        generatie_noua.append(copil1)
        generatie_noua.append(copil2)
    populatie = generatie_noua[:DIMENSIUNE_POPULATIE]

    # Evaluare generatie
    fitnessuri = [calculeaza_fitness(c) for c in populatie]
    best_generatie = max(fitnessuri)
    medie_generatie = sum(fitnessuri) / len(fitnessuri)
    istoric_best.append(best_generatie)
    istoric_medie.append(medie_generatie)

    # Memorare cea mai buna solutie
    index_best = fitnessuri.index(best_generatie)
    if best_generatie > cel_mai_bun_fitness:
        cel_mai_bun_fitness = best_generatie
        cea_mai_buna_solutie = populatie[index_best]


# AFISAREA SOLUTIEI FINALE
print("\n=================================================")
print("CEA MAI BUNA ECHIPA GASITA")
print("=================================================")

echipa = []
for gena, candidat in zip(cea_mai_buna_solutie, candidati):
    if gena == 1:
        echipa.append(candidat["nume"])
print("Membri echipa:", echipa)
cost_final = calculeaza_cost(cea_mai_buna_solutie)
scor_final = calculeaza_scor(cea_mai_buna_solutie)
print("Cost total:", cost_final)
print("Scor total:", scor_final)
print("Fitness:", cel_mai_bun_fitness)
if cost_final <= BUGET_MAXIM:
    print("Buget respectat!")
else:
    print("Buget depasit!")


# 7. GRAFIC

plt.figure(figsize=(10, 5))
plt.plot(istoric_best, label="Fitness maxim")
plt.plot(istoric_medie, label="Fitness mediu")
plt.title("Evolutia algoritmului genetic")
plt.xlabel("Generatia")
plt.ylabel("Fitness")
plt.legend()
plt.savefig("evolutie_algoritm_genetic.png")
plt.show()