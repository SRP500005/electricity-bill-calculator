import pytest
from app import calculate_bill

def test_normal_bill():
    assert calculate_bill(100,0.30) ==30.00
    
def test_zero_units():
    assert calculate_bill(0,0.30) == 00.00
    
def test_zero_price():
     assert calculate_bill(100,0) == 00.00
        
def test_rounding():
    assert calculate_bill(100,0.3333) == 33.33
    
def test_negative_consumption():
    with pytest.raises(ValueError, match = "Consumption can not be -ve"):
        calculate_bill(-100,0.30)
        
def test_negative_price():
    with pytest.raises(ValueError, match = "Price per unit can not be -ve"):
        calculate_bill(100,-0.30)