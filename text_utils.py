import re


def count_words(text):
    """Return the number of words in a string."""
    words = text.split()
    return len(words)


def normalize_whitespace(text):
    """Replace repeated whitespace with a single space."""
    return re.sub(r"\s+", " ", text).strip()


def is_valid_email(email):
    """Return True when the email has a basic valid format."""
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def reverse_words(text):
    """Reverse the order of words while preserving each word."""
    words = text.split()
    return " ".join(reversed(words))