import random
import types

import pytest

from app import update_score, reset_state_for_difficulty


def test_update_score_win_and_hints():
    # Win on first attempt should award large points
    assert update_score(0, "Win", 1) == 90
    # Too High/Too Low should add small points
    assert update_score(0, "Too High", 2) == 3
    assert update_score(5, "Too Low", 3) == 8


def test_reset_state_sets_secret_in_range(monkeypatch):
    # Force randint to return a known value to test assignment
    monkeypatch.setattr(random, "randint", lambda low, high: low + 1)

    state = {}
    reset_state_for_difficulty(state, "Easy", 1, 20)

    assert state["attempts"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert state["score"] == 0
    assert state["current_difficulty"] == "Easy"
    # secret should be within range; we forced randint so expect low+1
    assert state["secret"] == 2


def test_attempts_reset_on_difficulty_change(monkeypatch):
    # Simulate an existing session with attempts and score
    monkeypatch.setattr(random, "randint", lambda low, high: high)
    state = {"attempts": 5, "score": 42, "history": [10, 20], "current_difficulty": "Normal"}

    reset_state_for_difficulty(state, "Hard", 1, 150)

    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["history"] == []
    assert state["current_difficulty"] == "Hard"
    assert 1 <= state["secret"] <= 150
