"""1a)"""
def creeaza_entitate(z1, l1, an1, z2, l2, an2, destinatie_introdusa, pret_introdus):
    """Functia creeaza o noua entitate de tipul dictionar
    Date de intrare: z1(str), l1(str), an1(str), z2(str), l2(str), an2(str), destinatie_introdusa(str), pret_introdus(str)
    Date de iesire: entitate(dict)"""
    
    entitate ={"zi_inceput": z1,
                "luna_inceput": l1,
                "an_inceput": an1,
                "zi_sfarsit": z2,
                "luna_sfarsit": l2,
                "an_sfarsit": an2,
                "destinatie":destinatie_introdusa,
                "pret": pret_introdus
               }
    return entitate

def adauga_entitate_la_dictionar(dictionar, entitate, index):
    """Functia adauga o noua entitate in dictionar
    Date de intrare: dictionar(dict), entitate(dict), index(int)
    Date de iesire: dictionar(dict)"""
    dictionar.update({
                      index : entitate
                    })
    return dictionar







def get_zi_inceput(dictionar, i):
    return dictionar[i]["zi_inceput"]

def get_luna_inceput(dictionar, i):
    return dictionar[i]["luna_inceput"]

def get_an_inceput(dictionar, i):
    return dictionar[i]["an_inceput"]

def get_zi_sfarsit(dictionar, i):
    return dictionar[i]["zi_sfarsit"]

def get_luna_sfarsit(dictionar, i):
    return dictionar[i]["luna_sfarsit"]

def get_an_sfarsit(dictionar, i):
    return dictionar[i]["an_sfarsit"]

def get_destinatie(dictionar, i):
    return dictionar[i]["destinatie"]

def get_pret(dictionar, i):
    return dictionar[i]["pret"]

def set_zi_inceput(dictionar, i, val):
    dictionar[i]["zi_inceput"] = val
    
def set_luna_inceput(dictionar, i, val):
    dictionar[i]["luna_inceput"] = val    
    
def set_an_inceput(dictionar, i, val):
    dictionar[i]["an_inceput"] = val    
    
def set_zi_sfarsit(dictionar, i, val):
    dictionar[i]["zi_sfarsit"] = val
    
def set_luna_sfarsit(dictionar, i, val):
    dictionar[i]["luna_sfarsit"] = val    
    
def set_an_sfarsit(dictionar, i, val):
    dictionar[i]["an_sfarsit"] = val  
             
def set_destinatie(dictionar, i, val):
    dictionar[i]["destinatie"] = val      
    
def set_pret(dictionar, i, val):
    dictionar[i]["pret"] = val       
    
"""1b)"""    
def modifica_pachet(dictionar, nr_pachet, sir, val):
    """Functia modifica elementul "sir" din pachetul "nr_pachet" cu valoarea "val"
    Date de intrare: dictionar(dict), nr_pachet(str), sir(str), val(str)
    Date de iesire: dictionar(dict)
    """
    if sir == "zi_inceput":
        set_zi_inceput(dictionar, nr_pachet, val)
    elif sir =="luna_inceput":
        set_luna_inceput(dictionar, nr_pachet, val)    
    elif sir =="an_inceput":
        set_an_inceput(dictionar, nr_pachet, val)
    elif sir == "zi_sfarsit":
        set_zi_sfarsit(dictionar, nr_pachet, val)
    elif sir =="sfarsit":
        set_luna_sfarsit(dictionar, nr_pachet, val)    
    elif sir =="an_sfarsit":
        set_an_sfarsit(dictionar, nr_pachet, val)
    elif sir == "destinatie":
        set_destinatie(dictionar, nr_pachet, val) 
    elif sir == "pret":
        set_pret(dictionar, nr_pachet, val)      
    return dictionar 
   
def transforma_in_lista(dictionar):
    """Functia transforma un dictionar de dictionare in lista de disctionare
    Date de intrare: dictionar(dict)
    Date de iesire: lista(list)"""
    
    lista = []
    for el in dictionar:
        lista.append(dictionar[el])
    return lista

def transforma_in_dictionar(lista):
    """Functia transforma o lista de dictionare in dictionar de dictionare 
    Date de intrare: lista(list)
    Date de iesire: dictionar(dict)"""
    
  
    dictionar = {}
    for el in range(len(lista)):
       dictionar[el+1] = lista[el]
    return dictionar
    
"""6"""
def clona_pachet(pachet):
    """Functia copiaza elementele dintr-un pachet intr-un pachet nou
    Date de intrare: pachet(dict)
    Date de iesire: pachet_nou(dict)
    """
    return {"zi_inceput": pachet["zi_inceput"],
            "luna_inceput": pachet["luna_inceput"],
            "an_inceput": pachet["an_inceput"],
            "zi_sfarsit": pachet["zi_sfarsit"],
            "luna_sfarsit": pachet["luna_sfarsit"],
            "an_sfarsit": pachet["an_sfarsit"],
            "destinatie": pachet["destinatie"],
            "pret": pachet["pret"]
          }
def copie_lista(lista):
    """Functia creeaza o copie a listei 
    Date de intrare: lista(list)
    Date de iesire: copie(list)
    """
    copie = []
    for el in lista:
        copie.append(clona_pachet(el))
        
    return copie        
