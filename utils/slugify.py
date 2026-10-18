"""Convert strings into URL-friendly slugs.

A slug is lowercase text with all non-alphanumeric characters removed
and the remaining words joined by single hyphens, e.g. "hello-world".
"""

import re

_WORD_RE = re.compile(r"[a-z0-9]+")


def slugify(text):
    """Lowercase the text, strip non-alphanumerics, and join words with hyphens."""
    return "-".join(_WORD_RE.findall(text.lower()))
