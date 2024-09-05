def valideaza_zi(zi):  
    while(True):
        try:
            zi = int(zi)
            if zi < 1 or zi > 31:
                zi = input("Valoare invalida")
            else:
                return zi    
        except ValueError:
                    print("Introduceti un numar intreg")
                    zi = input()
                    
def valideaza_luna(luna):  
    while(True):
        try:
            luna = int(luna)
            if luna < 1 or luna > 12:
                luna = input("Valoare invalida")
            else:
                return luna    
        except ValueError:
                    print("Introduceti un numar intreg")
                    luna = input()  
                     
def valideaza_an(an):  
    while(True):
        try:
            an = int(an)
            if an < 0:
                an = input("Valoare invalida")
            else:
                return an    
        except ValueError:
                    print("Introduceti un numar intreg")
                    an = input()
                    
def valideaza_destinatie(dest):    
    while(True):
        if dest =="":
            dest = input("Destinatie invalida")
        else:
            return dest   
        
def valideaza_pret(pret):  
    while(True):
        try:
            pret = int(pret)
            if pret < 0:
                pret = input("Valoare invalida")
            else:
                return pret    
        except ValueError:
                    print("Introduceti un numar intreg")
                    pret = input()    
                    
def valideaza_comanda(sir):  
    """Functia verifica daca comanda de la 1b) este valida
    Date de intrare: sir(str)
    Date de iesire: sir(str)"""
    while(True):
        if sir == "zi_inceput" or sir == "luna_inceput" or sir =="an_inceput" or sir == "zi_sfarsit" or sir == "luna_sfarsit" or sir =="an_sfarsit" or sir =="destinatie" or sir =="pret":   
            return sir
        else:
            sir = input("Comanda invalida! Introduceti o alta comanda:")
            
def valideaza_valoare(val,cmd):
    """Functia verifica daca valoarea introdusa la 1b), in functie de comanda "cmd" este valida
    Date de intrare: val(str), cmd(str)
    Date de iesire: val(str)"""
    if cmd == "zi_inceput" or cmd == "zi_sfarsit":
        val = valideaza_zi(val)
    elif cmd == "luna_inceput" or cmd == "luna_sfarsit":
        val = valideaza_luna(val)    
    elif cmd == "an_inceput" or cmd == "an_sfarsit":
        val =  valideaza_an(val)    
    elif cmd == "destinatie":
        val = valideaza_destinatie(val)
    elif cmd == "pret":
        val = valideaza_pret(val)  
    return val          