from Repository.inmemory import StudentsRepo, ProblemsRepo, LabsRepo
from domain.validators import StudentValidator, ProblemValidator, LabValidator
from service.srv import StudentService, ProblemService, LabService
from ui.console import Console
'''
Created on Nov 9, 2020

@author: munte
'''

if __name__ == '__main__':
    rep_students = StudentsRepo()
    val_students = StudentValidator()
    ctr_students = StudentService(rep_students,val_students)
    
    rep_problems = ProblemsRepo()
    val_problems = ProblemValidator()
    ctr_problems = ProblemService(rep_problems, val_problems)
    
    rep_labs = LabsRepo()
    val_labs = LabValidator()
    ctr_labs = LabService(rep_labs, val_labs)
    
    ui = Console(ctr_students, ctr_problems,ctr_labs)
    ui.showUI()