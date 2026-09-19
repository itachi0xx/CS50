from datetime import date
from seasons import calculate_minutes


def test_one_year():
    assert calculate_minutes(date(2000, 1, 1)) == 525600


def test_leap_year():
    assert calculate_minutes(date(1999, 1, 1)) == 527040


def test_multiple_years():
    assert calculate_minutes(date(1990, 1, 1)) == 525600 * 10 + 1440 * 2