# classes
class Threat():
    """Object to encapsulate threat information"""
    def __init__(self,
                 name: str,
                 probability: float,
                 impact: float,
                 mvp: str) -> None:
        self.name = name
        self.probability = probability
        self.impact = impact
        self.relevance = self.probability * self.impact
        self.mvp = mvp

    def __repr__(self) -> str:
        """Printable string representation of Threat() object"""
        return '<{0}.{1} object at {2}>'.format(
            type(self).__module__, type(self).__qualname__, hex(id(self))
        )

    def __str__(self) -> str:
        """Readable string representation of Threat() object"""
        return f'Threat({self.name}): {self.relevance}'


# functions
def rank(threats: list[Threat]) -> list[Threat]:
    """Return a sorted listed based on threat probability"""
    return sorted(threats, key=lambda t: t.relevance, reverse=True)
