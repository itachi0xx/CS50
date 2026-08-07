from um import count


def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_multiple_um():
    assert count("um, um, um") == 3
    assert count("Um? um! UM.") == 3
    assert count("hello, um, world") == 1


def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("umm") == 0
    assert count("mum") == 0


def test_mixed():
    assert count("Um, thanks for the album, um.") == 2
    assert count("The umbrella is yummy.") == 0