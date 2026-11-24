# 🅰️ Track A: Build an App

**Mission:** In about 30 minutes, go from an idea to a working web app, without writing the code yourself. You are the product owner, Bob is your developer.

### The constraints (tell Bob about them!)

- Everything in **one single `index.html` file** (HTML + CSS + plain JavaScript)
- **No frameworks, no libraries, no CDN links, no installs**
- You run it by **double-clicking `index.html`**, which opens it in your browser

These constraints keep the project small, fast, and working on every laptop.

---

## 🎯 Pick a theme (or bring your own idea)

| | Idea | Must-have features |
|---|---|---|
| 🧠 | **Lecture Quiz**: a quiz about a topic of your choice | 10 multiple-choice questions, score, timer per question, high score |
| 🃏 | **Flashcard Trainer** for your next exam | Flip cards, "I knew it / I didn't", repeat the ones you didn't know |
| 🍝 | **Mensa Roulette**: can't decide what to eat? | List of meals with prices, budget filter, spin animation |
| 🍅 | **Pomodoro Study Timer** | 25/5 min timer, session counter, sound at the end, daily stats |
| 🧹 | **Flat-share Cleaning Rota** | Add flatmates and tasks, fair weekly rotation, "done" checkboxes |
| 💸 | **Split the Bill** for your trip | Add people and expenses, show who owes whom |
| 🎱 | **Lecture Bingo** | Random 5×5 board from buzzwords, click to mark, detect BINGO |

---

## 🗺️ Level 1: Plan (≈ 7 min), Plan mode

Switch to **Plan** mode (dropdown or ⌘/Ctrl + .), then send something like:

```
I want to build a [Lecture Quiz about the history of computers] as a web app.
Constraints: one single index.html file with HTML, CSS and plain JavaScript.
No frameworks, no libraries, no CDN links. It must work by double-clicking the file.
Must-have features: [10 multiple-choice questions, score, 15-second timer per question,
high score saved in localStorage].
Before planning, ask me up to 3 clarifying questions. Then write the plan to PLAN.md.
```

✅ **Done when:** `PLAN.md` exists and you have **read it**. Not happy with it? Tell Bob what to change.

> 🤔 *Why plan first?* An agent that plans before it codes makes fewer wrong assumptions. And you can fix a plan much more cheaply than you can fix code.

## 🛠️ Level 2: Build (≈ 10 min), Agent mode

Switch to **Agent** mode:

```
Implement @/PLAN.md. Keep everything in index.html.
When you are done, tell me how to test the main features.
```

- Watch what Bob does. **Read each proposed change before you approve it.**
- Open `index.html` in your browser (double-click it in your file explorer) and try it out.

✅ **Done when:** your app opens in the browser and the main feature works.

## 🔁 Level 3: Iterate (≈ 8 min), Agent mode

Add **2–3 features, one prompt per feature.** Pick from the menu or invent your own:

- 🌙 Dark-mode toggle that remembers the choice
- 📱 Works nicely on a phone screen
- 🔊 Sound effects generated with the Web Audio API (no audio files)
- ⌨️ Keyboard shortcuts (e.g. 1–4 to answer, Space to continue)
- 🎉 Confetti animation on success, drawn on a canvas, no library
- 📊 Statistics screen (e.g. history of the last 10 rounds)
- 🌍 Language switch English/German

Found a bug? Describe it like a pro:

```
Bug: when I click "Next" after the last question, nothing happens.
Expected: a results screen with my score and the high score.
Steps: start quiz, answer all 10 questions, click "Next".
```

> 💡 If the browser shows an error, open the developer console (F12 or ⌘+⌥+I), copy the red error message and paste it into the chat.

## 🔍 Level 4: Quality (≈ 5 min), Ask mode → Agent mode

1. Switch to **Ask** mode and get a review:
   ```
   Review @/index.html for bugs, accessibility problems and security issues.
   List the findings as a table sorted by severity. Do not change any files.
   ```
2. Switch to **Agent** mode and fix the most important finding.
3. **Break it on purpose:** ask Bob for a crazy change ("make every button run away from the mouse"), look at the result, then use **Rollback** (hover over your message → rollback button) to undo it.

## ⭐ Level 5: Bonus

Finished? Go to [`../bonus-make-bob-yours`](../bonus-make-bob-yours/) and give Bob a personality and team rules.

---

## 🎤 Show & tell checklist (60 seconds)

- What did you build? Show it live.
- Which prompt worked surprisingly well?
- Where did Bob go wrong, and how did you get it back on track?
