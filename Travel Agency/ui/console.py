from domeniu.entitati import creeaza_entitate, adauga_entitate_la_dictionar, set_an_inceput, modifica_pachet, copie_lista, transforma_in_lista, transforma_in_dictionar
from ui.validatori import valideaza_zi, valideaza_luna, valideaza_an, valideaza_destinatie, valideaza_pret, valideaza_comanda, valideaza_valoare
from domeniu.cautari import cauta_pachet_dest, cauta_pachet_pret, cauta_pachet_interval, cauta_pachet_dest_pret, cauta_pachete_data, cauta_oferte_dest, ordonare_lista_dupa_pret, calcul_medie_pret, filtrare_oferte_pret_dest, filtrare_oferte_luna, cauta_pachet_durata
from utils.utils import sterge, verificare_intreg
from ui.tipariri import tiparire_mesaj_negativ, tiparire_pachete, afis_oferte_dest, afis_medie_pret
  
def meniu():
    """Functia tipareste pe ecran meniul
    Date de intare: -
    Date de iesire: - """
    
    print("ADAUGARE")
    print("1.Adauga pachet de calatorie")
    print("2.Modifica pachet de calatorie")
    
    print("STERGERE")
    print("3.Stergerea tuturor pachetelor de calatorie disponibile pentru o destinatie data")
    print("4.Stergerea tuturor pachetelor de calatorie care au o durata mai scurta decat un numar de zile dat")
    print("5.Stergerea tuturor pachetelor de calatorie care au pretul mai mare decat o suma data")
    
    print("CAUTARE")
    print("6.Tiparirea pachetelor de calatorie care presupun un sejur intr-un interval dat")
    print("7.Tiparirea pachetelor de calatorie cu o destinatie data si cu pret mai mic decat o suma data.")
    print("8.Tiparirea pachetelor de calatorie cu o anumita data de sfarsit.")
    
    print("RAPOARTE")
    print("9.Tiparirea numarului de oferte pentru o destinatie data.")
    print("10.Tiparirea tuturor pachetelor disponibile intr-o anumita perioada citita de la tastatura in ordinea crescatoare a pretului.")
    print("11.Tiparirea mediei de pret pentru o destinatie data.")
    
    print("FILTRARE")
    print("12.Eliminarea ofertelor care au un pret mai mare decat cel dat si o destinatie diferita de cea citita de la tastatura")
    print("13.Eliminarea ofertelor in care sejurul presupune zile dintr-o anumita luna")

    print("UNDO")
    print("14.Refacerea ultimei operatii")
    
"""1a)"""    
def ui_adauga_pachet_calatorie(index, dictionar, lista_undo):  
    """Functia adauga un nou pachet de calatorie in dictionarul principal sub forma unui nou dictionar, a carui cheie este egala cu indexul curent.
    De asemenea, are loc validarea datelor introduse de utilizator.
    Date de intrare: index(int - numarul pachetului ce va fi introdus in dictionar), dictionar(dict)
    Date de iesire: index """
    
    lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
    z1 = valideaza_zi(input("Introduceti ziua de inceput:"))
    l1 = valideaza_luna(input("Introduceti luna de inceput:"))
    an1 = valideaza_an(input("Introduceti anul de inceput:"))
    z2 = valideaza_zi(input("Introduceti ziua de sfarsit:"))  
    l2 = valideaza_luna(input("Introduceti luna de sfarsit:"))
    an2 = valideaza_an(input("Introduceti anul de sfarsit:"))
    destinatie_introdusa = valideaza_destinatie(input("Introduceti destinatia:"))
    pret_introdus = valideaza_pret(input("Introduceti pretul in euro:"))
  
    entitate = creeaza_entitate(z1, l1, an1, z2,l2, an2, destinatie_introdusa, pret_introdus)
    dictionar = adauga_entitate_la_dictionar(dictionar, entitate, index)
    
    index +=1
    return index
    return dictionar  

"""1b)"""
def ui_modifica_pachet_calatorie(dictionar, lista_undo):
    """Functia citeste de la tastatura numarul pachetului ce trebuie modificat, ce anume trebuie modificat si noua valoare pe care o va lua elementul din dictionar
    Date de intrare: dictionar(dict)
    Date de iesire: dictionar(dict)"""
    
    lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
    nr_pachet = verificare_intreg(input("Introduceti numarul pachetului pe care doriti sa il modificati"))
    sir = valideaza_comanda(input("Introduceti ce anume doriti sa modificati: zi_inceput/luna_inceput/an_inceput/zi_sfarsit/luna_sfarsit/an_sfarsit/destinatie/pret"))
    val = valideaza_valoare(input("Modificati in valoarea: "), sir)
    nr_pachet = str(nr_pachet)
    modifica_pachet(dictionar, nr_pachet, sir, val)
    print("Modificare realizata!")
    return dictionar 
    
"""2a)"""
def ui_sterge_pachet_dest(dictionar, lista_undo):
    """Functia citeste de la tastatura o destinatie, modifica dictionarul in memorie si il afiseaza
    Se vor sterge toate pachetele cu destinatia introdusa
    Date de intrare: dictionar(dict)
    Date de iesire: dictionar(dict)"""
    
    lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
    dest_introdusa = input("Introduceti o destinatie:")
    lista =[]
    lista = cauta_pachet_dest(dictionar, dest_introdusa)
    dictionar = sterge(dictionar, lista)
    return dictionar

"""2b)"""
def ui_sterge_pachet_durata(dictionar, lista_undo):
    """Functia citeste de la tastatura numarul de zile minim.
    Se vor sterge pachetele cu o durata mai scurta decat numarul de zile introdus
    Date de intrare:dictionar(dict)
    Date de iesire: dictionar(dict)"""
  
    lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
    nr_zile = verificare_intreg(input("Introduceti numarul de zile minim"))
    lista = []
    lista = cauta_pachet_durata(dictionar, nr_zile)
    dictionar = sterge(dictionar, lista)
    return dictionar

"""2c)"""
def ui_sterge_pachet_pret(dictionar, lista_undo):
    """Functia citeste de la tastatura un pret si modifica dictionarul in memorie
    Se vor sterge toate pachetele de calatorie care au pretul mai mare decat o suma data
    Date de intrare: dictionar(dict)
    Date de iesire: dictionar(dict)"""
    
    lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
    pret_introdus = verificare_intreg(input("Introduceti o suma:"))
    lista = []
    lista = cauta_pachet_pret(dictionar, pret_introdus)
    dictionar = sterge(dictionar, lista)
    return dictionar

"""3a)"""
def ui_pachet_interval_dat(dictionar):
    """Functia citeste un interval de timp dat (de forma:10/08/2018 - 24/08/2018) 
    Se vor cauta pachetele de calatorie ce presupun un sejur in acel interval
    Date de intare: dictionar(dict)
    Date de iesire: - """
    z1 = valideaza_zi(input("Introduceti ziua de inceput:"))
    l1 = valideaza_luna(input("Introduceti luna de inceput:"))
    an1 = valideaza_an(input("Introduceti anul de inceput:"))
    z2 = valideaza_zi(input("Introduceti ziua de sfarsit:"))  
    l2 = valideaza_luna(input("Introduceti luna de sfarsit:"))
    an2 = valideaza_an(input("Introduceti anul de sfarsit:"))

    lista = []
    lista = cauta_pachet_interval(dictionar, z1, l1, an1, z2, l2, an2)
    if lista == []:
        tiparire_mesaj_negativ()
    else:
        tiparire_pachete(dictionar, lista)
        
"""3b)"""        
def ui_pachet_dest_pret (dictionar):
    """Functia  preia datele introduse de utilizator privind o anume destinatie si o suma de bani alocata excursiei 
    Se vor cauta pachetele de calatorie catre acea destinatie si cu pretul mai mic decat suma introdusa
    Date de intare: index(int), dictionar(dict)
    Date de iesire: - """
    
    dest = input("Introduceti o destinatie:")
    suma = verificare_intreg(input("Introduceti pretul maxim:"))

    lista = []
    lista = cauta_pachet_dest_pret(dictionar, dest, suma)

    tiparire_pachete(dictionar, lista) 

"""3c)"""
def ui_pachet_data(dictionar):
    """Functia preia datele introduse de utilizator privind o anumita data de sfarsit a excursiei
    Se vor cauta pachetele de calatorie cu acea data de sfarsit.
    Date de intare: index(int), dictionar(dict)
    Date de iesire: - """
    
    zi = valideaza_zi(input("Introduceti ziua de sfarsit:"))
    luna = valideaza_luna(input("Introduceti luna de sfarsit:"))
    an = valideaza_an(input("Introduceti anul de sfarsit:"))
    
    lista = []
    lista = cauta_pachete_data(dictionar, zi, luna, an)
    
    tiparire_pachete(dictionar, lista) 
    
"""4a)"""
def ui_numar_oferte_dest (dictionar):
    """Functia principala ce preia destinatia introdusa de utilizator 
    Se cauta numarul de oferte pentru o anumita destinatie.
    Date de intrare: dictionar(dict)
    Date de iesire: - """
    
    destinatie_introdusa = input("Introduceti destinatia dorita:")
    nr = cauta_oferte_dest (dictionar, destinatie_introdusa)
    afis_oferte_dest(nr)    
    
"""4b)"""    
def ui_pachet_interval_dat_crescator(dictionar):
    """Functia principala care citeste un interval de timp dat (de forma:10/08/2018 - 24/08/2018) 
    Se vor cauta pachetele de calatorie ce presupun un sejur in acel interval si se vor afisa in ordinea crescatoare a pretului
    Date de intare: dictionar(dict)
    Date de iesire: - """
    zi1 = valideaza_zi(input("Introduceti ziua de inceput:"))
    luna1 = valideaza_luna(input("Introduceti luna de inceput:"))
    an1 = valideaza_an(input("Introduceti anul de inceput:"))
    zi2 = valideaza_zi(input("Introduceti ziua de sfarsit:"))  
    luna2 = valideaza_luna(input("Introduceti luna de sfarsit:"))
    an2 = valideaza_an(input("Introduceti anul de sfarsit:"))

    lista = []
    lista = cauta_pachet_interval(dictionar, zi1, luna1, an1, zi2, luna2, an2)
    if lista == []:
        tiparire_mesaj_negativ()
    else:
        lista_ordonata = ordonare_lista_dupa_pret(dictionar, lista)
        tiparire_pachete(dictionar, lista_ordonata)   
        
"""4c)"""    
def ui_medie_pret(dictionar):
    """Functia principala ce preia destinatia introdusa de utilizator si apeleaza alte 3 functii
    Se cere media de pret pentru destinatia data
    Date de intrare: dictionar(dict)
    Date de iesire: - """
    
    destinatie_introdusa = input("Introduceti destinatia dorita:")
    nr_oferte = cauta_oferte_dest(dictionar, destinatie_introdusa)
    if nr_oferte == 0:
        tiparire_mesaj_negativ()
    else:    
        medie = calcul_medie_pret(dictionar, destinatie_introdusa, nr_oferte)
        afis_medie_pret(medie)
        
"""5a)"""   
def ui_eliminare_oferte_pret_dest(dictionar):
    """Functia citeste un pret si o destinatie introdusa de utilizator
    Se cere eliminarea ofertelor care au un pret mai mare decat cel dat si o destinatie diferita de cea citita
    Date de intrare: dictionar(dict)
    Date de iesire: - """
    pret_introdus = valideaza_pret(input("Introduceti un pret:"))
    dest_introdusa = valideaza_destinatie(input("Introduceti o destinatie:"))
    lista = []
    lista = filtrare_oferte_pret_dest(dictionar, pret_introdus, dest_introdusa)
    tiparire_pachete(dictionar, lista)     
    
"""5b)"""
def ui_eliminare_oferte_luna(dictionar):
    """Functia citeste luna introdusa de utilizator 
    Se cere eliminarea ofertelor in care sejurul presupune zile dintr-o anumita luna
    Date de intrare: dictionar(dict)
    Date de iesire: - """
    
    luna_introdusa = valideaza_luna(input("Introduceti o luna:"))
    lista = []
    lista = filtrare_oferte_luna(dictionar, luna_introdusa)
    tiparire_pachete(dictionar, lista) 
    
"""6"""
def ui_undo(dictionar, lista_undo):
    if(len(lista_undo) == 1):
        dictionar = transforma_in_dictionar(lista_undo[0])
        lista_undo = []
    elif len(lista_undo)>1:
        dictionar = transforma_in_dictionar(lista_undo[-1])
        lista_undo.pop()
        
    print("Lista a revenit la ce exista inainte de ultima operatie care a modificat-o")   
    return dictionar, lista_undo