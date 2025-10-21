articol = "Întâlnirea a avut loc la invitația domnului Șaman Yousefvand, însărcinatul cu afaceri al misiunii diplomatice iraniene în România."

#1
lungime= len(articol)
prima_parte= articol[:lungime//2]
a_doua_parte= articol[lungime//2:]
print(prima_parte)
print(a_doua_parte)

#2
prima_parte= prima_parte.upper()
print(prima_parte)
prima_parte.strip( )
print(prima_parte)

#3
a_doua_parte= a_doua_parte[::-1]
print(a_doua_parte)
a_doua_parte= a_doua_parte.capitalize()
print(a_doua_parte)
a_doua_parte= a_doua_parte.replace(".","")
a_doua_parte= a_doua_parte.replace(",","")
a_doua_parte= a_doua_parte.replace("?","")
a_doua_parte= a_doua_parte.replace("!","")
print(a_doua_parte)

#4
articol=prima_parte+a_doua_parte
<<<<<<< HEAD
print(articol)
=======
print(articol)
>>>>>>> d8d56f9d7ef4f0452dc3377c96eebf799bbc59b0
