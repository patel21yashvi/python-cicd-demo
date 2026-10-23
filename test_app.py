from app import greet, add
def test_greet():
    assert greet("Student") == "Hello, Student!"
def test_add():
    assert add(10, 20) == 30
def test_add_negative_numbers():
    assert add(-2, -3) == -5
