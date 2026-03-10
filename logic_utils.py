import typing


def parse_guess(raw: str, low: int, high: int) -> typing.Tuple[bool, typing.Optional[int], typing.Optional[str]]:
    """Parse a raw input string into an integer guess and validate range.

    Returns (ok, value, error_message).
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # allow floats by converting to int after float parsing
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # Validate against the allowed range
    try:
        if value < low or value > high:
            return False, None, f"Enter a number between {low} and {high}."
    except Exception:
        # defensive: if low/high are not ints for any reason
        return False, None, "Invalid difficulty range configuration."

    return True, value, None


def check_guess(guess: int, secret: int) -> typing.Tuple[str, str]:
    """Compare numeric guess to numeric secret and return (outcome, message).

    outcome is one of: "Win", "Too High", "Too Low".
    message is a short hint for the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # Ensure both are integers for numeric comparison
    try:
        if guess > secret:
            # guess is greater than secret -> too high, tell player to go lower
            return "Too High", "📉 Go LOWER!"
        else:
            # guess is less than secret -> too low, tell player to go higher
            return "Too Low", "📈 Go HIGHER!"
    except Exception:
        # Fallback: if non-numeric values slipped through, convert safely
        try:
            g = int(str(guess))
            s = int(str(secret))
            if g == s:
                return "Win", "🎉 Correct!"
            if g > s:
                return "Too High", "📉 Go LOWER!"
            return "Too Low", "📈 Go HIGHER!"
        except Exception:
            # If still failing, return a neutral response
            return "Too Low", "📈 Go HIGHER!"
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
  
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
