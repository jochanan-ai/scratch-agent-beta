"""Convert strings into URL-friendly slugs.

A slug is lowercase text with all non-alphanumeric characters removed
and the remaining words joined by single hyphens, e.g. "hello-world".
Runs of consecutive separators are collapsed, so a slug never contains
repeated hyphens ("--").
"""

import re

_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def slugify(text):
    """Lowercase the text, strip non-alphanumerics, and join words with hyphens.

    Every run of one or more non-alphanumeric characters is replaced by a
    single hyphen and leading/trailing hyphens are stripped, so the output
    never contains consecutive hyphens.
    """
    return _NON_ALNUM_RE.sub("-", text.lower()).strip("-")
