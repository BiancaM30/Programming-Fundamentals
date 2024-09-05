from domain.entities import Student, testCreateStudent ,Problema, Laborator
from domain.validators import StudentValidator, ProblemValidator, ValidatorException,\
    LabValidator
from Repository.inmemory import StudentsRepo, RepoException, ProblemsRepo, LabsRepo,\
    testGetStudentById

class StudentService():
    def __init__(self, rep, validator):
        """
        Initialize service
        rep - StudentsRepo- object to store students
        validator - StudentValidator - object to validate students
        """
        self.__rep = rep
        self.__validator = validator
        
    def createStudent(self, id, nume, grupa):
        """
        Create a student 
        id, nume, grupa of the student as a string
        return Student
        Post: student added to the repository
        raise RepoException - if student id already exists
        raise StudentValidatorException- if student fields are invalid
        """
        st = Student(id, nume, grupa)    
        self.__validator.validate(st)
        self.__rep.store(st)
        return st
    
    def getAllStudents(self):
        """
        return list of all students in the system
        """
        return self.__rep.getAllStudents()
    
    def del_student_id(self, id):
        """
        Delete the student with the given id
        id as a string
        Post: student removed from repository
        """
        self.__rep.removeStudent(id)
        
    def update_student(self, id, sir, val):
        """
        Update student field "sir" with "val"
        id, sir, val as strings
        Post: student updated in repository
        """             
        if sir == "nume":
            self.__rep.updateStudentNume(id, val)
            
        elif sir == "grupa": 
            self.__rep.updateStudentGrupa(id, val)
    
    def search_student(self, id):
        """
        Search the student with the given id
        id as string
        """    
        return self.__rep.getStudentById(id)
    
def testCreateStudent():       
    rep = StudentsRepo()
    validator = StudentValidator()
    srv = StudentService(rep, validator) 
    
    st = srv.createStudent("4y214246", "Andra", "213")
    assert (st.get_ID() == "4y214246")
    assert (st.get_nume() == "Andra")
    st = srv.createStudent("3y230135", "Bianca", "215")
    assert (st.get_grupa() == "215")
    all_students = srv.getAllStudents()
    assert(len(all_students) == 2)
    
    try:
        srv.createStudent("4y214246", "Alex", "212")
        assert False
    except RepoException as ex:
        assert (len(ex.getErrors()) == 1)
            
testCreateStudent()    

class ProblemService():
    def __init__(self, rep, validator):
        """
        Initialize service
        rep - repository - object to store problems
        validator - validator - object to validate problems
        """
        self.__rep = rep
        self.__validator = validator
        
    def createProblem(self, id_problema, descriere, deadline): 
        """
        Create a problem
        id_problema, descriere, deadline of the problem  as strings
        Post: problem added to the repository
        raise ProblemValidator exception if problem fields are invalid
        """
        pb = Problema(id_problema, descriere, deadline)
        self.__validator.validate(pb)
        self.__rep.store(pb)   
        return pb
    
    def getAllProblems(self):
        """
        Return list of all the problems in the system
        """
        return self.__rep.getAllProblems()
    
    def del_problem_id(self, id):
        """
        Delete the problem with the given id
        id as a string
        Post: problem removed from repository
        """
        self.__rep.removeProblem(id)
    
    def update_problem(self, id, sir, val):
        """
        Update problem field "sir" with "val"
        id, sir, val as strings
        Post: problem updated in repository
        """             
        if sir == "descriere":
            self.__rep.updateProblemDescriere(id, val)
           
        elif sir == "deadline": 
            self.__rep.updateProblemDeadline(id, val)
    
    def search_problem(self, id):
        """
        Search the problem with the given id
        id as string
        """    
        return self.__rep.getProblemById(id)  
           
def testCreateProblem():
    repo = ProblemsRepo()
    validator = ProblemValidator()
    srv = ProblemService(repo, validator)
    
    pb = srv.createProblem("3-23", "Determinati numerele prime din sir", "14.1.2021")
    assert pb.get_idProblema() == "3-23"
    assert pb.get_descriere() == "Determinati numerele prime din sir"
    assert pb.get_deadline() == "14.1.2021"
    
    try:
        srv.createProblem("", "", "13.12.2020")
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 2
        
testCreateProblem()    
   
class LabService:
    def __init__(self, rep, validator):
        """
        Initialize service
        rep - repository - object to store problems
        """
        self.__rep = rep
        self.__validator = validator
        
    def createLab(self, st, pb, nota):     
        """
        Create a lab
        st - Student()
        pb - Problema()
        Post: lab added to the repository
        """
        
        
        lab = Laborator(st, pb, nota)
        self.__validator.validate(lab)
        self.__rep.store(lab)
        return lab 
      
    def getAllLabs(self):
        """
        return list of all labs in the system
        """
        return self.__rep.getAllLabs()
    
    def notare(self, id_st, id_pb, nota):
        """
        Search for the lab with the given student id and problem id
        id_st, id_pb as strings
        nota as float
        post: Nota updated in repo
        """    
        
        lista = self.__rep.getAllLabs()
        gasit = 0
        for el in lista:
            if el.get_studentId() == id_st and el.get_problemId() == id_pb:
                self.__rep.updateNota(el, nota)
                return el
                gasit = 1
                
        if gasit == 0:
            raise Exception
    
    def removeLabByStudent(self, id_st):
        """
        Search for the labs with the given student id 
        id_st as str
        post: remove labs from repository
        """
        lista = self.__rep.getAllLabs()
        for el in lista:
            if el.get_studentId() == id_st:
                self.__rep.removeLab(el)
        return self.__rep  
    
    def removeLabByProblem(self, id_pb):
        """
        Search for the labs with the given student id 
        id_pb as str
        post: remove labs from repository
        """
        lista = self.__rep.getAllLabs()
        for el in lista:
            if el.get_problemId() == id_pb:
                self.__rep.removeLab(el)
        return self.__rep      
    
    def creareListaStatistica(self, id_pb):
        """
        Search for the labs with the given problem id, and store that student id, name 
        and nota in a list
        id_pb as a string
        return lista_statistica as a list
        """
        lista = self.__rep.getAllLabs()
        lista_statistica = []
        for el in lista:
            if el.get_problemId()== id_pb:
                lista_statistica.append([el.get_studentId(), el.get_studentNume(), el.get_nota()])       
        return lista_statistica
    
    
    def listaIdStudents(self):
        """
        Search for the students ids in labs
        return lista_ids as a list
        """
        lista = self.__rep.getAllLabs()
        lista_ids=[]
        for el in lista:
            if el.get_studentId() not in lista_ids:
                lista_ids.append(el.get_studentId())
                
        return lista_ids   
                
    def creareListaMedii(self, lista_ids):     
        """
        We have to iterate through the 'lista_ids' to get the grades of a student from all labs
        and compute his average grade. 
        Search for the students with average grade lower than 5
        lista_ids as a list
        return lista_statistica as a list of lists (containing student id, name and average grade)
        """ 
        lista = self.__rep.getAllLabs()     
        lista_statistica = []        
        
        for i in lista_ids:
            nr_elem = 0 #va retine numarul de note a studentului curent
            sum = 0 #va retine suma notelor studentului curent
            for j in lista:
                if j.get_studentId() == i:
                        sum = sum + j.get_nota()
                        nr_elem = nr_elem + 1
                        nume = j.get_studentNume()
            media = sum/nr_elem     
            lista_statistica.append([i, nume, media])  
                
        return lista_statistica   
    
              
      
def testCreateLab():
    repo = LabsRepo()
    validator = LabValidator()
    srv = LabService(repo, validator)
    
    st = Student("5", "andreea", "212")
    pb = Problema("2-14", "Aflati lungimea siului S", "13.2.2021")
    lab = srv.createLab(st, pb, 8.5)
    
    assert lab.get_student() == st
    assert lab.get_problema() == pb
    assert lab.get_nota() == 8.5
    try:
        st = Student("5", "", "")
        pb = Problema("", "Aflati lungimea siului S", "13.2.2021")
        srv.createLab(st, pb,7)
        assert False
        
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 2
        
def testNotare():
    repo = LabsRepo()
    validator = LabValidator()
    srv = LabService(repo, validator)
    
    st = Student("5", "andreea", "212")
    pb = Problema("2-14", "Aflati lungimea siului S", "13.2.2021")
    lab = srv.createLab(st, pb, "Momentan laboratorul nu a fost notat!")
    
    lab = srv.notare("5", "2-14", "9.5")      
    assert lab.get_nota() == "9.5"

def testremoveLabs():
    repo = LabsRepo()
    validator = LabValidator()
    srv = LabService(repo, validator)
    
    st1 = Student("5", "andreea", "212")
    st2 = Student("6", "ana", "210")
    st3 = Student("7", "bogdan", "211")
    st4 = Student("8", "mara", "210")
    pb1 = Problema("2-15", "Aflati lungimea siului S1", "13.2.2021")
    pb2 = Problema("3-14", "Aflati lungimea siului S2", "18.2.2021")
    pb3 = Problema("2-20", "Aflati lungimea siului S3", "19.2.2021")
    lab1 = srv.createLab(st1, pb2, "Momentan laboratorul nu a fost notat!")
    lab2 = srv.createLab(st3, pb1, "Momentan laboratorul nu a fost notat!")  
    lab3 = srv.createLab(st3, pb2, "Momentan laboratorul nu a fost notat!")     
    lab4 = srv.createLab(st4, pb2, "Momentan laboratorul nu a fost notat!")
    
    repo = srv.removeLabByStudent("7")
    assert repo.size() == 2
    
    repo = srv.removeLabByProblem("3-14")
    assert repo.size() == 0

def testCreareListaStatistica():  
    repo = LabsRepo()
    validator = LabValidator()
    srv = LabService(repo, validator)
     
    st1 = Student("7", "ana", "213")
    st2 = Student("14", "tudor", "212")
    st3 = Student("5", "alexandra", "215")
        
    pb1 = Problema("5-21", "aaa", "3.12.2020")
    pb2 = Problema("7-19", "bbb", "13.1.2020")
    
    lab1 = srv.createLab(st1, pb1, 7)
    lab2 = srv.createLab(st2, pb1, 8.5)
    lab3 = srv.createLab(st3, pb2, 9)
    
    lista = srv.creareListaStatistica("5-21")
    assert lista == [["7", "ana", 7], ["14", "tudor", 8.5]]
    
    lista = srv.creareListaStatistica("7-30")
    assert lista == []
    
def testCreareListaMedii(): 
    repo = LabsRepo()
    validator = LabValidator()
    srv = LabService(repo, validator)
     
    st1 = Student("7", "ana", "213")
    st2 = Student("14", "tudor", "212")
    st3 = Student("5", "alexandra", "215")
        
    pb1 = Problema("5-21", "aaa", "3.12.2020")
    pb2 = Problema("7-19", "bbb", "13.1.2020")
    
    lab1 = srv.createLab(st1, pb1, 6)
    lab2 = srv.createLab(st1, pb2, 2)
    lab3 = srv.createLab(st2, pb1, 8)
    lab4 = srv.createLab(st2, pb2, 5)  
    lab5 = srv.createLab(st3, pb1, 5)
    lab6 = srv.createLab(st3, pb2, 4)
    
    lista_ids = srv.listaIdStudents()
    lista = srv.creareListaMedii(lista_ids)
    assert lista == [["7", "ana", 4], ["14", "tudor", 6.5], ["5", "alexandra", 4.5]]
    

    
testCreateLab() 
testNotare() 
testremoveLabs()
testCreareListaStatistica()
testCreareListaMedii()
