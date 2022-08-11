from arithmetic_operation import arithmetic_operation
import pytest


@pytest.mark.parametrize("a,b,expected_result", [(10,5,15)])
def test_arithmetic_add(a,b,expected_result):
    add = arithmetic_operation("+")
    assert add(a,b) == expected_result

@pytest.mark.parametrize("a,b,expected_result", [(10,5,2)])
def test_arithmetic_div(a,b,expected_result):
    div = arithmetic_operation("/")
    assert div(a,b) == expected_result

@pytest.mark.parametrize("expected_exception, divider", [(ZeroDivisionError, 0),
                                                         (TypeError, '2')])
def test_arithmetic_zero(expected_exception, divider):
    with pytest.raises(expected_exception):
        div = arithmetic_operation("/")
        div(10, divider)