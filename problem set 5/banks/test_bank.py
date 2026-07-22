from bank import value


def test_hello():
    assert value("Hello, World") == 0
    assert value("hello") == 0
    assert value("   hello") == 0
    assert value("HELLO!") == 0


def test_h():
    assert value("Hi") == 20
    assert value("Howdy") == 20
    assert value("H3ll0") == 20
    assert value("   hi") == 20


def test_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Bye") == 100