import pytest
from factorial import factorial

def test_factorial_valid():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        factorial(-1)

def test_factorial_invalid_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        factorial("a")