glosar = {
  "variabilă": {
    "definitie": "nume asociat unei valori",
    "categorie": "fundamente",
    "exemplu": "x = 10"
  },
  "dicționar": {
    "definitie": "structură de date bazată pe perechi cheie-valoare",
    "categorie": "structuri de date",
    "exemplu": "{'a': 1, 'b': 2}"
  }
}

def afisare_meniu():
    print("----- MENIU GLOSAR -----")
    print("Optiuni:")
    print("1. Adauga termen")
    print("2. Cautare exacta a unui termen")
    print("3. Cautare partiala a termenilor")
    print("4. Actualizare termen")
    print("5. Stergere termen")
    print("6. Afisare glosar")
    print("7. Statistici")
    print("8. Salvare")
    print("9. Incarcare")
    print("0. Iesire")

def adauga_termen():
    print()
    termen = input("Introduceti termen: ")
    definitie = input("Introduceti definitie: ")
    categorie = input("Introduceti categorie: ")
    exemplu = input("Introduceti exemplu: ")
    if termen in glosar:
        print("Termenul deja exista in glosar. ")
        return
    glosar[termen] = {
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }

def cautare_exacta():
    print()
    termen = input("Introduceti termen: ")
    if termen in glosar:
        info = glosar[termen]
        print("Definiție:", info["definitie"])
        print("Categorie:", info["categorie"])
        print("Exemplu:", info["exemplu"])
    else:
        print("Termenul nu există.")

def cautare_partiala():
    print()
    fragment= input("Introduceti termen: ")
    gasit = False
    for termen in glosar:
        if fragment in termen:
            print("Termen:", termen)
            print("Definiție:", glosar[termen]["definitie"])
            print("Categorie:", glosar[termen]["categorie"])
            print("Exemplu:", glosar[termen]["exemplu"])
            gasit = True
    if not gasit:
        print("Nu s-au găsit termeni.")

def actualizare_termen():
    print()
    termen = input("Introduceti termen: ")
    if termen not in glosar:
        print("Termenul nu există.")
        return
    else:
        print("Ce doriți să modificați?")
        print("1. Definiție")
        print("2. Categorie")
        print("3. Exemplu")
        optiune = input("Alegeți opțiunea: ")
        if optiune == "1":
            glosar[termen]["definitie"] = input("Noua definiție: ")
        elif optiune == "2":
            glosar[termen]["categorie"] = input("Noua categorie: ")
        elif optiune == "3":
            glosar[termen]["exemplu"] = input("Noul exemplu: ")
        else:
            print("Opțiune invalidă.")
            return
        print("Termen actualizat.")

def sterge_termen():
    print()
    termen = input("Introduceti termen: ")
    if termen in glosar:
        glosar.pop(termen)
        print("Termen șters.")
    else:
        print("Termenul nu există.")

def afisare_glosar():
    print()
    for termen, info in glosar.items():
        print()
        print("Termen:", termen)
        print("Definitie:", info["definitie"])
        print("Categorie:", info["categorie"])
        print("Exemplu:", info["exemplu"])

def statistici():
    print()
    total = len(glosar)
    categorii = {}
    for info in glosar.values():
        cat = info["categorie"]
        categorii[cat] = categorii.get(cat, 0) + 1
    print("Număr total de termeni:", total)
    print("Termeni pe categorii:")
    for cat, nr in categorii.items():
        print(cat, ":", nr)

def salvare_CSV():
    print()
    nume_fisier = input("Numele fișierului CSV: ")
    with open(nume_fisier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["termen", "definitie", "categorie", "exemplu"])
        writer.writeheader()
        for termen, info in glosar.items():
            writer.writerow({
                "termen": termen,
                "definitie": info["definitie"],
                "categorie": info["categorie"],
                "exemplu": info["exemplu"]
            })
    print("Glosarul a fost salvat.")

def incarcare_din_CSV():
    print()
    nume_fisier = input("Numele fișierului CSV: ")
    with open(nume_fisier, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            glosar[row["termen"]] = {
                "definitie": row["definitie"],
                "categorie": row["categorie"],
                "exemplu": row["exemplu"]
            }
    print("Glosarul a fost încărcat.")

if __name__ == "__main__":
  while (True):
        print()
        afisare_meniu()
        optiune = input("Alege o optiune: ")
        if optiune == "1":
            adauga_termen()
        elif optiune == "2":
            cautare_exacta()
        elif optiune == "3":
            cautare_partiala()
        elif optiune == "4":
            actualizare_termen()
        elif optiune == "5":
            sterge_termen()
        elif optiune == "6":
            afisare_glosar()
        elif optiune == "7":
            statistici()
        elif optiune == "8":
            salvare_CSV()
        elif optiune == "9":
            incarcare_din_CSV()
        elif optiune == "0":
            print("Program închis.")
            break
        else:
            print("Optiune invalida")