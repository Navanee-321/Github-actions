# app.py
# this is a test commit

def add(a, b):
    return a + b

def test_add():
    # Existing tests
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    
    # Additional test cases
    assert add(0, 0) == 0  # Adding two zeros
    assert add(-5, -5) == -10  # Adding two negative numbers
    assert add(2.5, 3.5) == 6.0  # Adding two float numbers
    assert add(1000000, 1) == 1000001  # Large number addition

# This allows the test to run when executed as a standalone script
if __name__ == "__main__":
    test_add()
    print("All tests passed!")

