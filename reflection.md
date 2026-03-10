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

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- Answer
The AI recommended moving the core game logic (parsing and guess-checking) out of the Streamlit UI into a separate module and validating guesses against the selected difficulty range. This was correct because it simplified the code and centralized validation. I verified it using small unit tests and manual playthroughs; parse_guess now rejects out-of-range inputs and check_guess returns correct results.

Incorrect / misleading AI suggestion
The AI suggested a parity-based approach that sometimes converted the secret number to a string, which caused lexicographic comparisons (e.g., '9' > '51'). This produced incorrect hints. I identified the issue by reviewing the code and testing examples, then fixed it by ensuring both the secret and guess are always compared as integers.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
