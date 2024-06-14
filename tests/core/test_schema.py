from src.core.schemas import *
from pytest import raises

def test_validate_npi():
    assert validate_npi('1 1+') == '1 1 +'
    assert validate_npi('1 1 1++') == '1 1 1 + +'
    assert validate_npi('2 5 6+*') == '2 5 6 + *'
    with raises(ValueError):
        assert validate_npi('1 1 ++')
        assert validate_npi('1 1 1+')
        assert validate_npi('1 1 11')