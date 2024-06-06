# tests/test_calc_soft.py

import sys
import os
import pytest

# Ajoutez le chemin du répertoire parent au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Maintenant, vous pouvez importer les fonctions de main.py
from main import add, soust, mult, div

def test_addition():
    """Teste la fonction d'addition."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_soustraction():
    """Teste la fonction de soustraction."""
    assert soust(2, 3) == -1
    assert soust(-1, 1) == -2
    assert soust(0, 0) == 0

def test_multiplication():
    """Teste la fonction de multiplication."""
    assert mult(2, 3) == 6
    assert mult(-1, 1) == -1
    assert mult(0, 0) == 0

def test_division():
    """Teste la fonction de division."""
    assert div(6, 3) == 2
    assert div(10, 2) == 5
    assert div(5, 2) == 2.5

def test_division_by_zero_with_exception():
    """Teste la division par zéro avec une exception levée."""
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_division_with_zero_denominator():
    """Teste la division par zéro avec une exception levée."""
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_division_by_zero():
    """Teste la division par zéro avec une exception levée."""
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
