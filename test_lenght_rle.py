from lenght_string import lenght
import pytest

@pytest.mark.parametrize('stroka, expected_result',[('A4B3', 7),
                                                    ('A15B5', 20),
                                                    ('A15BA5', 21),
                                                    ('ABCDR', 5),
                                                    ('Z123XY', 125)])
def test_lenght(stroka, expected_result):
    assert lenght(stroka) == expected_result