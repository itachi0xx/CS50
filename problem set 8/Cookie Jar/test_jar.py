import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_init_invalid():
    for bad in [-1, "cat", 3.5, None]:
        with pytest.raises(ValueError):
            Jar(bad)


def test_zero_capacity():
    jar = Jar(0)
    assert jar.capacity == 0
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10


def test_deposit_overflow():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0


def test_withdraw_too_many():
    jar = Jar(10)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
    assert jar.size == 2


def test_negative_amounts():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    assert jar.size == 5