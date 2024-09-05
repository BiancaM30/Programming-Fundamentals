from domeniu.entitati import get_zi_inceput, get_luna_inceput, get_an_inceput, get_zi_sfarsit, get_luna_sfarsit, get_an_sfarsit,get_destinatie, get_pret
from utils.utils import verifica_la_dreapta, verifica_la_stanga, diferenta_date
    
"""2a)"""
def cauta_pachet_dest(dictionar, dest_introdusa):
    """Functia cauta pachetele cu aceeasi destinatie ca cea introdusa si returneaza o lista cu numerele de ordine a acestor pachete
    Date de intrare: dictionar(dict), dest_introdusa(str)
    Date de iesire: keys(list)"""
    keys = []
    for key in dictionar:
        if get_destinatie(dictionar, key) == dest_introdusa:
            keys.append(key)
            
    return keys

"""2b)"""
def cauta_pachet_durata(dictionar, nr_zile):
    """Functia cauta pachetele cu o durata mai scurta decat "nr_zile" si returneaza o lista cu numerele de ordine a acestor pachete
    Date de intrare: dictionar(dict), nr_zile(str)
    Date de iesire: keys(list)"""
    keys = []
    for key in dictionar:
        if diferenta_date(int(get_zi_inceput(dictionar, key)), int(get_luna_inceput(dictionar, key)), int(get_an_inceput(dictionar, key)), int(get_zi_sfarsit(dictionar, key)), int(get_luna_sfarsit(dictionar, key)), int(get_an_sfarsit(dictionar, key))) < nr_zile:
            keys.append(key)
            
    return keys
    
"""2c)"""
def cauta_pachet_pret(dictionar, pret_introdus):
    """Functia cauta pachetele cu un pret mai mare decat cel introdus si returneaza o lista cu numerele de ordine a acestor pachete
    Date de intrare: dictionar(dict), pret_introdus(int)
    Date de iesire: keys(list)"""
    
    keys = []
    for key in dictionar:
        if int(get_pret(dictionar, key)) > pret_introdus :
            keys.append(key)
            
    return keys

"""3a)"""
def cauta_pachet_interval(dictionar, zi1, luna1, an1, zi2, luna2, an2):
    """Cautarea numerelor de ordine ale pachetelor de calatorie ce au data intr-un anumit interval
    Date de intare: dictionar(dict), zi1(int), luna1(int), an1(int), zi2(int), luna2(int), an2(int)
    Date de iesire: keys(lista ce contine numerele de ordine ale pachetelor ce respecta cerinta) """
    keys = []
    for key in dictionar:
        if verifica_la_dreapta(zi1, luna1, an1, int(get_zi_inceput(dictionar, key)), int(get_luna_inceput(dictionar, key)), int(get_an_inceput(dictionar, key))) and verifica_la_stanga(zi2, luna2, an2, int(get_zi_sfarsit(dictionar, key)), int(get_luna_sfarsit(dictionar, key)), int(get_an_sfarsit(dictionar, key))):
            keys.append(key)
            
    return keys

"""3b)"""
def cauta_pachet_dest_pret(dictionar, dest, suma_max):
    """Cautarea numerelor de ordine ale pachetelor de calatorie catre o anumita destinatie si cu pret mai mic decat o suma data
    Date de intare:  dictionar(dict), dest(str), suma_max(int)
    Date de iesire: keys(lista ce contine numerele de ordine ale pachetelor ce respecta cerinta) """
    
    gasit = False
    keys = []
    for key in dictionar:
        if get_destinatie(dictionar, key) == dest and int(get_pret(dictionar, key)) < suma_max:
            keys.append(key)
            gasit = True
    return keys

"""3c)"""
def cauta_pachete_data(dictionar, zi, luna, an):
    """Cautarea numerelor de ordine ale pachetelor de calatorie cu o anumita data de sfarsit
    Date de intare: dictionar(dict), zi(int), luna(int), an(int)
    Date de iesire: keys(lista ce contine numerele de ordine ale pachetelor ce respecta cerinta) """

    gasit = False
    keys = [] #Stocam intr o lista numerele pachetelor ce respecta cerinta, pentru a putea testa functia
    for key in dictionar:
        if int(get_zi_sfarsit(dictionar, key)) == zi and int(get_luna_sfarsit(dictionar, key)) == luna and int(get_an_sfarsit(dictionar, key)) == an:
            gasit = True
            keys.append(key)
            
    return keys   

"""4a)"""
def cauta_oferte_dest (dictionar, destinatie_introdusa):
    """Functia calculeaza si returneaza numarul de oferte gasite pentru o anumita destinatie
    Date de intrare:  dictionar(dict), destinatie_introdusa(str)
    Date de iesire: oferte(int)"""
    
    oferte = 0
    for key in dictionar:
        if get_destinatie(dictionar, key) == destinatie_introdusa:
            oferte += 1
            
    return oferte 

"""4b)"""
def ordonare_lista_dupa_pret(dictionar, lista_indici):
    """Functia creeaza o lista ordonata crescator in functie de pretul pachetelor din dictionar continute in lista primita ca parametru
    Date de intrare: dictionar(dict), lista_indici(list)
    Date de iesire: lista_ord(list)"""
    lista_pret = []
    lista_ord = []
    
    for i in lista_indici:
        lista_pret.append(int(get_pret(dictionar, i)))
        
    lista_ord=[x for _,x in sorted(zip(lista_pret,lista_indici))]
    return lista_ord

"""4c)"""
def calcul_medie_pret(dictionar, destinatie_introdusa, nr_oferte):
    """Functia calculeaza media de pret pentru o destinatie data si o returneaza
    Date de intrare: index(int), dictionar(dict), destinatie_introdusa(str), nr_oferte(int)
    Date de iesire: media(int)"""
    
    pret = 0
    for key in dictionar:
        if get_destinatie(dictionar, key) == destinatie_introdusa:
            pret += int(get_pret(dictionar, key))
    media = int(pret/nr_oferte)        
    return media

"""5a)"""
def filtrare_oferte_pret_dest(dictionar, pret_introdus, dest_introdusa):
    """Functia filtreaza pachetele si introduce intr-o lista indicii ofertelor cu aceeasi destinatie ca cea introdusa si cu un pret mai mic decat
    pretul introdus
    Date de intrare: dictionar(dict), pret_introdus(int), dest_introdusa(str)
    Date de iesire: keys(list) """
    keys = []
    for key in dictionar:
        if get_destinatie(dictionar, key) == dest_introdusa and int(get_pret(dictionar, key)) <= pret_introdus:
            keys.append(key)
            
    return keys

"""5b)"""
def filtrare_oferte_luna(dictionar, luna_introdusa):
    """Functia filtreaza pachetele si introduce intr-o lista indicii ofertelor ce nu presupun zile dintr-o anumita luna
    Date de intrare: dictionar(dict), luna_introdusa(int)
    Date de iesire: keys(list) """
    keys = []
    for key in dictionar:
        if str(get_luna_inceput(dictionar, key)) != str(luna_introdusa) and str(get_luna_sfarsit(dictionar, key)) != str(luna_introdusa):
            keys.append(key)
            
    return keys
          