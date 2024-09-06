import pytest
from command_sample.batch import hello_user

def test_hello_user():
    assert hello_user("unit test") == 'hello, unit test!'
