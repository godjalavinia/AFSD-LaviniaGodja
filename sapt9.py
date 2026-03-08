A = [[" ", " ", " "],
     [" ", " ", " "],
     [" ", " ", " "]]

def afiseaza(A):
    for row in A:
        print(row)

def citeste_mutareX(A,jucator1):
    linia = int(input("Linia: "))
    coloana = int(input("Coloana: "))
    if A[linia][coloana] == " " and linia < 3 and coloana < 3 and linia >= 0 and coloana >=0:
        A[linia][coloana] = jucator1
    else:
        print("Pozitie invalida")
        citeste_mutareX(A,jucator1)

def citeste_mutare0(A,jucator2):
    linia = int(input("Linia: "))
    coloana = int(input("Coloana: "))
    if A[linia][coloana] == " " and linia < 3 and coloana < 3 and linia >= 0 and coloana >=0:
        A[linia][coloana] = jucator2
    else:
        print("Pozitie invalida")
        citeste_mutare0(A,jucator2)

def stare_joc(A):
    nr_linii = len(A)
    nr_coloane = len(A[0])

    #verificare diagonala principala
    k = 0
    for i in range(nr_linii):
        for j in range(nr_coloane):
            if i == j and A[i][j] == "X":
                k += 1
    if k == 3:
        return "X a castigat"

    k = 0
    for i in range(nr_linii):
        for j in range(nr_coloane):
            if i == j and A[i][j] == "0":
                k += 1
    if k == 3:
        return "0 a castigat"

    #verificare diagonala secundara
    k = 0
    for i in range(nr_linii):
        for j in range(nr_coloane):
            if i + j == nr_linii - 1 and A[i][j] == "0":
                k += 1
    if k == 3:
        return "0 a castigat"

    k = 0
    for i in range(nr_linii):
        for j in range(nr_coloane):
            if i + j == nr_linii - 1 and A[i][j] == "X":
                k += 1
    if k == 3:
        return "X a castigat"

    #verificare coloane
    k = 0
    j = 0
    for i in range(nr_linii):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"

    k = 0
    j = 1
    for i in range(nr_linii):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"
    k = 0
    j = 2
    for i in range(nr_linii):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"
    k = 0
    j = 0
    for i in range(nr_linii):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"
    k = 0
    j = 1
    for i in range(nr_linii):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"
    k = 0
    j = 2
    for i in range(nr_linii):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"

    #verificare linii
    k = 0
    i = 0
    for j in range(nr_coloane):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"

    k = 0
    i = 1
    for j in range(nr_coloane):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"

    k = 0
    i = 2
    for j in range(nr_coloane):
        if A[i][j] == "X":
            k += 1
    if k == 3:
        return "X a castigat"

    k = 0
    i = 0
    for j in range(nr_coloane):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"

    k = 0
    i = 1
    for j in range(nr_coloane):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"

    k = 0
    i = 2
    for j in range(nr_coloane):
        if A[i][j] == "0":
            k += 1
    if k == 3:
        return "0 a castigat"
    #Verificare tabla plina
    k = 0
    i = 0
    j = 0
    for i in range(nr_linii):
        for j in range(nr_coloane):
            if A[i][j] != " ":
                k += 1
    if k == 9:
        return "EGAL"
    return "CONTINUA"

start = "CONTINUA"
afiseaza(A)
while start == "CONTINUA":
    citeste_mutareX(A, 'X')
    afiseaza(A)
    start = stare_joc(A)
    if start == "CONTINUA":
        citeste_mutare0(A, '0')
        afiseaza(A)
    start = stare_joc(A)
print(start)