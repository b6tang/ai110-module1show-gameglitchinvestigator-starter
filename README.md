# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose of the Game:** The Number Guessing Game challenges players to guess a randomly generated number within a limited range. The game provides feedback after each guess, updates the score based on performance, and allows players to select different difficulty levels.
- **Bugs Found and Fixed Applied :** 
   - Decimal float inputs were accepted and silently converted to integers.
      - Fixed by rejecting non-integer input values.
   - Guesses hint displayed the wrong direction.
      - Fixed by changing the wrone feedback string.
   - Changing the difficulty did not reset the secret number, score, attempts, or guess history.
      - Fixed by tracking difficulty changes in session_state and performing reset when the selected difficulty changes.
   - The scoring logic incorrectly added 5 points for some "Too High" guesses instead of deducting points.
     - Fixed by correcting the score calculation logic and enforcing the intended scoring rules.
   - Attempts started at 1 instead of 0, causing incorrect attempt counts and score calculations.
      - Fixed by initializing the attempt counter to 0.
   - Invalid inputs increased the attempt counter.
       - Fixed by ensuring only valid guesses count as attempts.
   - Starting a new game used a hardcoded number range instead of the selected difficulty range.
      - Fixed by generating a new secret number using the current difficulty's low and high bounds.
   - The information panel sometimes displayed stale data after state updates.
      - Fixed by using st.empty() placeholders to refresh the displayed information after state changes.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Easy difficulty from the sidebar.
2. User enters a guess of 10.
3. The game returns "Go LOWER!".
4. User enters a guess of 5.
5. The game returns "Go LOWER!".
6. User enters a guess of 3.
7. The game displays balloons and "You won!..." with the final score
8. The game ends and the user can choose to start a new game

**Screenshot** *(optional)*: <img src="demo.png" width="600">
## 🧪 Test Results

```
collected 11 items                                                                                                                                      

tests/test_game_logic.py::test_parse_guess_rejects_decimal PASSED                                                                                 [  9%]
tests/test_game_logic.py::test_parse_guess_rejects_decimal_dot_zero PASSED                                                                        [ 18%]
tests/test_game_logic.py::test_parse_guess_accepts_plain_integer PASSED                                                                           [ 27%]
tests/test_game_logic.py::test_check_guess_high_gives_lower_hint PASSED                                                                           [ 36%]
tests/test_game_logic.py::test_check_guess_low_gives_higher_hint PASSED                                                                           [ 45%]
tests/test_game_logic.py::test_check_guess_exact_is_win PASSED                                                                                    [ 54%]
tests/test_game_logic.py::test_update_score_too_high_even_attempt_subtracts PASSED                                                                [ 63%]
tests/test_game_logic.py::test_update_score_too_high_odd_attempt_subtracts PASSED                                                                 [ 72%]
tests/test_game_logic.py::test_update_score_win_attempt_1 PASSED                                                                                  [ 81%]
tests/test_game_logic.py::test_update_score_win_attempt_8 PASSED                                                                                  [ 90%]
tests/test_game_logic.py::test_update_score_win_never_below_10_within_limit PASSED                                                                [100%]

================================================================== 11 passed in 0.03s ==================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
