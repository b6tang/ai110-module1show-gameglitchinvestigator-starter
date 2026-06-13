import pytest
from logic_utils import parse_guess, check_guess, update_score


# --- Bug 1: parse_guess truncated decimals instead of rejecting them ---
# Old: parse_guess("3.7") → (True, 3, None)
# Fixed: any input with "." must return ok=False

def test_parse_guess_rejects_decimal():
    """Bug 1: decimal input must be rejected, not silently truncated to int."""
    ok, value, err = parse_guess("3.7")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_rejects_decimal_dot_zero():
    """Bug 1: '5.0' looks integer-like but contains '.', must still reject."""
    ok, value, err = parse_guess("5.0")
    assert ok is False

def test_parse_guess_accepts_plain_integer():
    """Sanity: valid integer string must still pass after the decimal fix."""
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


# --- Bug 2: check_guess returned reversed hint messages ---
# Old: guess > secret → "Go HIGHER!" (wrong direction)
# Fixed: guess > secret → "Go LOWER!"

def test_check_guess_high_gives_lower_hint():
    """Bug 2: guessing too high must tell player to go LOWER, not HIGHER."""
    outcome, message = check_guess(10, 5)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_check_guess_low_gives_higher_hint():
    """Bug 2: guessing too low must tell player to go HIGHER, not LOWER."""
    outcome, message = check_guess(3, 8)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_check_guess_exact_is_win():
    """Sanity: correct guess must return Win regardless of hint-direction fix."""
    outcome, _ = check_guess(7, 7)
    assert outcome == "Win"


# --- Bug 3: "Too High" on even attempts incorrectly added +5 instead of -5 ---
# Old: attempt_number % 2 == 0 → current_score + 5
# Fixed: always subtract 5

def test_update_score_too_high_even_attempt_subtracts():
    """Bug 3: Too High on even attempt must subtract 5, not add 5."""
    score = update_score(50, "Too High", 2)
    assert score == 45

def test_update_score_too_high_odd_attempt_subtracts():
    """Bug 3: Too High on odd attempt must also subtract 5 (consistent)."""
    score = update_score(50, "Too High", 3)
    assert score == 45


# --- Bug 4: update_score had unreachable minimum-score guard ---
# Old code had `if points < 10: points = 10` but formula never reaches <10
# within max 8 attempts. The guard was removed; formula is now:
# points = 100 - 10 * (attempt_number + 1)
# attempt 1 → 80, attempt 8 → 10

def test_update_score_win_attempt_1():
    """Bug 4 / formula check: win on attempt 1 awards 80 pts (100 - 10*2)."""
    score = update_score(0, "Win", 1)
    assert score == 80

def test_update_score_win_attempt_8():
    """Bug 4: win on attempt 8 awards 10 pts — minimum, no guard needed."""
    score = update_score(0, "Win", 8)
    assert score == 10

def test_update_score_win_never_below_10_within_limit():
    """Bug 4: no attempt within 1-8 should produce negative or zero points."""
    for attempt in range(1, 9):
        score = update_score(0, "Win", attempt)
        assert score >= 10
