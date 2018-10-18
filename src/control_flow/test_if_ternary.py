"""IF statement

@see: https://docs.python.org/3/reference/expressions.html#conditional-expressions

if ternary to evaluate condition to store into variable in the same sentence.
"""


def test_if_ternary_statement():
    """IF ternary statement"""
    
    number = 10
    result = ""
    
    result = "number even" if number % 2 == 0 else "number odd" 

    assert result == 'number even'


