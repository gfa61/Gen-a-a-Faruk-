import pytest
from arithmetic_aranger import arithmetic_arranger

test_cashes =[
    #testi gir
]


@pytest.mark.parametrize('arguments,expected_output,fail_message')

def test_template(arguments,expected_output,fail_message):
    actual = arithmetic_arranger(*arguments)
    assert actual == expected_output,fail_message