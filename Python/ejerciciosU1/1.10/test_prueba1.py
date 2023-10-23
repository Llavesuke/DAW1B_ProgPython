import pytest
from prueba1 import comparacion

def test_comparacion():
    assert comparacion (2,1) == 2 
    assert comparacion (5,5) == 0 
    assert comparacion (4,7) == 7
    assert comparacion (-3,0) == 0