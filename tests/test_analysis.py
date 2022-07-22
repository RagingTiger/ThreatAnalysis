from threat.analysis import rank


def test_ranking_order(mock_threats):
    """Test whether ranking algo arrives at correct order."""
    # get ranked threats list
    threats_ranked = rank(mock_threats.values())

    # check if highest rank is at top
    assert threats_ranked[0].name == 'Oranges'
