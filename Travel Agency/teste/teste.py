from teste.init_dict import initializare_dictionar
from domeniu.cautari import calcul_medie_pret, cauta_oferte_dest, cauta_pachet_dest, cauta_pachet_dest, cauta_pachet_dest_pret,cauta_pachet_interval, cauta_pachet_durata,cauta_pachet_interval, cauta_pachet_pret, cauta_pachete_data, ordonare_lista_dupa_pret, filtrare_oferte_luna, filtrare_oferte_pret_dest
from utils.utils import verifica_la_dreapta, verifica_la_stanga, diferenta_date 
def test_verifica_la_dreapta():
    """Testarea functiei care verifica daca o data de forma zi2/luna2/an2 se afla dupa data z1/luna1/luna1
    Date de intare: -
    Date de iesire: - """
    assert(verifica_la_dreapta(14, 5, 2020, 15, 5, 2018) == False)
    assert(verifica_la_dreapta(14, 5, 2020, 10, 1, 2021) == True)
    assert(verifica_la_dreapta(14, 5, 2020, 15, 6, 2020) == True)
    assert(verifica_la_dreapta(14, 5, 2020, 15, 4, 2020) == False)
    assert(verifica_la_dreapta(23, 6, 2020, 30, 6, 2020) == True)
    assert(verifica_la_dreapta(14, 5, 2020, 13, 5, 2020) == False)
    assert(verifica_la_dreapta(18, 7, 2020, 18, 7, 2020) == True)

def test_verifica_la_stanga():
    """Testarea functiei care verifica daca o data de forma zi2/luna2/an2 se afla inaintea datei z1/luna1/luna1
    Date de intare: -
    Date de iesire: - """
    assert(verifica_la_stanga(13, 2, 2018, 2, 2, 2021) == False)
    assert(verifica_la_stanga(13, 2, 2018, 10, 3, 2017) == True)
    assert(verifica_la_stanga(20, 5, 2020, 12, 3, 2020) == True)
    assert(verifica_la_stanga(15, 7, 2021, 2, 8, 2021) == False)
    assert(verifica_la_stanga(13, 2, 2020, 20, 2, 2020) == False)
    assert(verifica_la_stanga(13, 2, 2020, 12, 2, 2020) == True)
    assert(verifica_la_stanga(13, 2, 2018, 13, 2, 2018) == True)
    

def test_diferenta_date():
    """Testarea functiei care calculeaza cate zile sunt intre 2 date de forma:  z1/luna1/luna1 - zi2/luna2/an2
    Date de intare: -
    Date de iesire: - """
    assert(diferenta_date(3, 5, 2021, 15, 5, 2021) == 12) 
    assert(diferenta_date(5, 7, 2020, 3, 8, 2020) == 29)
    assert(diferenta_date(1, 1, 2020, 2, 3, 2020) == 61)
    assert (diferenta_date(3, 2, 2021, 5, 3, 2021) == 30)
    
def test2a(dictionar):
    """Testare 2 a)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachet_dest(dictionar,"barcelona") == ["1", "3", "8"])
    assert(cauta_pachet_dest(dictionar,"lisabona") == ["2", "6", "9"])
    assert(cauta_pachet_dest(dictionar,"londra") == ["4", "10"])
    assert(cauta_pachet_dest(dictionar, "haga") == [])

def test2b(dictionar):  
    """Testare 2 a)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachet_durata(dictionar, 10) == ["1", "2", "3", "5", "6", "8", "9", "10"])
    assert(cauta_pachet_durata(dictionar, 7) == ["5", "8", "10"]) 
    assert(cauta_pachet_durata(dictionar, 4) == []) 
    assert(cauta_pachet_durata(dictionar, 20) == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
def test2c(dictionar):
    """Testare 2 c)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachet_pret(dictionar, 2000) == ["1", "3", "4", "6", "7"])
    assert(cauta_pachet_pret(dictionar, 400) == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    assert(cauta_pachet_pret(dictionar, 2300) == ["4"])
    assert(cauta_pachet_pret(dictionar, 4120) == [])
    
def test3a(dictionar):
    """Testare 3 a)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachet_interval(dictionar, 15, 10, 2020, 3, 1, 2021) == ["3", "4"])
    assert(cauta_pachet_interval(dictionar, 1, 7, 2021, 30, 7, 2021) == ["2", "5"])
    assert(cauta_pachet_interval(dictionar, 20, 1, 2021, 30, 12, 2021) == ["1", "2", "5", "7", "8", "9", "10"])
    assert(cauta_pachet_interval(dictionar, 5, 7, 2024, 6, 10, 2025) == [])
    assert(cauta_pachet_interval(dictionar, 10, 6, 2021, 30, 6, 2021) == ["9"])
    
def test3b(dictionar):
    """Testare 3 b)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachet_dest_pret(dictionar, "barcelona", 2150) == ["3", "8"])
    assert(cauta_pachet_dest_pret(dictionar, "barcelona", 3000) == ["1", "3", "8"])
    assert(cauta_pachet_dest_pret(dictionar, "lisabona", 500) == [])
    assert(cauta_pachet_dest_pret(dictionar, "londra", 2150) == ["10"])
    
def test3c (dictionar):
    """Testare 3 c)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_pachete_data(dictionar, 30, 7, 2021) == ["2", "5"])
    assert(cauta_pachete_data(dictionar, 4, 5, 2020) == [])
    assert(cauta_pachete_data(dictionar, 29, 3, 2021) == ["8"])

def test4a(dictionar):
    """Testare 4 a)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(cauta_oferte_dest (dictionar, "barcelona") == 3)
    assert(cauta_oferte_dest (dictionar, "londra") == 2)
    assert(cauta_oferte_dest (dictionar, "budapesta") == 1)
    assert(cauta_oferte_dest (dictionar, "haga") == 0)

def test4b(dictionar):
    """Testare 4 b)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(ordonare_lista_dupa_pret(dictionar, ["3", "4"]) == ["3", "4"])
    assert(ordonare_lista_dupa_pret(dictionar, ["2", "5"]) == ["5", "2"])
    assert(ordonare_lista_dupa_pret(dictionar,["1", "2", "5", "7", "8", "9", "10"]) == ["10", "5", "8", "2", "9", "7", "1"])
    assert(ordonare_lista_dupa_pret(dictionar, ["9"]) == ["9"])
    
def test4c(dictionar):
    """Testare 4 c)
    Date de intare: index(int), dictionar(dict)
    Date de iesire: - """
    assert(calcul_medie_pret(dictionar, "barcelona", 3) == 2033)    
    assert(calcul_medie_pret(dictionar, "londra", 2) == 2025)
    assert(calcul_medie_pret(dictionar, "budapesta", 1) == 2250)
    assert(calcul_medie_pret(dictionar, "lisabona", 3) == 1966)

def test5a(dictionar):    
    """Testare 5 a)
    Date de intare: dictionar(dict)
    Date de iesire: - """
    assert(filtrare_oferte_pret_dest(dictionar, 2150, "barcelona") == ["3", "8"])
    assert(filtrare_oferte_pret_dest(dictionar, 700, "lisabona") == [])
    assert(filtrare_oferte_pret_dest(dictionar, 3000, "barcelona") == ["1", "3", "8"])
    assert(filtrare_oferte_pret_dest(dictionar, 2150, "londra") == ["10"])
    
def test5b(dictionar):
    """Testare 5 b)
    Date de intare: idictionar(dict)
    Date de iesire: - """
    assert(filtrare_oferte_luna(dictionar, "7") == ["1","3", "4", "6", "7", "8", "9", "10"])
    assert(filtrare_oferte_luna(dictionar, "6") == ["1", "2", "3", "4", "5", "6", "7", "8"])
    assert(filtrare_oferte_luna(dictionar, "4") == ["2", "3", "4", "5", "6", "7", "8", "9", "10"])
    assert(filtrare_oferte_luna(dictionar, "10") == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    
def run_all_tests():
    """Efectueaza toate testele
    Date de intare: -
    Date de iesire: - """
    
    dictionar = dict()
    initializare_dictionar(dictionar)
    test2a(dictionar)
    test2b(dictionar)
    test2c(dictionar)
    test_verifica_la_dreapta()
    test_verifica_la_stanga()
    test_diferenta_date()
    test3a(dictionar)
    test3b(dictionar)
    test3c(dictionar)
    test4a(dictionar)
    test4b(dictionar)
    test4c(dictionar)
    test5a(dictionar)
    test5b(dictionar)