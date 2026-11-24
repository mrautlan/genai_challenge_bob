# 🤖 IBM Bob Hands-on Challenge

**45 minutes. You, a teammate, and an AI coding agent.**

In this session you'll build real software with [IBM Bob](https://bob.ibm.com), an AI development partner that doesn't just autocomplete code. It **plans, edits files, runs commands, and checks its own work**, and you stay in charge of every step.

📄 **Keep the handout open while you work:** [`handout/IBM-Bob-Handout.pdf`](handout/IBM-Bob-Handout.pdf). It covers modes, prompting, and copy-paste prompts.

---

## ✅ 1. Setup (do this first, ~5 min)

| Step | What to do |
|---|---|
| 1 | **Create an IBMid** (free): <https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776> |
| 2 | **Start the free trial** (50 Bobcoins for 30 days): <https://bob.ibm.com/trial> |
| 3 | **Install Bob IDE**: <https://bob.ibm.com/download>. On a Mac, choose *mac-ARM* for Apple silicon (M1–M4) or *mac-Intel*. On Windows, use the `.exe`. |
| 4 | **Start Bob and sign in** with your IBMid (a browser window opens). |
| 5 | **Get this repository:** click the green **Code → Download ZIP** button on GitHub and unzip it, *or* run `git clone https://github.com/mrautlan/genai_challenge_bob.git` |

> 💡 **Work in pairs.** One person drives, one person reads and challenges what Bob proposes. Switch roles after each level.

## 📂 2. Open ONE track folder in Bob

In Bob, use **File → Open Folder…** and open **only the folder of your track**, not the whole repository. That way Bob sees only what it needs.

## 🛤️ 3. Choose your track

| | Track | You will… | Good for |
|---|---|---|---|
| 🅰️ | [**Build an App**](track-a-build-an-app/) | Go from an idea to a working web app (quiz, flashcards, study timer…) | Everyone, no coding experience needed |
| 🅱️ | [**Legacy Rescue**](track-b-legacy-rescue/) | Understand, test, debug and modernize a messy 2014 grading script | People who know a bit of Python (needs Python 3.8+) |
| ⭐ | [**Bonus: Make Bob Yours**](bonus-make-bob-yours/) | Create your own Bob mode and rules | Anyone who finishes early |

Each track has **levels**. You don't have to finish all of them; get as far as you can.

## ⏱️ 4. Schedule

| Time | What |
|---|---|
| 0–5 min | Setup check, open your track folder, first prompt |
| 5–35 min | Work through the levels of your track |
| 35–40 min | ⭐ Bonus level, or polish your result |
| 40–45 min | 🎤 **Show & tell**: 2–3 teams show what they built (60 seconds each) |

## 🧠 5. Bob in 60 seconds

Bob has **three modes**. Switch with the dropdown left of the chat input or **⌘ + .** (Mac) / **Ctrl + .** (Windows/Linux).

| Mode | Use it to… | Can it change files? |
|---|---|---|
| 💬 **Ask** | Understand code, ask questions, get reviews | ❌ No (read-only) |
| 🗺️ **Plan** | Think before building: ask questions, write a plan | Only Markdown/text files |
| 🛠️ **Agent** | Build: create and edit files, run commands | ✅ Yes |

- **Approvals:** Bob asks before it edits a file or runs a command. **Read before you click *Approve*.**
- **Rollback:** made a mess? Hover over one of *your* earlier messages and click the rollback button to restore the files.
- **Context:** type `@` in the chat to point Bob at things: `@/index.html`, `@problems`, `@terminal`.

## 🏆 Rules of the game

1. **Small steps.** One feature or one question per prompt.
2. **You are the pilot.** Bob proposes, you decide. Keep auto-approve **off** today.
3. **Trust, but verify.** Run it, click through it, check the numbers.
4. **Save Bobcoins.** Start a new chat for a new topic, and don't ask for "everything at once".
5. **Have fun and break things.** That's what Rollback is for.

---

<sub>Material for a university hands-on session about IBM Bob. Bob documentation: <https://bob.ibm.com/docs/ide></sub>
