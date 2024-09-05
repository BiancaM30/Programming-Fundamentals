from domain.entities import Student, Problema, Laborator
from domain.validators import StudentValidator, ValidatorException, ProblemValidator
from Repository.inmemory import StudentsRepo, RepoException, ProblemsRepo, LabsRepo
from service.srv import StudentService, ProblemService, LabService
from utils.utils import get_random_string, get_random_alphanumeric,get_random_problemId, get_radom_date, get_random_grupa, ordonare, apartineInterval
from builtins import int

class Console:
    def __init__(self, srv_s, srv_p, srv_l):
        self.__srv_students = srv_s
        self.__srv_problems = srv_p
        self.__srv_labs = srv_l
        
    def __showAllStudents(self):
        """
        Print all students
        """ 
    
        lista = self.__srv_students.getAllStudents()
        if len(lista) == 0:
            print("Nu exista studenti in catalog")
        else:
            for el in lista:
                print("Id: ", el.get_ID())
                print("Nume: ", el.get_nume()) 
                print("Grupa", el.get_grupa()) 
                print()
    
    def __showAllProblems(self):
        """
        Print all problems
        """            
        lista = self.__srv_problems.getAllProblems()
        if len(lista) == 0:
            print("Lista de probleme este goala")
        else:
            for el in lista:
                print("Id problema: ", el.get_idProblema())
                print("Descriere problema: ", el.get_descriere())
                print("Deadline: ", el.get_deadline())
                print() 
    
    def __showAllLabs(self):
        """
        print all labs
        """    
        lista = self.__srv_labs.getAllLabs()
        if len(lista) == 0:
            print("Lista de laboratoare este goala")
        else:
            for el in lista:
                print("Id-ul studentului: ", el.get_studentId())
                print("Id-ul problemei: ", el.get_problemId())
                print("Nota este: ", el.get_nota())
                print() 
                
    def __addStudent(self):
        """
        Add new student from console
        """         
        id = input("Introduceti ID-ul: ")
        nume = input("Introduceti numele: ")
        grupa = input("Introduceti grupa: ")
        
        try:
            st = self.__srv_students.createStudent(id, nume, grupa)
            print("Student adaugat cu succes!")
            
        except RepoException:
            print("Id deja existent!") 
            
        except ValidatorException as ex:
            print(ex.getErrors())       
     
    def __addProblem(self):
        """
        Add new problem from console
        """    
        id_pb = input("Introduceti id-ul problemei(numar laborator_numar problema): ")
        descriere = input("Introduceti descrierea problemei: ")
        deadline = input("Introduceti deadline-ul problemei(zi.luna.an): ")
        
        try:
            self.__srv_problems.createProblem(id_pb, descriere, deadline)
            print("Problema adaugata cu succes!")
            
        except ValidatorException as ex:
            print(ex.getErrors())
   
    def __delStudent(self):
        """
        Read an Id from console
        Delete the student with the same Id 
        """            
        id = input("Introduceti Id-ul studentului pe care doriti sa il stergeti: ")
        try:
            self.__srv_labs.removeLabByStudent(id)
            self.__srv_students.del_student_id(id)
            print("Student sters!")
            print("S-au sters si laboratoarele asignate studentului, daca existau")
            
        except KeyError:
            print("Id-ul introdus nu a fost gasit")
                
    def __delProblem(self):
        """
        Read a problem Id from console
        Delete the problem with the same Id
        """    
        id_problema = input("Introduceti Id-ul problemei pe care doriti sa o stergeti (in formatul: <numar laborator_numar problema):")
        try:
            self.__srv_labs.removeLabByProblem(id_problema)
            self.__srv_problems.del_problem_id(id_problema)
            print("Problema stearsa!")
            print("S-au sters si laboratoarele asignate studentilor, ce contineau problema respectiva")
        except KeyError:
            print("Id-ul introdus nu a fost gasit")   
    
    def __modificaStudent(self):
        """
        Read the change that user want to apply
        Modify the student
        """     
        id = input("Introduceti id-ul studentului pe care doriti sa il modificati:")
        sir = input("Introduceti ce anume doriti sa modificati(id/nume/grupa):" )
        val = input("Introduceti noua valoare: ")
        
        if id == ""  or val == "":
            print("Comanda invalida!")
            
        elif (sir != "nume" and sir!= "grupa"):
            print("Comanda invalida!")
            
        else:        
            try:
                self.__srv_students.update_student(id, sir, val)
                print("Valoare modificata!")
            except KeyError:
                print("Id-ul introdus nu a fost gasit")
    
    def __modificaProblema(self):
        """
        Read the change that user want to apply
        Modify the problem
        """     
        id = input("Introduceti id-ul problemei pe care doriti sa o modificati:")
        sir = input("Introduceti ce anume doriti sa modificati(descriere/deadline):" )
        val = input("Introduceti noua valoare: ")
        
        if id == ""  or val == "":
            print("Comanda invalida!")
            
        elif (sir != "descriere" and sir!= "deadline"):
            print("Comanda invalida!")
            
        else:        
            try:
                self.__srv_problems.update_problem(id, sir, val)
                print("Valoare modificata!")
            except KeyError:
                print("Id-ul introdus nu a fost gasit")        
    
    def __cautaStudent(self):
        """Read the id of a student
        Search the student with the same id and print it
        """     
        id = input("Introduceti id-ul studentului pe care doriti sa il cautati: ")
        
        if id == "":
            print("Comanda invalida!")
        else:
            try:
                st = self.__srv_students.search_student(id)
                print("Id: ", st.get_ID())
                print("Nume: ", st.get_nume()) 
                print("Grupa", st.get_grupa()) 
                print()
    
            except KeyError:
                print("Id-ul introdus nu a fost gasit")   
    
    def __cautaProblema(self):
        """Read the id of a problem
        Search the problem with the same id and print it
        """     
        id = input("Introduceti id-ul problemei pe care doriti sa o cautati: ")
        
        if id == "":
            print("Comanda invalida!")
        else:
            try:
                pb = self.__srv_problems.search_problem(id)
                print("Id problema: ", pb.get_idProblema())
                print("Descriere problema: ", pb.get_descriere())
                print("Deadline: ", pb.get_deadline())
                print() 
    
            except KeyError:
                print("Id-ul introdus nu a fost gasit")  
    
    def __asignareLaborator(self):
        """
        Read a student id and a problem id
        create a lab assigning a problem to the student, without a grade
        """ 
        id_st = input("Introduceti id-ul studentului: ")
        id_pb = input("Introduceti id-ul problemei pe care doriti sa o asignati: ")  
        
        if id_st == "" or id_pb == 0:
            print("Comanda invalida!")
        else:    
            try:
                st = self.__srv_students.search_student(id_st)
                pb = self.__srv_problems.search_problem(id_pb)
                self.__srv_labs.createLab(st, pb, 0)
                print("Laborator asignat!")
                
            except ValidatorException as ex:
                print(ex.getErrors())  
            
            except KeyError:
                print("Id-ul introdus nu a fost gasit")    
  
    def __notareLaborator(self):
        """
        Read a student id, a problem id and a grade
        assign a grade to the specified lab
        """ 
        id_st = input("Introduceti id-ul studentului: ")
        id_pb = input("Introduceti id-ul problemei pe care doriti sa o notati: ")
        
        if id_st == "" or id_pb == "" :
            print("Comanda invalida!") 
        
        else:    
            try:
                nota = float(input("Introduceti nota: "))
                if nota < 1 or nota >10:
                    raise ValueError
                try:
                    self.__srv_labs.notare(id_st, id_pb, nota)
                    print("Laborator notat!") 
                except ValidatorException as ex:
                    print(ex.getErrors())      
                except Exception:
                        print("Id-urile introduse nu a fost gasite in lista de laboratoare. Trebuie sa asignati laboratorul pentru a-l putea nota") 
                        
            except ValueError:
                print("Introduceti un numar real cuprins intre 1 si 10!")               
                  
    
    def __generareStudentiRandom(self):
        try:
            nr = int(input("Introduceti numarul studentilor pe care doriti sa ii generati: ")) 
            for i in range(nr):
                id = get_random_alphanumeric(3)
                nume = get_random_string(8)
                grupa = get_random_grupa() 
                try:        
                    st = self.__srv_students.createStudent(id, nume, grupa)
                except RepoException:
                    print("Id deja existent!") 
                except ValidatorException as ex:
                    print(ex.getErrors()) 
            print("S-au introdus ", nr, " studenti")         
        except ValueError:
            print("Introduceti un numar intreg!")              
    
    def __generareProblemeRandom(self):
        try:
            nr = int(input("Introduceti numarul problemelor pe care doriti sa le generati: ")) 
            for i in range(nr):
                id = get_random_problemId()
                descriere = get_random_string(50)
                deadline = get_radom_date()
                try:        
                    pb = self.__srv_problems.createProblem(id, descriere, deadline)
                except RepoException:
                    print("Id deja existent!") 
                except ValidatorException as ex:
                    print(ex.getErrors()) 
            print("S-au introdus ", nr, " probleme")         
        except ValueError:
            print("Introduceti un numar intreg!")  
    
    def __ordonareLabAlfabetic(self):
        """
        Read a problem id
        Print the list of students sorted ascending by name and descending by grade
        """
        id_pb = input("Introduceti id-ul problemei pentru care se va afisa lista de studenti ordonata alfabetic dupa nume si descrescator dupa nota: ")  
        lista = self.__srv_labs.creareListaStatistica(id_pb)
        if lista == []:
            print("Nu s-au gasit studenti care sa fi rezolvat problema introdusa")
        else: 
            lista = ordonare(lista)
            for el in lista:
                print("Id:", el[0]," Nume:", el[1], " Nota:", el[2])
                
    def __mediaNoteLabSub5(self):
        """
        Print the list of students with the average grade lower than 5
        """
        lista_ids = self.__srv_labs.listaIdStudents()
        lista = self.__srv_labs.creareListaMedii(lista_ids)
        for el in lista:
            if apartineInterval(0, 5, el[2]):
                print("Id:", el[0], " Nume:", el[1], " Media:", "% 1.2f" % el[2])
                gasit = 1
        if gasit == 0:
                print("Nu sunt studenti cu media notelor de laborator mai mica decat 5")        
    
    def __mediaNoteLabInterval(self):  
        """
        Print the list of students with the average grade between 2 input values [x,y]
        """
        x = input("Introduceti capatul inferior al intervalului:")
        y = input("Introduceti capatul superior al intervalului:")
        try:
            x = int(x)
            y = int(y)
            if x < 0 or y > 10:
                raise Exception
            else:
                lista_ids = self.__srv_labs.listaIdStudents()
                lista = self.__srv_labs.creareListaMedii(lista_ids)
                gasit = 0
                for el in lista:
                    if apartineInterval(x, y, el[2]):
                        print("Id:", el[0], " Nume:", el[1], " Media:", "% 1.2f" % el[2])
                        gasit = 1
                if gasit == 0:       
                    print("Nu sunt studenti cu media notelor de laborator in intervalul introdus.") 
        except Exception:
            print("Capetele intervalui trebuie sa fie numere intregi, cuprinse intre 0 si 10!")      
                        
    def __menu(self):   
        print("1.Afisare studenti") 
        print("2.Afisare probleme")
        print("3.Adauga student")
        print("4.Adauga problema")
        print("5.Sterge student")
        print("6.Sterge problema")
        print("7.Modifica student")
        print("8.Modifica problema")
        print("9.Cauta student")
        print("10.Cauta problema")
        print("11.Afisare laboratoare")
        print("12.Asignare laborator")
        print("13.Notare laborator")
        print("14.Generare n studenti aleatoriu")
        print("15.Generare n probleme aleatoriu")
        print("16.Afisare lista de studenti si notele lor la o problema de laborator data, ordonata: alfabetic dupa nume, descrescator dupa nota.")
        print("17.Afisare studenti cu media tuturor notelor de laborator mai mica decat 5")
        print("18.Afisare studenti cu media tuturor notelor de laborator intr-un interval dat")
        
    def __initializareEntitatiTest(self):
        """
        Initialize with some data for testing 
        """
        st1 = self.__srv_students.createStudent("7", "ana", "213")
        st2 = self.__srv_students.createStudent("14", "tudor", "212")
        st3 = self.__srv_students.createStudent("5", "alexandra", "215")
        st4 = self.__srv_students.createStudent("2", "ana", "215")
        st5 = self.__srv_students.createStudent("20", "bogdan", "213")
        
        pb1 = self.__srv_problems.createProblem("5-21", "aaa", "3.12.2020")
        pb2 = self.__srv_problems.createProblem("7-19", "bbb", "13.1.2020")
        pb3 = self.__srv_problems.createProblem("9-15", "ccc", "15.2.2021")    
        pb4 = self.__srv_problems.createProblem("3-11","ddd","3.10.2020")
        
        self.__srv_labs.createLab(st1, pb1, 7.5)
        self.__srv_labs.createLab(st1, pb2, 2)
        self.__srv_labs.createLab(st1, pb4, 2)
        
        self.__srv_labs.createLab(st2, pb2, 8.5)
        self.__srv_labs.createLab(st2, pb3, 10)
        self.__srv_labs.createLab(st2, pb4, 4)
        
        self.__srv_labs.createLab(st3, pb1, 7)
        self.__srv_labs.createLab(st3, pb2, 5)
        self.__srv_labs.createLab(st3, pb3, 2)
        
        self.__srv_labs.createLab(st4, pb1, 9)
        self.__srv_labs.createLab(st4, pb4, 2)
        
        self.__srv_labs.createLab(st5, pb3, 10)
        
        
    def showUI(self):
        self.__menu()
        self.__initializareEntitatiTest()
        while True:
            cmd = input(">>>")
            if cmd == "1":
                self.__showAllStudents()  
            if cmd == "2": 
                self.__showAllProblems()       
            if cmd == "3":
                self.__addStudent()   
            if cmd == "4":
                self.__addProblem()    
            if cmd == "5":
                self.__delStudent()   
            if cmd == "6":
                self.__delProblem()     
            if cmd == "7":
                self.__modificaStudent() 
            if cmd == "8":
                self.__modificaProblema()      
            if cmd == "9":
                self.__cautaStudent() 
            if cmd == "10":
                self.__cautaProblema() 
            if cmd == "11":
                self.__showAllLabs()      
            if cmd == "12":
                self.__asignareLaborator() 
            if cmd == "13":
                self.__notareLaborator() 
            if cmd == "14":
                self.__generareStudentiRandom()
            if cmd == "15":
                self.__generareProblemeRandom() 
            if cmd == "16":
                self.__ordonareLabAlfabetic()     
            if cmd == "17":
                self.__mediaNoteLabSub5() 
            if cmd == "18":
                self.__mediaNoteLabInterval()                              