import pytest
from git_python_test.phrase import Phrase


def test_init_value():
    test_phrase = Phrase()
    assert test_phrase.name == "PyTest"


def test_set_name():
    test_phrase = Phrase()
    test_name = "tests"
    test_phrase.set_name(name=test_name)

    assert test_phrase.name == test_name


def test_hello():
    test_phrase = Phrase()
    assert test_phrase.hello_phrase() == "Hello PyTest"
