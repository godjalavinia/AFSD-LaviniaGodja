elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       5,        8]

#Partea A
#1
for i in range (len(elevi)) :
    print(f"{elevi[i]} are nota {note[i]}")

#2
j= max(note)
print(j)
for i in range (len(elevi)) :
    if note[i] == j :
        print(elevi[i])

#3
avg= sum(note) / len(note)
print(avg)

#4
for i in range (len(elevi)) :
    if note[i] >= 5 :
        print(elevi[i])

print()
#Partea B

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

#5
for i in range (len(elevi)) :
    if note[i] < 10 :
        note[i] +=1

#6
elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)

#7
poz = 0
for i in range (len(elevi)) :
    if  elevi[i] == elev_de_sters :
        poz = i

elevi.pop(poz)
note.pop(poz)

print(elevi)
print(note)

#8
for i in range (len(elevi)) :
    print(f"{elevi[i]} - {note[i]}")

print()
#Partea C
interogari_nume = ["Ana", "Mara", "Elena", "stop"]
absente = [1, 0, 2, 3, 0]

#9
frr=0
i = 0
while interogari_nume[i] != "stop" :
    if interogari_nume[i] == elevi[i] :
        print(note[i])
    else:  print("Nu exista")
    i += 1

#10
nr_trecuti = 0
nr_netrecuti=0
for i in range (len(note)) :
    if note[i] >= 5 :
        nr_trecuti += 1
    if note[i] < 5 :
        nr_netrecuti += 1
print(nr_trecuti)
print(nr_netrecuti)

#11
promo = []
for i in range (len(note)) :
    if note[i] >= 5 :
        promo.append(note[i])
if(promo != []) :
    avg = sum(promo) / len(promo)
print(avg)
