import random
import string
from audioop import reverse
import operator
from Tools.scripts.eptags import treat_file


def get_random_alphanumeric(lung):
    """
    For student id
    Generate a random string of digits and lowercase letters, with the specified length 
    lung as an integer
    """
    litere_cifre = string.ascii_lowercase + string.digits
    sir = ''.join(random.choice(litere_cifre) for i in range(lung))
    return sir

def get_random_string(lung):
    """
    For student name and problem description
    Generate a random string of lowercase letters, with the specified length 
    lung as an integer
    """
    litere = string.ascii_lowercase
    sir = ''.join(random.choice(litere) for i in range(lung))
    return sir

def get_random_grupa():
    """
    For student group
    Generate a random group 
    """
    gr = random.randint(100, 999)
    return str(gr)

def get_random_problemId():
    """
    For problem id
    Generate a random problem id 
    Format: "nrLab_nrProblem"
    """
    nr_lab = random.randint(1, 14)
    nr_pb = random.randint(1, 20)
    pb_id = (str(nr_lab) + '_' + str(nr_pb))
    return pb_id


def get_radom_date():
    """
    For problem deadline
    Generate a random date
    Format: "d.m.y"
    """
    zi = random.randint(1, 31)
    luna = random.randint(1, 12)
    an = random.randint(2020, 2021)
    data = (str(zi) + '.' + str(luna) + '.' + str(an))
    return data

def ordonare(lista):
    """
    Sort alphabetical a list of lists containing ids, names and grades after 2 criteria
    First sort ascending after name 
    Secondly sort descending after grade
    """
    lista.sort(key=lambda row: row[2], reverse=True)
    lista.sort(key=lambda row: row[1])
    return lista

def apartineInterval(x, y, val):
    """
    Verify if val is a value between x and y
    """
    if val >= x and val <= y:
        return True
    return False