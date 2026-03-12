from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_guess_handles_string_and_float_inputs():
    # Ensure non-int input types that represent numbers still compare correctly
    # e.g., the guess as a numeric string or float-string should be treated as the number
    assert check_guess("60", 50) == "Too High"
    assert check_guess("60.0", 50) == "Too High"
