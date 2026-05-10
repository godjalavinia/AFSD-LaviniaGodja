import random
import matplotlib.pyplot as plt

#Această funcție generează o singură rundă a jocului. După aruncarea zarurilor, verifică suma și returnează câștigul
def joaca_runda():
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    suma = zar1 + zar2
    castig = (suma == 7 or suma == 11)
    return castig

#Simularea Monte Carlo pentru un N fix
def simulare_monte_carlo(N):
    castiguri = 0
    for _ in range(N):
        if joaca_runda():
            castiguri += 1
    probabilitate = castiguri / N
    return probabilitate


# Test pentru valori diferite
valori_N = [100, 1000, 10000, 100000]
rezultate = []
print("Estimări Monte Carlo:\n")
for N in valori_N:
    p = simulare_monte_carlo(N)
    rezultate.append(p)
    print(f"N = {N:6d} -> probabilitate estimată = {p:.5f}")


# Rulări repetate pentru același N
N_fix = 10000
rulari = 10
estimari = []
print("\nRulări repetate pentru N = 10000:\n")
for i in range(rulari):
    p = simulare_monte_carlo(N_fix)
    estimari.append(p)
    print(f"Rulare {i+1}: {p:.5f}")


# Grafic 1 - Probabilitatea estimată
plt.figure(figsize=(8, 5))
plt.plot(valori_N, rezultate, marker='o', label='Estimare Monte Carlo')
plt.axhline(y=2/9, color='red', linestyle='--', label='Valoare teoretică')
plt.xscale('log')
plt.xlabel('Număr simulări (N)')
plt.ylabel('Probabilitate estimată')
plt.title('Estimarea probabilității de câștig')
plt.legend()
plt.grid(True)
plt.savefig('monte_carlo_probabilitate.png')
plt.show()


# Grafic 2 - Comparație între rulări
plt.figure(figsize=(8, 5))
plt.plot(range(1, rulari + 1), estimari, marker='o')
plt.axhline(y=2/9, color='red', linestyle='--', label='Valoare teoretică')
plt.xlabel('Numărul rulării')
plt.ylabel('Probabilitate estimată')
plt.title('Variația estimării între rulări')
plt.legend()
plt.grid(True)
plt.savefig('monte_carlo_rulari.png')
plt.show()