def calculate_square(number):
    square= number*number
    return square
# Test Case:
def test_calculate_square():
    assert calculate_square(0)==0
    assert calculate_square(1)==1
    assert calculate_square(2)==4
    print("All test cases passed")

test_calculate_square()