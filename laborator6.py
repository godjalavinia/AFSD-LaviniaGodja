import json

# Citire date din JSON
def citeste_investitii():
    with open("investitii.json", "r") as f:
        investitii = json.load(f)
    return investitii


# Afișare investiții
def afiseaza_investitii(investitii):
    print("\nInvestiții disponibile:\n")
    for i in investitii:
        print(f"{i['nume']} | Cost: {i['cost']} | Profit: {i['profit']} | "
              f"Categorie: {i['categorie']} | Risc: {i['risc']}")



# Eliminare risc ridicat
def elimina_risc_ridicat(investitii):
    rezultat = []
    for i in investitii:
        if i["risc"] != "ridicat":
            rezultat.append(i)
    return rezultat



# Programare Dinamică
def optimizare(investitii, buget):
    n = len(investitii)
    # tabel DP
    dp = [[0 for j in range(buget + 1)] for i in range(n + 1)]
    # construire tabel
    for i in range(1, n + 1):
        cost = investitii[i - 1]["cost"]
        profit = investitii[i - 1]["profit"]
        for b in range(buget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + profit
                )
            else:
                dp[i][b] = dp[i - 1][b]
    # reconstruire soluție
    b = buget
    selectate = []
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selectate.append(investitii[i - 1])
            b -= investitii[i - 1]["cost"]
    return dp[n][buget], selectate


# Afișare rezultat
def afiseaza_rezultat(buget, profit, selectate):
    cost_total = 0
    for i in selectate:
        cost_total += i["cost"]
    print("\n===== REZULTAT =====")
    print("Buget:", buget)
    print("Profit maxim:", profit)
    print("Cost total:", cost_total)
    print("Buget rămas:", buget - cost_total)
    print("\nInvestiții selectate:")
    for i in selectate:
        print("-", i["nume"])



investitii = citeste_investitii()
investitii = elimina_risc_ridicat(investitii)
afiseaza_investitii(investitii)
buget = int(input("\nIntroduceți bugetul: "))
profit, selectate = optimizare(investitii, buget)
afiseaza_rezultat(buget, profit, selectate)