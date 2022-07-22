import pytest
from threat.dtypes import Threat
from threat.analysis import rank


# mocking
@pytest.fixture
def mock_threats() -> dict[Threat]:
    """Fixture of mock threat dict data."""
    return {
        'apples':  Threat('Apples', 0.01, 0.2, 'Apple cider'),
        'oranges': Threat('Oranges', 0.04, 0.5, 'Orange juice'),
        'bananas': Threat('Bananas', 0.08, 0.1, 'Banana bread')
    }


# tests
def test_ranking_order(mock_threats):
    """Test whether ranking algo arrives at correct order."""
    # get ranked threats list
    threats_ranked = rank(mock_threats.values())

    # check if highest rank is at top
    assert threats_ranked[0].name == 'Oranges'


def test_threat_str_rep(mock_threats):
    """Test string representation of Threat objects."""
    # get orange threat
    oranges = mock_threats['oranges']

    # gen format expected
    expected = f'Threat({oranges.name}): {oranges.relevance}'

    # check string representation
    assert expected == oranges.__str__()
