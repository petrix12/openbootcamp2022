def esBisiesto(anho):
    if ((anho % 4 == 0) and not (anho % 100 == 0)):
        return True
    elif((anho % 4 == 0) and (anho % 400 == 0)):
        return True
    return False

anho = 2002
print("El año", anho, "es bisiesto" if esBisiesto(anho) else "no es bisiesto")