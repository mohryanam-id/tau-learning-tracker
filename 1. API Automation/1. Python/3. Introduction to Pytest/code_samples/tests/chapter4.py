# Parametrized Test Cases
import pytest

products = [
    (2, 3, 6),
    (1, 99, 99),
    (2, 4, 8)
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiple(a, b, product):
    assert a * b == product
