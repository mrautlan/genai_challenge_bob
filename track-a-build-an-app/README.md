# 🅰️ Track A: Build a Prototype

**Mission:** In about 30 minutes, go from a **problem statement** to a **working, clickable prototype**, without writing the code yourself. You are the product owner, Bob is your development team.

### The constraints (tell Bob about them!)

- Everything in **one single `index.html` file** (HTML + CSS + plain JavaScript)
- **No frameworks, no libraries, no CDN links, no installs, no API keys**
- You run it by **double-clicking `index.html`**, which opens it in your browser

These constraints keep the prototype small, fast, and working on every laptop.

> ✍️ **How to use this page:** each level has a goal and a *"done when"*. **Write your own prompts.** You've had the prompt engineering session 😉. If you're stuck, open the 💡 example.

---

## 🎯 Pick a theme (or bring your own idea)

**💼 Business prototypes**

| | Idea | Core features |
|---|---|---|
| 💰 | **AI Use-Case ROI Calculator** for a client meeting | Inputs (hours saved, hourly rate, licence cost) → yearly savings, payback period, bar chart drawn on a `<canvas>` |
| 🧭 | **Agentic AI Readiness Check** for clients | 10-question self-assessment, score per dimension (data, process, people, governance), radar chart, recommendations |
| ⏱️ | **Meeting Cost Ticker** | Participants × hourly rate → live cost counter, "this meeting could have been an e-mail" alert |
| 📋 | **Client Feedback Board** | Add, filter and sort feedback, tag the sentiment, summary stats, export as CSV |

**🎓 Campus life**

| | Idea | Core features |
|---|---|---|
| 🧠 | **Webinar Quiz** about this series (agentic systems, RAG, AgentOps…) | 10 multiple-choice questions, score, timer, high score |
| 🃏 | **Flashcard Trainer** for your next exam | Flip cards, "I knew it / I didn't", repeat the ones you didn't know |
| 🍝 | **Mensa Roulette** | List of meals with prices, budget filter, spin animation |
| 💸 | **Split the Bill** for a trip | Add people and expenses, show who owes whom |

---

## 🧩 Level 0: Problem statement (≈ 2 min), Design Thinking

Before you talk to Bob, write **one sentence**:

> **How might we** help **[persona]** to **[need]**, so that **[benefit]**?

*Example: "How might we help an IBM consultant estimate the ROI of an AI use case live in a client meeting, so that the client sees the business value in under two minutes?"*

## 🗺️ Level 1: Spec (≈ 7 min), Plan mode

**Goal:** Bob turns your problem statement into a spec in `PLAN.md`: user stories, must-have and nice-to-have features, a rough UI layout, implementation steps, and acceptance criteria. Bob should **ask you clarifying questions first**.

✅ **Done when:** `PLAN.md` exists and you have **reviewed and adjusted it**. From now on it's the contract between you and Bob.

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Problem statement: How might we help [persona] to [need], so that [benefit]?

I want to build a prototype for this: [ROI calculator for AI use cases].
Constraints: one single index.html file with HTML, CSS and plain JavaScript.
No frameworks, libraries, CDN links or API keys. It must work by double-clicking the file.

Before planning, ask me up to 3 clarifying questions. Then write PLAN.md with:
user stories, must-have vs. nice-to-have features, a rough UI layout,
implementation steps and acceptance criteria.
```
</details>

> 🤔 *Why spec first?* A plan is a cheap artifact to correct, and it becomes context for every later step. This is spec-driven development.

## 🛠️ Level 2: Build (≈ 8 min), Agent mode

**Goal:** implement the **must-haves** from `PLAN.md`.

👀 **Watch the agent loop:** which files does Bob read? Which tool calls does it make? Does it keep a to-do list? Where does it stop and ask for approval?

Open `index.html` in your browser (double-click it in your file explorer) and try it out.

✅ **Done when:** your prototype opens in the browser and the core flow works.

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Implement the must-have features from @/PLAN.md. Keep everything in index.html.
Work through the implementation steps in order.
When you are done, tell me how to test each acceptance criterion.
```
</details>

## 🔁 Level 3: Iterate (≈ 8 min), Agent mode

**Goal:** add **2–3 features, one prompt per feature.** Pick from the menu or invent your own:

- 📤 Export results as CSV, or a print-friendly "client summary" view
- 💾 Save state in `localStorage` so nothing is lost on reload
- 🌙 Dark-mode toggle that remembers the choice
- 📱 Works nicely on a phone screen
- ⌨️ Keyboard shortcuts
- 🎉 Confetti on success, drawn on a canvas, no library
- 🌍 Language switch English/German

Found a bug? Report it like a pro: **steps → expected → actual → error message.** If the browser shows an error, open the developer console (F12 or ⌘+⌥+I) and paste the red message into the chat.

<details>
<summary>💡 Stuck? Example bug report</summary>

```
Bug: after I change the hourly rate, the chart does not update.
Steps: enter 10 hours saved, rate 80, click "Calculate", change the rate to 100.
Expected: the chart and the payback period update immediately.
Actual: only the number updates, the chart stays the same.
Explain the root cause before you fix it.
```
</details>

## 🔍 Level 4: Trust, but verify (≈ 5 min), Ask mode → Agent mode

1. **Independent review:** start a **new chat** in **Ask** mode, so Bob doesn't carry over its own assumptions, and get a review of `index.html` covering bugs, accessibility and security, sorted by severity.
2. **Check the acceptance criteria yourself:** go through the acceptance criteria in `PLAN.md` by hand. Does the prototype really pass all of them? Business prototypes: check at least one calculation with a pocket calculator.
3. Switch to **Agent** mode and fix the most important finding.
4. **Break it on purpose:** ask for a crazy change ("make every button run away from the mouse"), look at the result, then use **Rollback** (hover over your message → rollback button) to undo it.

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Review @/index.html for bugs, accessibility problems and security issues.
Also check it against the acceptance criteria in @/PLAN.md.
List the findings as a table sorted by severity. Do not change any files.
```
</details>

## ⭐ Level 5: Bonus

Finished? Go to [`../bonus-make-bob-yours`](../bonus-make-bob-yours/) and add guardrails: team rules and your own least-privilege mode.

---

## 🎤 Show & tell (if you volunteer: share your screen, 60 seconds)

- Your problem statement, plus a live demo
- One prompt that worked surprisingly well
- One moment where Bob went wrong, and how you got it back on track
