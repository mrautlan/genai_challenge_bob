# 🤖 IBM Bob Hands-on Challenge

**45 minutes · solo · remote**

You've learned the concepts: agent loops, tools, RAG, prompt engineering, AgentOps. Now you'll work with a production coding agent yourself. [IBM Bob](https://bob.ibm.com) **plans, edits files, runs commands, and checks its own work**, and you stay in charge of every step.

📄 **Keep the handout open while you work:** [`handout/IBM-Bob-Handout.pdf`](handout/IBM-Bob-Handout.pdf). It maps the concepts to Bob and covers prompting for coding agents, a prompt cheat sheet, and troubleshooting.

---

## 🔗 How today builds on the previous sessions

| Session | Where you'll meet it today |
|---|---|
| Intro Agentic AI for Business | Bob as a "digital colleague" for software work |
| IBM Design Thinking | Track A starts with a *"How might we…"* problem statement, which Bob turns into a spec |
| Agentic Systems | Bob's loop: plan → tool call (read, edit, run) → observe → repeat. Modes, to-dos, subagents |
| RAG & Prompt Engineering | Context engineering: `@` mentions, rules, `AGENTS.md`, Bob looking up its own docs |
| Best Practices, AgentOps & Open Source | Human-in-the-loop approvals, least-privilege modes, rollback, rules as policy |
| *Next: Client Selling & Trustworthiness* | Track B: how do you **verify** an agent's work before you trust it? |

## ✅ 1. Setup (ideally while the talk is running)

| Step | What to do |
|---|---|
| 1 | **Create an IBMid** (free): <https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776> |
| 2 | **Start the free trial** (50 Bobcoins for 30 days): <https://bob.ibm.com/trial> |
| 3 | **Install Bob IDE**: <https://bob.ibm.com/download>. On a Mac, choose *mac-ARM* for Apple silicon (M1–M4) or *mac-Intel*. On Windows, use the `.exe`. |
| 4 | **Start Bob and sign in** with your IBMid (a browser window opens). |
| 5 | **Get this repository:** click the green **Code → Download ZIP** button on GitHub and unzip it, *or* run `git clone https://github.com/mrautlan/genai_challenge_bob.git` |

## 📂 2. Open ONE track folder in Bob

In Bob, use **File → Open Folder…** and open **only the folder of your track**, not the whole repository. Bob's context is the folder you open, so keep it focused.

## 🛤️ 3. Choose your track

| | Track | You will… | Good for |
|---|---|---|---|
| 🅰️ | [**Build a Prototype**](track-a-build-an-app/) | Go from a problem statement to a working web prototype, such as an ROI calculator for a client or a readiness check | Everyone, no coding experience needed |
| 🅱️ | [**Legacy Rescue**](track-b-legacy-rescue/) | Understand, test, debug and modernize a messy 2014 grading script, and find out whether you can trust the agent's fixes | Anyone who can read a bit of Python (needs Python 3.8+) |
| ⭐ | [**Bonus: Guardrails & Custom Modes**](bonus-make-bob-yours/) | Give Bob team rules and build your own least-privilege mode | Anyone who finishes early |

Each track has **levels**. Write your own prompts first. If you're stuck, open the 💡 example prompt. Get as far as you can.

## ⏱️ 4. Schedule

| Time | What |
|---|---|
| 0–5 min | Setup check, open your track folder, first prompt |
| 5–35 min | Work through the levels of your track |
| 35–40 min | ⭐ Bonus level, or polish your result |
| 40–45 min | 🎤 **Show & tell**: 2–3 volunteers share their screen (60 seconds each) |

## 💬 5. Working remotely

- **Put the call and Bob side by side**, or use two screens.
- **Post your progress in the chat** when you finish a level, e.g. `A2 ✅` or `B3 ✅ 3 bugs`. That way the host sees where everyone is.
- **Stuck for more than 3 minutes?** Ask Bob first (Ask mode). If that doesn't help, post your question with a screenshot in the chat.
- **Proud of your result?** Volunteer for show & tell.

## 🧠 6. Bob in 60 seconds

Bob has **three modes**. Switch with the dropdown left of the chat input or **⌘ + .** (Mac) / **Ctrl + .** (Windows/Linux).

| Mode | Use it to… | Can it change files? |
|---|---|---|
| 💬 **Ask** | Understand code, ask questions, get reviews | ❌ No (read-only) |
| 🗺️ **Plan** | Clarify, design, and write a spec or plan | Only Markdown/text files |
| 🛠️ **Agent** | Build: create and edit files, run commands | ✅ Yes |

- **Approvals:** Bob asks before it edits a file or runs a command. **Read before you click *Approve*.**
- **Rollback:** made a mess? Hover over one of *your* earlier messages and click the rollback button to restore the files.
- **Context:** type `@` in the chat to point Bob at things: `@/index.html`, `@problems`, `@terminal`.

## 🏆 Rules of the game

1. **Small steps.** One feature or one question per prompt.
2. **You are the pilot.** Bob proposes, you decide. Keep auto-approve **off** today, so you see every tool call.
3. **Trust, but verify.** Run it, click through it, check the numbers.
4. **Save Bobcoins.** Start a new chat for a new topic. If Bob fails twice, stop and rethink instead of retrying.
5. **Break things.** That's what Rollback is for.

---

<sub>Material for a university webinar series on agentic AI. Bob documentation: <https://bob.ibm.com/docs/ide></sub>
