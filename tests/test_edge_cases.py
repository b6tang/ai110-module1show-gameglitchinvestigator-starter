import pytest
from logic_utils import parse_guess, get_range_for_difficulty

# --- Edge-case input suite ---

def test_parse_guess_empty_string():
    """Empty string must be rejected with an error message."""
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_decimal_whole_number():
    """'5.0' contains '.', must be rejected even though it represents an integer."""
    ok, value, err = parse_guess("5.0")
    assert ok is False
    assert value is None
    assert err is not None

def test_negative_guess_rejected_by_bounds():
    """
    parse_guess("-5") succeeds (valid integer), but -5 falls below the minimum
    range for any difficulty. This test mirrors the bounds check in app.py.
    """
    low, high = get_range_for_difficulty("Easy")  # range: 1–20
    
    ok, guess_int, err = parse_guess("-5")
    assert ok is True                          # parse succeeds: -5 is a valid integer
    assert not (low <= guess_int <= high)      # bounds check rejects it

def test_parse_guess_very_large_integer():
    """'99999999999999' is a valid integer; parse_guess must accept it (bounds checked in app)."""
    ok, value, err = parse_guess("99999999999999")
    assert ok is True
    assert value == 99999999999999
    assert err is None

def test_parse_guess_double_minus():
    """'--5' is malformed; must be rejected as not a number."""
    ok, value, err = parse_guess("--5")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_plus_minus():
    """'+-5' is malformed; must be rejected as not a number."""
    ok, value, err = parse_guess("+-5")
    assert ok is False
    assert value is None
    assert err is not None