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
        stripped = raw.strip()
        if "." in stripped:
            # Reject whole-number decimals as integer (e.g., "1000.0", "1000.00")
            value = int(float(stripped))
            return False, None, "That is not an integer."
        else:
            value = int(stripped) 
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: AI helped identify that the hint directions were reversed. I corrected the comparison logic and verified the behavior with pytest.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

# FIX: AI-assisted review revealed that "Too High" guesses could incorrectly award points.
# FIX: Manual analysis showed that the minimum-score safeguard was unreachable with an 8-attempt limit.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score