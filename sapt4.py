def  timp_in_format(secunde: int):
    secunde_initiale = secunde
    minute = 0
    ore = 0
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    else:
        if secunde < 60:
            return f"{secunde_initiale} inseamna 00:00:{secunde}"
    if secunde >= 60:
        while secunde >= 60:
            secunde -= 60
            minute += 1
        if secunde < 10 and minute < 10:
            return f"{secunde_initiale} inseamna 00:0{minute}:0{secunde}"
        else:
            if secunde > 10 and secunde < 60 and minute >10 and minute < 60:
                return f"{secunde_initiale} inseamna 00:{minute}:{secunde}"
    if minute >= 60:
        while minute >= 60:
            minute -= 60
            ore += 1
        if secunde < 10 and  minute < 10  and ore > 0 and ore < 10:
            return f"{secunde_initiale} inseamna 0{ore}:0{minute}:0{secunde}"
        if secunde > 10 and secunde < 60 and  minute < 10  and ore > 0 and ore < 10:
            return f"{secunde_initiale} inseamna 0{ore}:0{minute}:{secunde}"
        else:
            if secunde > 10 and secunde < 60 and minute > 10 and minute < 60 and ore > 10:
                return f"{secunde_initiale} inseamna {ore}:{minute}:{secunde}"
n = timp_in_format(3600)
print(n)