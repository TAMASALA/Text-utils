from text_utils import (
    count_words,
    normalize_whitespace,
    is_valid_email,
    reverse_words,
)


def test_count_words():
    assert count_words("hello world python") == 3
    assert count_words("one two") == 2


def test_normalize_whitespace():
    assert normalize_whitespace("hello   world") == "hello world"
    assert normalize_whitespace("  hello \n world  ") == "hello world"


def test_valid_email():
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("john.doe@test.org") is True
    assert is_valid_email("invalid-email") is False


def test_reverse_words():
    assert reverse_words("hello world python") == "python world hello"
    assert reverse_words("one two three four") == "four three two one"