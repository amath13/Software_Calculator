# main.py

def add(a, b):
# Additionne deux nombres."""
    return a + b

def soust(a, b):
# Soustraction de deux nombres 
    return a - b

def mult(a, b):
# Multiplie deux nombres.
    return a * b

def div(a, b):    
# Divise a par b Si b est zéro, lève une exception ZeroDivisionError.
    
    if b == 0:
        raise ZeroDivisionError("Erreur: division par zéro!")
    return a / b
