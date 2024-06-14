import pytest

from src.core.calculator import *

def test_compute_rpn():
    assert compute_npi("2 3 +") == 5
    assert compute_npi("2 3 *") == 6
    assert compute_npi("2 3 -") == -1
    assert compute_npi("2 3 /") == pytest.approx(0.6666666, rel=1e-6)
    assert compute_npi("2 5 6 + *") == 22
    assert compute_npi("1 1 1 1 1 + + + +") == 5
