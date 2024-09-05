'''
Created on Nov 1, 2020

@author: munte
'''
from teste.init_dict import initializare_dictionar
from ui.console import meniu, ui_adauga_pachet_calatorie, ui_eliminare_oferte_luna, ui_eliminare_oferte_pret_dest, ui_medie_pret, ui_numar_oferte_dest, ui_numar_oferte_dest, ui_pachet_data, ui_pachet_dest_pret, ui_pachet_dest_pret, ui_pachet_interval_dat, ui_pachet_interval_dat, ui_pachet_interval_dat_crescator, ui_sterge_pachet_dest, ui_sterge_pachet_pret, ui_modifica_pachet_calatorie, ui_sterge_pachet_durata, ui_undo
from ui_batch.console2 import meniu_batch

from teste.teste import run_all_tests
if __name__ == '__main__':
    def run():
        meniu()
        dictionar = dict()
        index = 11 
        initializare_dictionar(dictionar)
        lista_undo = []
        while True:
            cmd = input(">>>")
            if cmd == "1":
                index = ui_adauga_pachet_calatorie(index, dictionar, lista_undo)
            elif cmd == "2":
                 ui_modifica_pachet_calatorie(dictionar, lista_undo)
            elif cmd == "3":
                dictionar = ui_sterge_pachet_dest(dictionar, lista_undo)
            elif cmd == "4":
                dictionar = ui_sterge_pachet_durata(dictionar, lista_undo)
                print(dictionar)
            elif cmd == "5":
                dictionar = ui_sterge_pachet_pret(dictionar, lista_undo)
            elif cmd == "6":
                ui_pachet_interval_dat(dictionar) 
            elif cmd == "7":
                ui_pachet_dest_pret(dictionar)  
            elif cmd == "8":    
                ui_pachet_data(dictionar) 
            elif cmd == "9":
                ui_numar_oferte_dest(dictionar)  
            elif cmd == "10":
                ui_pachet_interval_dat_crescator(dictionar)    
            elif cmd == "11":         
                ui_medie_pret(dictionar) 
            elif cmd == "12":
                ui_eliminare_oferte_pret_dest(dictionar)   
            elif cmd == "13":
                ui_eliminare_oferte_luna(dictionar)    
            elif cmd == "14":
                ui_undo(dictionar, lista_undo)
            elif cmd == "15":
                meniu_batch(dictionar, index, lista_undo)  
            else:
                print("Comanda invalida!")
                
run_all_tests()                    
run()                          
    