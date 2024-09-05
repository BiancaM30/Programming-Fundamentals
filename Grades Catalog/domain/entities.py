from itertools import count
class Student:
    def __init__(self, id, nume, grupa):
        """ 
        Create a new student with the given studentID, nume, grupa
        studentID, nume, grupa are Strings 
        """
        self.__studentID = id
        self.__nume = nume
        self.__grupa = grupa
    
    def get_ID(self):    
        return self.__studentID
    
    def get_nume(self):
        return self.__nume
    
    def get_grupa(self):
        return self.__grupa
    
    def set_ID(self, valoare):    
        self.__studentID = valoare
        return self.__studentID
    
    def set_nume(self, valoare):
        self.__nume = valoare
        return self.__nume
     
    def set_grupa(self, valoare):
        self.__grupa = valoare
        return self.__grupa
    
    def __eq__(self, student):
        """
        Verify equality
        student - Student
        return True if the current student equals with student (have the same ID)
        """
        return self.get_ID() == student.get_ID()
    
def testCreateStudent():
    """
    Testing student creation
    Testing get_,set_ methods
    """
    st = Student("3y131281", "Ioana", "213")  
    assert st.get_ID() == "3y131281" 
    assert st.get_nume() == "Ioana"
    assert st.get_grupa() == "213" 
    st.set_grupa("220")
    st.set_nume("Andreea")
    assert st.get_grupa() == "220"
    assert st.get_nume() == "Andreea"
    
def testEqual():
    """
    Test if 2 students are equal(have the same ID)
    """    
    
    st1 = Student("5b123213", "Mihai", "212")
    st2 = Student("5b123213", "Dan", "211")
    assert(st1 == st2)
    
testCreateStudent()
testEqual()    

class Problema:
    def __init__(self, idProblema, descriere, deadline):
        """
        Create a new problem with the given id, descriere, deadline
        id, descriere, deadline are strings
        """
    
        self.__id = idProblema
        self.__descriere = descriere
        self.__deadline = deadline
    
    def get_idProblema(self):
        return self.__id 
    
    def get_descriere(self):
        return self.__descriere
    
    def get_deadline(self):
        return self.__deadline
    
    def set_descriere(self, val):
        self.__descriere = val
        return self.__descriere
    
    def set_deadline(self, val):
        self.__deadline = val
        return self.__deadline
    
    def __eq__(self, pb):
        """
        Verify equality
        pb - Problema
        return True if the current problem equals with pb (have the same ID)
        """
        return self.get_idProblema()== pb.get_idProblema()
    
    
def testCreateProblem():
    """
    Testing problem creation
    Testing get_,set_ methods
    """
    pb = Problema("3_15", "Se citeste un numar pozitiv,intreg,de maxim 5 cifre sa se determine cate cifre are numarul", "5.12.2020")   
    assert pb.get_idProblema() == "3_15"
    assert pb.get_descriere() == "Se citeste un numar pozitiv,intreg,de maxim 5 cifre sa se determine cate cifre are numarul"
    assert pb.get_deadline() == "5.12.2020"
    pb.set_deadline("5.1.2021")
    pb.set_descriere("Aflati minimul dintre a si b")
    assert pb.get_deadline() == "5.1.2021"
    assert pb.get_descriere() == "Aflati minimul dintre a si b"
    
def testEqualProbleme():
    """
    Test if 2 problems are equal(have the same ID)
    """    
    pb1 = Problema("2_12", "Verificati daca a si b sunt prime intre ele", "4.12.2020")
    pb2 = Problema("2_12", "Verificati daca a este mai mare decat b", "5.12.2020")
    assert pb1 == pb2
    
testCreateProblem()     
testEqualProbleme()

class Laborator:
    
    def __init__(self, st, pb, nota):
        """
        Create a new lab with the given student, problema
        st - is an Student() object
        pb - is a Problema() object
        """
        self.__student = st
        self.__problema = pb
        self.__nota = nota
        self.__ids = count(1)
        
    def __post_init__(self):
        self.__lab_id = next(self._ids)
    
    def id(self):
        return self.__lab_id
    
    def get_student(self):
        return self.__student
    
    def get_problema(self):
        return self.__problema 
    
    def get_nota(self):
        return self.__nota
    
    def get_studentId(self):
        return self.__student.get_ID()
    
    def get_studentNume(self):
        return self.__student.get_nume()
    
    def get_problemId(self):
        return self.__problema.get_idProblema()
     
    def set_nota(self, val):
        self.__nota = val
        return self.__nota
     
def testCreateLab():
    st1 = Student("4", "ioana", "212")
    st2 = Student("5", "alex", "210")
    pb = Problema("3-20", "Aflati minimul dintre a si b", "3.12.2020")
    lab = Laborator(st1, pb, "10")
    assert lab.get_student() == st1
    assert lab.get_problema() == pb
    assert lab.get_nota()== "10"
    
testCreateLab()     