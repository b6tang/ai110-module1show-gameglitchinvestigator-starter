# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

In claude: (attached `logic_utils.py` and `app.py`)"Review my number guessing game and identify 10 potential edge-case inputs that could cause incorrect behavior, crashes, or unexpected results. Is there more edge cases?"

**What did the agent do?**

### What did the agent do?

1. Read both `logic_utils.py` and `app.py`.
2. Traced the input-validation and guess-processing flow.
3. Identified potential edge cases such as empty strings, whole-number decimal, scientific notation, negative numbers, and very large integers.
4. Reviewed scoring logic and highlighted possible issues related to score calculation.
5. Suggested which edge cases would be valuable candidates for additional pytest coverage.
6. Provided explanations for why each edge case might cause unexpected behavior.


1. Reviewed each reported issue to determine whether it was an actual bug or intended behavior.
2. Traced the relevant code paths manually to confirm the agent's findings.
3. Selected the most useful edge cases for testing.
4. Verified the behavior of the application before deciding which changes or tests to add.



**What did you have to verify or fix manually?**

- I had to determine which of the agent's suggestions were actual input edge cases for the assignment. For example, inputs such as `""`, `"1e2"`, and `"99999999999999"` were relevant test cases, while score-calculation issues were not input edge cases.

- I had to verify the agent's analysis by tracing the code manually. For example, I confirmed that `"1e2"` reaches the exception-handling path and that `" 5 "` is accepted because the input is stripped before parsing.

- I had to review the agent's recommendations and decide which findings were valid, which were design choices, and which should be covered by additional pytest tests.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|Empty string input ("")  |Review my game and suggest edge cases.| Empty string must be rejected with an error message| Yes| Users may click Submit without entering a value.|
|whole-number decimal input ("5.0")|Same prompt as above | '5.0' contains '.', must be rejected even though it represents an integer.| Yes| The game should only accept integer guesses.|
|Negative number ("-5") |Same prompt as above | the game should
    then reject it because -5 falls below the minimum range.| Yes| The game should only accept positive integer guesses.|
|Malformed signed number ("--5" or "+-5")|Same prompt as above|'--5' is malformed; must be rejected as not a number.| Yes| Tests validation of malformed user input.|
|Very large integer ("99999999999999")|Same prompt as above|'99999999999999' is a valid integer; parse_guess must accept it (bounds checked in app).| Yes| Tests extreme numeric input.|
---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Review my both files for style and readability improvements.
```

**Linting output before:**

```
Location	Severity	Issue
app.py:4	nit	Missing space before update_score in import
app.py:24	nit	Trailing whitespace after attempt_limit_map[difficulty]
app.py:31	nit	Typo: "claer" → "clear"
app.py:39	nit	Inline comment # don't forget to update the last_difficulty — obvious, delete
app.py:45	nit	# FIXED: attempts should start from zero — obvious from code, delete
app.py:60	nit	Long FIX comment on placeholder — belongs in commit message, not code
app.py:79	nit	# FIXED: use difficulty range — vague, doesn't explain the original bug
app.py:82	nit	# FIXED reset the score... — missing colon, and again: obvious from code
app.py:94	risk	# st.stop() commented out — dead code, unclear if intentional or forgotten
app.py:106	nit	FIX comment on attempt-count logic — belongs in commit message
app.py:140	nit	# FIXED: use actual range variables — dead comment inside placeholder fill, delete

Location	Severity	Issue
logic_utils.py:1	nit	"There is no bug" — defensive, delete
logic_utils.py:28	nit	"would not accept" → "rejects"
logic_utils.py:30	nit	"a integer" → "an integer" (user-visible bug)
logic_utils.py:58	nit	attempt_number+1 unexplained — add space: attempt_number + 1 and a comment why

```

**Changes applied:**

app.py:
Line 4: add space before update_score in import
Line 31: fix typo claer → clear
Line 39: remove inline comment # don't forget to update the last_difficulty
Line 94: remove # st.stop() dead commented-out code

logic_utils.py:
Line 1: remove # There is no bug comment
Line 28: "would not accept Whole-number decimals" → "rejects whole-number decimals"
Line 30: "a integer" → "an integer"
Line 58: attempt_number+1 → attempt_number + 1 (spacing)

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
