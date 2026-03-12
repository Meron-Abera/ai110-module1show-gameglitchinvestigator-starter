# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
 1, I expected the game to show the correct hint after submitting a number, but it gives the opposite response. For example, when the secret number was 51, submitting a number greater than 51 displayed “Go Higher”, and submitting a lower number produced the opposite incorrect hint.

 2, After selecting a difficulty level, I expected Easy to have a range smaller than 1–100, since Normal is 1–100. While Easy correctly uses 1–20, selecting Hard unexpectedly shows 1–50, which is a smaller range instead of a wider one.

 3, I expected the input field to restrict numbers to the selected range, but it allows values outside the limits, including negatives. For example, for Hard (1–50) it still accepts numbers such as 52 or -1. In addition to that it resets secret to a hardcoded 1–100 range (ignores difficulty).

 4, After using all attempts, when I change the difficulty level, the main page shows Attempts left: 0 changing to Attempts left: -2, while the navigation bar still displays Attempts allowed: 8, creating inconsistent attempt counts.

 5, I tested the game after the first commit and I encountered another bug which was allowing the secret to be out of range and the same for all difficulty level (Example secret =34 on level normal(1-100) and easy(1-20))

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  - I used a ChatGPT-style interactive coding assistant during this session and drew on suggestions that are similar to GitHub Copilot's recommendations while editing files.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  - What the AI suggested: Extract the core game logic (input parsing and guess comparison) out of the Streamlit UI and centralize it in a module (`logic_utils.py`) so it can be unit tested and reused by the UI.
  - Correct or incorrect?  Correct.
  - How I verified it: I inspected and updated `logic_utils.py` to contain `parse_guess` and `check_guess`, then wrote focused unit tests in `tests/test_game_logic.py` that exercise boundary cases and numeric conversions. The tests passed after the implementation, which confirmed the logic is centralized and behaves as expected.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  - What the AI suggested: Use a simple fallback conversion such as `int(str(value))` in the comparison fallback so non-int inputs would be coerced for numeric comparison.
  - Correct or incorrect?: Incorrect/misleading for this codebase.
  - How I verified it: I added a test (`test_guess_handles_string_and_float_inputs`) asserting that `check_guess("60.0", 50)` should return `"Too High"`. Running `pytest` initially failed: the function returned `"Too Low"` for the string "60.0". Inspecting `logic_utils.py` showed the fallback used `int(str(guess))`, which raises for the string "60.0" and allowed an early exception path that returned the wrong default. I fixed the code to use `int(float(str(...)))` in the fallback so float-like strings parse correctly, and the test passed afterwards.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
- How did you decide whether a bug was really fixed?

  - I considered a bug fixed when a focused unit test that reproduces the failing behavior passes and when manual inspection of the code confirms there are no remaining early-exit or fallback paths that could reintroduce the problem. In practice that meant adding a test that reproduced the failure and then iterating on the implementation until the test and the full test suite passed.In addition, I also tested the game by running it on local host and the issues were fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  - The concrete test I added is `tests/test_game_logic.py::test_guess_handles_string_and_float_inputs`, which asserts that `check_guess("60", 50)` and `check_guess("60.0", 50)` both return `"Too High"`. Running `python3 -m pytest -q` initially showed one failing test: the float-string case returned `"Too Low"` instead of `"Too High"`. That failure pointed directly to the fallback parsing logic in `logic_utils.check_guess`. After changing the fallback to use `int(float(str(...)))`, I re-ran the tests and the suite reported `4 passed`.

- Did AI help you design or understand any tests? How?

  - Yes. The AI suggested adding focused unit tests around parsing and comparison edge cases (strings, float-like strings, and out-of-range inputs), which I implemented. Those tests helped pinpoint the exact mismatch between intended behavior and actual behavior and validated the fix after code changes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
