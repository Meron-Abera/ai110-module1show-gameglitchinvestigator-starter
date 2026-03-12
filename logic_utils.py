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

    # Validate against the allowed range (reject negatives and out-of-bounds)
    try:
        if value < low or value > high:
            return False, None, f"Enter a number between {low} and {high}."
        if value < 0:
            return False, None, "Negative numbers are not allowed."
    except Exception:
        # defensive: if low/high are not ints for any reason
        return False, None, "Invalid difficulty range configuration."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """Compare numeric guess to numeric secret and return outcome string.
    
    outcome is one of: "Win", "Too High", "Too Low".
    This function matches the test API which expects a single string return.
    """
    if guess == secret:
        return "Win"

    # Ensure both are integers for numeric comparison
    try:
        if guess > secret:
            # guess is greater than secret -> too high
            return "Too High"
        else:
            # guess is less than secret -> too low
            return "Too Low"
    except Exception:
        # Fallback: if non-numeric values slipped through, convert safely
        try:
            # allow float-like strings (e.g. "60.0") and numeric types
            g = int(float(str(guess)))
            s = int(float(str(secret)))
            if g == s:
                return "Win"
            if g > s:
                return "Too High"
            return "Too Low"
        except Exception:
            # If still failing, return a neutral response
            return "Too Low"


def check_guess_verbose(guess: int, secret: int) -> typing.Tuple[str, str]:
    """Compare numeric guess to numeric secret and return (outcome, message).

    outcome is one of: "Win", "Too High", "Too Low".
    message is a short hint for the player.
    Used by the Streamlit UI to provide user-facing feedback.
    """
    outcome = check_guess(guess, secret)
    
    if outcome == "Win":
        message = "🎉 Correct!"
    elif outcome == "Too High":
        message = "📉 Go LOWER!"
    else:  # Too Low
        message = "📈 Go HIGHER!"
    
    return outcome, message
