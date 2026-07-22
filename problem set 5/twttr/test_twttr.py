from twttr import shorten
import pytest


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("David") == "Dvd"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("1234 attia") == "1234 tt"
    assert shorten("Da1vid2") == "D1vd2"


def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("Ha:R/V(ar)+D") == "H:R/V(r)+D"

def test_shorten_lower():
    assert shorten("thisiscs50") == "thsscs50"
    assert shorten("testtwitter") == "tsttwttr"


def test_shorten_upper():
    assert shorten("HELLOWORD") == "HLLWRD"
    assert shorten("THISISCS50") == "THSSCS50"
