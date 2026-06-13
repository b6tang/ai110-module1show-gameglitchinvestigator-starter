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

  Claude

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
