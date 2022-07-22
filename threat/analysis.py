from .dtypes import Threat


def rank(threats: list[Threat]) -> list[Threat]:
    """Return a sorted listed based on threat probability"""
    return sorted(threats, key=lambda t: t.relevance, reverse=True)
