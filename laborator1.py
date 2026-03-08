produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]
tip_reducere = 0

def afisare_meniu(produse, preturi, stoc):
    print()
    print("----- MENIU -----")
    for i in range (len(produse)):
        print(i, produse[i], preturi[i], stoc[i])

def adaugare_produs(cant_comanda,stoc, index, cantitate):
    if index < 0 or index >= len(stoc):
        print("Index invalid")
        return
    if cantitate <= 0:
        print("Cantitate invalida")
        return
    stoc_disponibil = stoc[index] - cant_comanda[index]
    if cantitate > stoc_disponibil:
        print("Stoc insuficient")
        return
    cant_comanda[index] += cantitate
    print("Produs adaugat in comanda")

def scadere_produs(cant_comanda, index, cantitate):
    if index < 0 or index >= len(cant_comanda):
        print("Index invalid")
        return
    if cantitate <= 0:
        print("Cantitate invalida")
        return
    if cantitate > cant_comanda[index]:
        print("Nu exista atatea produse in comanda")
        return
    cant_comanda[index] -= cantitate
    print("Produs scazut din comanda")

def calcul_total(cant_comanda, preturi):
    total = 0
    for i in range (len(cant_comanda)):
        total += cant_comanda[i] * preturi[i]
    return total

def stabilire_reducere(total, tip_reducere):
    reducere = 0
    if tip_reducere == "student":
        if total >= 30.00:
            reducere = 0.10 * total
        else:
            print("Total insuficient pentru student")
    elif tip_reducere == "happy":
        if total >= 50.00:
            reducere = 0.15 * total
        else:
            print("Total insuficient pentru happy")
    elif tip_reducere == "cupon":
        if total >= 25.00:
            reducere = 7.00
        else:
            print("Total insuficient pentru cupon")
    if reducere > total:
        reducere = total
    return reducere

def finalizare_comanda(stoc, cant_comanda):
    for i in range(len(stoc)):
        stoc[i] -= cant_comanda[i]
        cant_comanda[i] = 0

def finalizare_comanda(stoc, cant_comanda):
    for i in range(len(stoc)):
        stoc[i] -= cant_comanda[i]
        cant_comanda[i] = 0

def afisare_bon(produse, preturi, cant_comanda, reducere):
    print()
    print("----- BON -----")
    total = 0
    for i in range(len(produse)):
        if cant_comanda[i] > 0:
            subtotal = cant_comanda[i] * preturi[i]
            total += subtotal
            print(produse[i], "x", cant_comanda[i], "=", subtotal)
    total_final = total - reducere
    print("Total:", total)
    print("Reducere:", reducere)
    print("Total final:", total_final)

def anulare_comanda(cant_comanda):
    for i in range(len(cant_comanda)):
        cant_comanda[i] = 0

while True:
    print()
    print("----- MENIU PRINCIPAL -----")
    print("1. Afisare produse")
    print("2. Adauga produs")
    print("3. Scade produs")
    print("4. Aplicare reducere")
    print("5. Finalizare comanda")
    print("6. Anulare comanda")
    print("0. Iesire")

    optiune = input("Alege optiunea: ")
    if optiune == "0":
        print("Program inchis")
        break
    elif optiune == "1":
        afisare_meniu(produse, preturi, stoc)
    elif optiune == "2":
        index = int(input("Index produs: "))
        cant = int(input("Cantitate: "))
        adaugare_produs(cant_comanda, stoc, index, cant)
    elif optiune == "3":
        index = int(input("Index produs: "))
        cant = int(input("Cantitate de scazut: "))
        scadere_produs(cant_comanda, index, cant)
    elif optiune == "4":
        total = calcul_total(cant_comanda, preturi)
        if total == 0:
            print("Comanda este goala")
            continue
        print()
        print("----- SUB_MENIU REDUCERI -----")
        print("1. Reducere student")
        print("2. Reducere happy")
        print("3. Reducere cupon")
        print("4. Fara reducere")
        print("5. Inapoi")
        r = input("Alege reducere: ")
        if r == "1":
            tip_reducere = "student"
            reducere_curenta = stabilire_reducere(total, "student")
            print("Reducere student aplicata")
        elif r == "2":
            tip_reducere = "happy"
            reducere_curenta = stabilire_reducere(total, "happy")
            print("Reducere happy aplicata")
        elif r == "3":
            tip_reducere = "cupon"
            reducere_curenta = stabilire_reducere(total, "cupon")
            print("Reducere cupon aplicata")
        elif r == "4":
            reducere_curenta = 0
            tip_reducere = None
            print("Fara reducere")
        elif r == "5":
            pass

    elif optiune == "5":
        total = calcul_total(cant_comanda, preturi)
        if total == 0:
            print("Nu exista produse in comanda")
            continue
        reducere_finala = stabilire_reducere(total, tip_reducere)
        afisare_bon(produse, preturi, cant_comanda, reducere_finala)
        finalizare_comanda(stoc, cant_comanda)
        reducere_curenta = 0
        tip_reducere = None
    elif optiune == "6":
        anulare_comanda(cant_comanda)
        reducere_curenta = 0
        tip_reducere = None
        print("Comanda anulata")
    else:
        print("Optiune invalida")