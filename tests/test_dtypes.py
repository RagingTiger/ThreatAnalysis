def test_threat_str_rep(mock_threats):
    """Test string representation of Threat objects."""
    # get orange threat
    oranges = mock_threats['oranges']

    # gen format expected
    expected = f'Threat({oranges.name}): {oranges.relevance}'

    # check string representation
    assert expected == oranges.__str__()
