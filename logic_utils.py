# There is no bug in this function but for readibility, I moved it here
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: AI helped identify that decimal inputs were being truncated to integers. I implemented the validation and verified it with regression tests.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # Should not accepts decimal inputs by truncating them to integers.
        if "." in raw:
            value = int(float(raw))
            return False, None, "That is not a integer."
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIXED: No exception handling is needed here because input validation is performed before this function is called.
# FIX: AI helped identify that the hint directions were reversed. I corrected the comparison logic and verified the behavior with pytest.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    if guess > secret:
        # should return lower
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIXED: 1.Modified the scoring logic for cases: "Too High" on even attempt used to ADD 5 pts.
# FIXED: 2.Removed unreachable minimum-score check. With a maximum of 8 attempts, the point already ranges from 80 to 10, so can never drop below 10.
# FIX: AI helped review the scoring logic. I verified that "Too High" guesses should never increase the player's score.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number+1)
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")