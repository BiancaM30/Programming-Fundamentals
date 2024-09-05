def verificare_intreg(x):
    """Functia verifica daca stringul x poate fi convertit intr-un numar intreg. Daca da, atunci realizeaza conversia. In caz contrar,
    afiseaza mesajul corespunzator si preia un nou string de la tastatura.
    Date de intrare: x(str)
    Date de iesire: x(int)"""
    
    try:
        x = int(x)
    except ValueError:
        print("Introduceti un numar intreg")
        x = input()
        
    return x

def sterge(dictionar, lista):
    """Functia sterge pachetele din dictionar ale caror numere de ordine se gasesc in lista si returneaza dictionarul modificat
    Date de intrare: dictionar(dict), lista(list)
    Date de iesire: dictionar(dict)"""
    
    for i in lista:
        dictionar.pop(i)
    return dictionar

def verifica_la_dreapta(zi1, luna1, an1, zi2, luna2, an2):
    """Functia verifica daca o data de forma zi2/luna2/an2 se afla dupa o data de forma zi1/luna1/an1
    Date de intrare: zi1(int), luna1(int), an1(int), zi2(int), luna2(int), an2(int)
    Date de iesire: True/False """
    if an2 < an1: return False
    if an2 > an1: return True
    #altfel inseamna ca anii sunt egali
    if luna2 < luna1: return False
    if luna2 > luna1: return True
    #altfel inseamna ca lunile sunt egale
    if zi2 < zi1: return False
    return True

def verifica_la_stanga(zi1, luna1, an1, zi2, luna2, an2):
    """Functia verifica daca o data de forma zi2/luna2/an2 ianintea unei date de forma zi1/luna1/an1
    Date de intrare: zi1(int), luna1(int), an1(int), zi2(int), luna2(int), an2(int)
    Date de iesire: True/False """
    if an2 > an1: return False
    if an2 < an1: return True
    #altfel inseamna ca anii sunt egali
    if luna2 > luna1: return False
    if luna2 < luna1: return True
    #altfel inseamna ca lunile sunt egale
    if zi2 > zi1: return False
    return True

def diferenta_date(z1, l1, a1, z2, l2, a2):
    """Functia calculeaza cate zile sunt intre 2 date de forma z1/l1/a1 - z2/l2/a2 fara a include z2
    Calculam numarul unei zile "nr1" in calendarul gregorian dupa formula: 365*an + an/4 - an/100 + an/400 + zi + (153*luna+8)/5
    Pentru a afla cate zile sunt intre cele 2 date calculam nr2-nr1
    Date de intrare: z1(int), l1(int), a1(int), z2(int), l2(int), a2(int)
    Date de iesire: dif(int)
    """
    if l1 <= 2:
        l1 += 12
        a1 -= 1
        
    if l2 <=2:
        l2 += 12
        a2 -= 1
    
    nr1 = int(365*a1) +int(a1/4)- int(a1/100) + int(a1/400) + int(z1) + int((153*l1+8)/5)
    nr2 = int(365*a2) +int(a2/4)- int(a2/100) + int(a2/400) + int(z2) + int((153*l2+8)/5)
   
    dif = nr2-nr1
    return dif