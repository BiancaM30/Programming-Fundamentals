from domain.entities import Student, Problema, Laborator
from Tools.scripts.fixcid import rep

class RepoException(Exception):
    
    def __init__(self, errors):
        self.errors = errors
        
    def getErrors(self):
        return self.errors
        
class StudentsRepo:
    def __init__(self):
        self.__students = {}
    
    def store(self, st):    
        """
        Store __students
        st = Student
        raise exception if we have a student with the same id
        """
        errors = []
        if st.get_ID() in self.__students: 
            errors.append("ID existent!")
            raise RepoException(errors)
        self.__students[st.get_ID()] = st
    
    def size(self):
        """ 
        The number of __students in the repository
        return an integer
        """
        return len(self.__students) 
    
    def getAllStudents(self):   
        """
        Return the list of __students in repository
        """
        return list(self.__students.values())
    
    def removeStudent(self, id):
        """
        Remove a student from repository
        id as a string
        """
        del self.__students[id]
    
    def updateStudentNume(self, id, val):
        """
        Update a student name in repository
        id, val as strings
        """    
        self.__students[id].set_nume(val)
    
    def updateStudentGrupa(self, id, val):
        """
        Update a student group in repository
        id, val as strings
        """    
        self.__students[id].set_grupa(val) 
          
    def getStudentById(self, id):
        """
        Get a student by id
        id as a string
        """ 
        return self.__students[id] 
           
def testStoreStudents():
    rep = StudentsRepo()
    assert (rep.size() == 0) 
    
    st = Student("5x232132", "Maria", "211")   
    rep.store(st)
    assert(rep.size() == 1)
    
    st = Student("3r216289", "Ion", "212")
    rep.store(st)
    assert(rep.size()== 2)
    
    st = Student("3r216289", "Ana", "213")
    try:
        rep.store(st)
        assert False
    except RepoException as ex:
        assert  len(ex.getErrors()) == 1
        
def testRemoveStudent():
    rep = StudentsRepo()
    st = Student("2", "ioana", "230")
    rep.store(st)
    
    st = Student("3", "bogdan", "215")  
    rep.store(st) 
    rep.removeStudent("2")
    assert (rep.size() == 1)
   
def testUpdateStudent():
    rep = StudentsRepo()
    st1 = Student("2", "ioana", "230") 
    rep.store(st1)
  
    st2 = Student("3", "bogdan", "215") 
    rep.store(st2)
    
    rep.updateStudentNume("2", "alexandra")
    rep.updateStudentGrupa("3", "220")
    assert st1.get_nume() == "alexandra"
    assert st2.get_grupa() == "220"

def testGetStudentById():
    rep = StudentsRepo()

    st1 = Student("5x232132", "Maria", "211")   
    rep.store(st1)
    
    st2 = Student("3r216289", "Ion", "212")
    rep.store(st2)
    
    st3 = rep.getStudentById("5x232132")
    assert st3 == st1
    
    try:
        st3= rep.getStudentById("13r4dcadc")
        assert False
    except KeyError:
        assert True   
        
testStoreStudents()        
testRemoveStudent()
testUpdateStudent()
testGetStudentById()

class ProblemsRepo:
    def __init__(self):
        self.__problems = {}
        
    def store(self, pb):    
        """
        Store problems
        pb - Problem
        raise exception if we have a problem with the same id
        """
        errors = []
        if pb.get_idProblema() in self.__problems:
            errors.append("Id problema existent!")
            raise RepoException(errors)
        
        self.__problems[pb.get_idProblema()] = pb
        
    def size(self):
        """
        The number of __problems in the repository
        return an integer
        """
        return len(self.__problems)    
    
    def getAllProblems(self):
        """
        Return the list of __problems from the repository
        """
        return list(self.__problems.values())
    
    def removeProblem(self, id):
        """
        Remove a problem from repository
        id as a string
        """
        del self.__problems[id]
    
    def updateProblemDescriere(self, id, val):
        """
        Update a problem description in repository
        id, val as strings
        """    
        self.__problems[id].set_descriere(val)
        
    def updateProblemDeadline(self, id, val):
        """
        Update a problem deadline in repository
        id, val as strings
        """    
        self.__problems[id].set_deadline(val)
        
    def getProblemById(self, id):
        """
        Get a problem by id
        id as a string
        """ 
        return self.__problems[id]     
          
def testStoreProblems():
    repo = ProblemsRepo()
    
    pb = Problema("2-14", "Se citesc 4 intregi numere sa se determine daca exista printre ele 3 numere pozitive.", "12.12.2020")
    repo.store(pb)
    assert (repo.size() == 1)
    
    pb = Problema("3-15", "Sa se determine cmmmdc dintre a si b", "13.3.2021")
    repo.store(pb)
    assert (repo.size() == 2)
    
    pb = Problema("2-14", "Aflati lungimea sirului S", "15.2.2021")
    try:
        repo.store(pb)
        assert False
    except RepoException as ex:
        assert  len(ex.getErrors()) == 1
 
def testRemoveProblem():
    rep = ProblemsRepo()
    pb = Problema("2-27", "Sa se determine cmmmdc dintre a si b", "3.12.2020")
    rep.store(pb)
    
    pb = Problema("3-20", "Aflati lungimea sirului S", "5.12.2020")
    rep.store(pb)
    
    rep.removeProblem("2-27")
    assert (rep.size() == 1)
   
def testUpdateProblem():
    rep = ProblemsRepo()
    pb1 = Problema("2-27", "Sa se determine cmmmdc dintre a si b", "3.12.2020")
    rep.store(pb1)
    
    pb2 = Problema("3-20", "Aflati lungimea sirului S", "5.12.2020")
    rep.store(pb2)
    
    rep.updateProblemDescriere("2-27", "Aflati al treilea termen al sirului")
    rep.updateProblemDeadline("3-20", "5.4.2021")
    assert pb1.get_descriere() == "Aflati al treilea termen al sirului"    
    assert pb2.get_deadline() == "5.4.2021"

def testGetProblemById():
    rep = ProblemsRepo()
    pb1 = Problema("2-27", "Sa se determine cmmmdc dintre a si b", "3.12.2020")
    rep.store(pb1)
    
    pb2 = Problema("3-20", "Aflati lungimea sirului S", "5.12.2020")
    rep.store(pb2)  
      
    pb3 = rep.getProblemById("3-20")
    assert pb2 == pb3
    
    try:
        pb3 = rep.getProblemById("3-21")
        assert False
    except KeyError:
        assert True   
         
testStoreProblems()    
testRemoveProblem()
testUpdateProblem()
testGetProblemById()

class LabsRepo:
    def __init__(self):
        self.__labs = {}
        
    def store(self, lab):    
        """
        Store labs
        lab = Laborator()
        """
        
        self.__labs[lab.id] = lab
          
    def size(self):
        """
        The number of __labs in the repository
        return an integer
        """
        return len(self.__labs)
    
    def getAllLabs(self):   
        """
        Return the list of __labs in repository
        """
        return list(self.__labs.values())
    
    def updateNota(self, lab, nota):
        """
        Update nota in repository
        lab as Laborator()
        nota as float
        """
        
        lab.set_nota(nota)
        return self.__labs
    
    def removeLab(self, lab):
        """
        Remove a lab from repository
        
        """
       
        del self.__labs[lab.id]
    
             
def testStoreLabs(): 
    repo = LabsRepo()  
    
    st = Student("5", "andreea", "212")
    pb = Problema("2-14", "Aflati lungimea siului S", "13.2.2021")
    lab = Laborator(st, pb, "9")
    repo.store(lab)
    assert repo.size() == 1

testStoreLabs()    
    
    