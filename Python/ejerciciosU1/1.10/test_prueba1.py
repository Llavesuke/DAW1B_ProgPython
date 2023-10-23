import pytest
from prueba1 import comparacion

def test_comparacion():
    assert comparacion (2,1) == 2 
    assert comparacion (5,5) == 0 
    assert comparacion (4,7) == 7
    assert comparacion (-3,0) == 0

@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (2,1,2),
        (5,5,0),
        (8,9,9),
        (-3,-9,-3),
        (0,0,0)
    ]
)
def test_comparacion_params(input_num1, input_num2, expected):  
    assert comparacion(input_num1, input_num2) == expected