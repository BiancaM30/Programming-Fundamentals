from domeniu.entitati import creeaza_entitate, adauga_entitate_la_dictionar, copie_lista, transforma_in_lista, transforma_in_dictionar
from domeniu.cautari import cauta_pachet_dest, filtrare_oferte_luna
from ui.tipariri import tiparire_pachete
from utils.utils import sterge

def meniu_batch(dictionar, index, lista_undo): 
    print("adaugare : Adauga pachet de calatorie")
    print("stergere: Stergerea tuturor pachetelor de calatorie disponibile pentru o destinatie data")
    print("filtrare: Eliminarea ofertelor in care sejurul presupune zile dintr-o anumita luna")
    print("undo: Refacerea ultimei operatii")
    
    sir = input("Introduceti comanda:")
    sir = sir.split(";")
    
    for cmd in sir:
        args = cmd.split(" ")
        if args[0] == "adaugare":
            lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
            z1 = args[1]
            l1 = args[2]
            a1 = args[3]
            z2 = args[4]
            l2 = args[5]
            a2 = args[6]
            destinatie = args[7]
            pret = args[8]
            entitate = creeaza_entitate(z1, l1, a1, z2, l2, a2, destinatie, pret)
            adauga_entitate_la_dictionar(dictionar, entitate, index)
            index += 1
            
        elif args[0] == "stergere":
            lista_undo.append(copie_lista(transforma_in_lista(dictionar)))
            destinatie = args[1]
            print(destinatie)
            lista =[]
            lista = cauta_pachet_dest(dictionar, destinatie)
            dictionar = sterge(dictionar, lista)
            
        elif args[0] == "filtrare":   
            luna= args[1]
            lista = []
            lista = filtrare_oferte_luna(dictionar, luna)
            tiparire_pachete(dictionar, lista) 
         
        elif args[0] == "undo":
            if(len(lista_undo) == 1):
                dictionar = transforma_in_dictionar(lista_undo[0])
                lista_undo = []
            elif len(lista_undo)>1:
                dictionar = transforma_in_dictionar(lista_undo[-1])
                lista_undo.pop()  
    print(dictionar)             