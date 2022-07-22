import pytest
from threat.dtypes import Threat


@pytest.fixture(scope='module')
def mock_threats() -> dict[Threat]:
    """Fixture of mock threat dict data."""
    return {
        'apples':  Threat('Apples', 0.01, 0.2, 'Apple cider'),
        'oranges': Threat('Oranges', 0.04, 0.5, 'Orange juice'),
        'bananas': Threat('Bananas', 0.08, 0.1, 'Banana bread')
    }
