from domeniu.entitati import get_zi_inceput, get_luna_inceput, get_an_inceput, get_zi_sfarsit, get_luna_sfarsit, get_an_sfarsit, get_destinatie, get_pret
def tiparire_pachete(dictionar, lista):
    """Functia tipareste pachetele cu o anumita proprietate din dictionarul principal 
    Date de intrare: dictionar(dict), lista (lista - contine numele pachetelor ce trebuiesc tiparite)
    Date de iesire: - """
    
    if lista == []:
        tiparire_mesaj_negativ
        
    for i in lista:
        print("Pachetul numarul", i)
        print(get_zi_inceput(dictionar,i), "/", get_luna_inceput(dictionar, i), "/", get_an_inceput(dictionar, i))
        print(get_zi_sfarsit(dictionar,i), "/", get_luna_sfarsit(dictionar, i), "/", get_an_sfarsit(dictionar, i))
        print(get_destinatie(dictionar, i))
        print(get_pret(dictionar,i))
        print('\n')
        
def tiparire_mesaj_negativ():
    print("Nu am gasit un pachet care sa corespunda cerintelor dumneavoastra")
    
def afis_oferte_dest(nr):
    """Functia afiseaza numarul de oferte catre o anumita destinatie
    Date de intrare: nr(int)
    Date de iesire: - """
    
    if nr !=0:
        if nr == 1:
            print("Exista o oferta catre destinatia dorita")
        else:
            print("Exista", nr, "oferte catre destinatia dorita!")
            
    else:
        print("Nu exista oferte catre destinatia dorita")
        
def afis_medie_pret (medie):
    """Se afiseaza media de pret pentru destinatia aleasa
    Date de intrare: medie(int)
    Date de iesire: - """
    
    print('Media de pret pentru destinatia aleasa este: ', medie)            