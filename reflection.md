# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. When I changed the difficulty, the number range stayed at 1–100 instead of changing
  2. The hint gave the wrong direction. When my guess was too high, it told me to guess higher.
  3. Sometimes the game did not deduct points after an incorrect guess, while other times it did..
  4. New Game did not reset history and score. After the game ended(either by winning or running out of attempts), clicking "New Game" generated a new number, but the game did not fully restart. The "Submit Guess" button stopped responding, so I could not make any new guesses.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Changed difficulty from Normal to Easy | "Guess a number between 1 and 100. Attempts left: 8" | "Guess a number between 1 and 100. Attempts left: 5" | None                   |
| Entered guess: 50 (the Secret: 75)     | "Go HIGHER!" hint                                    | "Go LOWER!" hint instead | None                   |
| Entered guess: 50, then enter 40, then enter 30 (the Secret: 62) | Score change from 0 to -5, then -10 | Score change from 0 to -5, then5 | None                   |
| Finished a game, then clicked "New Game", enter new guess | A new game should start and accept new guesses                 |Only the secret number was regenerated and the attempt count was reset to 0, other game state were not reset. And it does not take new guess.| None                   |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Correct AI Suggestion: The AI identified that the `check_guess()` function tells player wrong direction. message says "Go HIGHER" but outcome is "Too High". The suggestion was correct. I verified it by playing the game testing several guesses against a known secret value. After confirming the issue, I updated the logic and confirmed that the hints matched the expected behavior.

Misleading AI Suggestion: The AI assumed that the scoring system needed a minimum score floor of 10 to prevent negative values. The suggestion was misleading. After reviewing the game's attempt limit (8 attempts maximum), I verified that the score already ranged from 10 to 80 and could never become negative. Therefore, this suggestion was not applicable to the actual game logic.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I considered a bug fixed when the code behavior matched the intended game rules and the incorrect behavior could no longer be reproduced.

One manual test I ran was entering several decimal values such as "5.1". Before the fix, the game accepted and converted it to an integer. After the fix, the game correctly rejected the input and displayed an error message. 
I also used pytest to test my fixes. I listed the bugs I fixed and asked AI to generate test cases for test_game_logic.py. I then ran the tests and verified that the fixes worked as intended.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is like a printer. Every time it reruns, it will stop from where it is, and "print" the script from the beginning to the end of the script. Besides rerun(), every interaction will trigger rerun automatically for example clicking a button, typing in a box. Thus we should be very careful about the position of the display blocks and variable mutations in the script. Value changed after the display blocks may not be reflected immediately.

Because Streamlit reruns the script many times, it needs a place to remember important information. That place is called session state. You can think of it as a dictionary that stores data in the background and is not affected by reruns. This allows the app to remember things like difficulty, attempts, and game history even when the page reruns.
  
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is understanding the overall code structure before debugging. During this project, taking time to understand how different parts of the program worked together helped me trace bugs more effectively and identify their root causes.

Next time I would discussing one bug at a time with AI. When I focused on a single issue, the explanations were clearer and it was easier to verify the suggested fixes.

Before this project, I mainly used AI as a chatbot. I was surprised to learn that it could analyze multiple files, help debug code, and generate tests more like a coding agent than a simple conversation tool.

