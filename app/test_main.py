from app.main import get_human_age


def test_zero_ages() -> None:
    """Test when both cat and dog ages are zero."""
    assert get_human_age(0, 0) == [0, 0]


def test_ages_below_fifteen() -> None:
    """Test when ages are below 15, should return zero human years."""
    assert get_human_age(14, 14) == [0, 0]


def test_age_at_fifteen() -> None:
    """Test when ages reach exactly 15 years."""
    assert get_human_age(15, 15) == [1, 1]


def test_ages_between_fifteen_and_twenty_four() -> None:
    """Test ages between 15 and 23."""
    assert get_human_age(23, 23) == [1, 1]


def test_age_at_twenty_four() -> None:
    """Test when ages reach exactly 24 years."""
    assert get_human_age(24, 24) == [2, 2]


def test_ages_with_different_growth_rates() -> None:
    """Test ages where cat and dog conversion rates diverge."""
    assert get_human_age(28, 28) == [3, 2]


def test_higher_ages() -> None:
    """Test with higher ages like 100 to verify calculations."""
    assert get_human_age(100, 100) == [21, 17]
