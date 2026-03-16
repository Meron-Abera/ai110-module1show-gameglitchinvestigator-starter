from logic_utils import parse_guess


def test_parse_guess_trims_whitespace_and_float():
    ok, value, err = parse_guess(" 60.0 ", 1, 100)
    assert ok is True
    assert value == 60
    assert err is None


def test_parse_guess_negative_input_reports_range_error():
    # Negative number should be rejected; current behavior returns range error
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    # parse_guess currently reports out-of-range for negatives (since check for
    # value < low comes first), so assert the expected message.
    assert err == "Enter a number between 1 and 100."
