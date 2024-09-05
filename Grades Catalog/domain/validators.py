from domain.entities import Student, Problema, Laborator

class ValidatorException(Exception):
    
    def __init__(self, errors):
        self.errors = errors
        
    def getErrors(self):
        return self.errors
        
class StudentValidator:
    """
    Throw ValidatorException if fields are empty
    """
   
    def validate(self, st):
        
        errors = []
        if st.get_ID() == "":
            errors.append("ID-ul nu poate fi gol")
        if st.get_nume() == "":
            errors.append("Numele nu poate fi gol")
        if st.get_grupa() == "":
            errors.append("Grupa nu poate fi goala")   
        if len(errors)>0:
            raise ValidatorException(errors)   
        
def testStudentValidator():     
    validator = StudentValidator()
    st = Student("", "", "")
    try:
        validator.validate(st)
        assert False
    except ValidatorException as ex:   
        assert len(ex.getErrors()) == 3
    
    st = Student("", "", "210")
    try:
        validator.validate(st)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 2
    st = Student("4y121923", "Dana", "212")
    try:
        validator.validate(st)
        assert True
    except ValidatorException as ex:
        assert False            
            
testStudentValidator()   

 
class ProblemValidator:
    """
    Throw ValidatorException if fields are empty
    """      
    
    def validate(self, pb):
        errors = []
          
        if pb.get_idProblema() == "":
            errors.append("Id-ul problemei nu poate fi gol")    
                  
        if pb.get_descriere() == "":
            errors.append("Descrierea nu poate fi goala")
            
        if pb.get_deadline() == "":
            errors.append("Deadline-ul nu poate fi gol") 
            
        if(len(errors) > 0):
            raise ValidatorException(errors)     

def testProblemaValidator():
    validator = ProblemValidator()
    pb = Problema("3-25", "", "")
    try:
        validator.validate(pb)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 2
        
    pb = Problema("", "", "")
    try:
        validator.validate(pb)  
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 3   
    
    pb = Problema("5-11", "Se citesc 3 numere. Sa se determine care este maximul", "20.12.2020")
    try:
        validator.validate(pb)
        assert True
    except ValidatorException as ex:
        assert False        
testProblemaValidator()      
          
class LabValidator():  
    """
    Throw ValidatorException if fields are empty
    """      
    
    def validate(self, lab):
        errors = []
        validator_st = StudentValidator()
        validator_pb = ProblemValidator()
        
        try:
            validator_st.validate(lab.get_student())
        except Exception as ex:
            errors.append("Student invalid!")
            
        try:    
            validator_pb.validate(lab.get_problema())
        except Exception as ex:
            errors.append("Problema invalida")
        
        if lab.get_nota() != "Momentan laboratorul nu a fost notat!":     
            if lab.get_nota() < 0 or lab.get_nota() > 10:  
                errors.append("Nota trebuie sa fie cuprinsa in intervalul [1, 10]")    
        
        if(len(errors) > 0):
            raise ValidatorException(errors) 
            
def testLabValidator():   
    st = Student("5", "alex", "210")
    pb = Problema("3-20", "Aflati minimul dintre a si b", "3.12.2020")
    lab1 = Laborator(st, pb, 9.5)
    
    validator = LabValidator()
    
    try:
        validator.validate(lab1)
        assert True
    except ValidatorException as ex:
        assert False
        
    lab2 = Laborator(st, pb, 11)    
    try:
        validator.validate(lab2)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 1 

    st3 = Student("5", "", "210")
    pb3 = Problema("3-20", "", "3.12.2020")
    lab3 = Laborator(st3, pb3, -3)
    
    try:
        validator.validate(lab3)
        assert False
    except Exception as ex:
        assert len(ex.getErrors()) == 3
              
testLabValidator()                      
               