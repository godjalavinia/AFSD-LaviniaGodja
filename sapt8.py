def my_function(text):
    caractere = list(text)
    pozitie = 1
    lungime = len(caractere)
    caractere[pozitie], caractere[lungime - 2] = caractere[lungime - 2], caractere[pozitie]
    print(caractere)
my_function('hello')