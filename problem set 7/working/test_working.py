import pytest
from working import convert


def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"


def test_overnight():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5:99 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9 to 5")

    with pytest.raises(ValueError):
        convert("09:00 AM 5:00 PM")