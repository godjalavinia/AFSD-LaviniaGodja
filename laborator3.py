import csv
import json


def citeste_produse_csv(fisier):
    produse = {}
    with open(fisier, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            produse[row["id"]] = {
                "nume": row["nume"],
                "pret": float(row["pret"]),
                "stoc": int(row["stoc"])
            }
    return produse

def citeste_reduceri_json(fisier):
    with open(fisier, 'r', encoding='utf-8') as f:
        return json.load(f)

def afiseaza_meniu(produse):
    print("\n----- MENIU PRODUSE -----")
    for idp, p in produse.items():
        print(f"{idp}. {p['nume']} - {p['pret']} lei (stoc: {p['stoc']})")

def adauga_produs(comanda, produse, idp, cant):
    if idp not in produse:
        print("Produs inexistent!")
        return
    if cant <= 0:
        print("Cantitate invalida!")
        return
    deja = comanda.get(idp, 0)
    stoc_real = produse[idp]["stoc"] - deja
    if cant > stoc_real:
        print("Stoc insuficient!")
        return
    comanda[idp] = deja + cant
    print("Produs adaugat!")

def scade_produs(comanda, idp, cant):
    if idp not in comanda:
        print("Produsul nu este in comanda!")
        return
    if cant <= 0:
        print("Cantitate invalida!")
        return
    if cant >= comanda[idp]:
        del comanda[idp]
    else:
        comanda[idp] -= cant
    print("Produs actualizat!")

def goleste_comanda(comanda):
    comanda.clear()

def calculeaza_total(comanda, produse):
    total = 0
    for idp, cant in comanda.items():
        total += produse[idp]["pret"] * cant
    return total

def calculeaza_reducere(total, tip, reduceri):
    if tip == "" or tip not in reduceri:
        return 0
    r = reduceri[tip]
    if total < r["prag"]:
        print("Prag minim neindeplinit!")
        return 0
    if r["tip"] == "procent":
        return total * r["valoare"] / 100
    elif r["tip"] == "fix":
        return r["valoare"]
    return 0

def genereaza_bon(comanda, produse, total, reducere):
    linii = []
    linii.append("----- BON FISCAL -----")
    for idp, cant in comanda.items():
        p = produse[idp]
        subtotal = p["pret"] * cant
        linii.append(f"{p['nume']} x{cant} = {subtotal:.2f} lei")
    linii.append("----------------------")
    linii.append(f"Total: {total:.2f} lei")
    linii.append(f"Reducere: {reducere:.2f} lei")
    linii.append(f"Total final: {total - reducere:.2f} lei")
    return "\n".join(linii)

def scrie_bon_txt(fisier, text):
    with open(fisier, 'w', encoding='utf-8') as f:
        f.write(text)


produse = citeste_produse_csv("produse.csv")
reduceri = citeste_reduceri_json("reduceri.json")
comanda = {}
reducere_curenta = ""

while True:
    print("\n----- MENIU PRINCIPAL -----")
    print("1 - Afisare produse")
    print("2 - Adauga produs")
    print("3 - Scade produs")
    print("4 - Aplicare reducere")
    print("5 - Finalizare comanda")
    print("6 - Anulare comanda")
    print("0 - Iesire")
    opt = input("Alege optiunea: ")
    if opt == "1":
        afiseaza_meniu(produse)
    elif opt == "2":
        idp = input("ID produs: ")
        cant = int(input("Cantitate: "))
        adauga_produs(comanda, produse, idp, cant)
    elif opt == "3":
        idp = input("ID produs: ")
        cant = int(input("Cantitate de scazut: "))
        scade_produs(comanda, idp, cant)
    elif opt == "4":
        total = calculeaza_total(comanda, produse)
        if total == 0:
            print("Comanda este goala!")
            continue
        print("\n1 - student")
        print("2 - happy")
        print("3 - cupon")
        print("4 - fara reducere")
        print("0 - inapoi")
        alegere = input("Alege reducere: ")
        mapping = {
            "1": "student",
            "2": "happy",
            "3": "cupon",
            "4": ""
        }
        if alegere in mapping:
            reducere_curenta = mapping[alegere]
            reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
            print(f"Reducere: {reducere:.2f} lei")
    elif opt == "5":
        total = calculeaza_total(comanda, produse)
        reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
        bon = genereaza_bon(comanda, produse, total, reducere)
        print("\n" + bon)
        scrie_bon_txt("bon.txt", bon)
        # actualizare stoc
        for idp, cant in comanda.items():
            produse[idp]["stoc"] -= cant
        goleste_comanda(comanda)
        reducere_curenta = ""
    elif opt == "6":
        goleste_comanda(comanda)
        reducere_curenta = ""
        print("Comanda anulata!")
    elif opt == "0":
        print("Program inchis.")
        break
    else:
        print("Optiune invalida!")
