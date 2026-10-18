"""Capitalize each word of a space-separated string.

Each whitespace-separated word has its first letter uppercased and the
rest lowercased, e.g. "hello world" becomes "Hello World".
"""


def title_case(text):
    """Capitalize each word of the text and join the words with single spaces."""
    return " ".join(word.capitalize() for word in text.split())
