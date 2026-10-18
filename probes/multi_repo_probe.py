"""Multi-repo probe for the gateway-infra factory pipeline.

This is the multi-repo parallel-cycle probe (task issue #4, tier t2). It
proves the factory can write to this repo concurrently with the others by
exposing this repository's slug through a single documented function.
"""


def repo_slug():
    """Return this repository's slug: ``"beta"``."""
    return "beta"
