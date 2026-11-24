# 🅱️ Track B: Legacy Rescue

> *"DO NOT TOUCH - it works!!!"* (a comment in `grades.py`, 2014)

**The story:** The *Intro to Programming* course still computes its final grades with `grades.py`, a script a tutor wrote in 2014. This semester several students complained that their grade is wrong. Nobody understands the code anymore, and it has no tests and no documentation.

**Your mission:** Use Bob to **understand** the code, build a **safety net of tests**, **find and fix the bugs**, and **modernize** the code. This is exactly the kind of work Bob was built for in companies: understanding and modernizing code that nobody wants to touch.

**The twist:** in the end, you have to decide whether you **trust** the result. Bob explains the code, Bob writes the tests, Bob fixes the bugs. Who checks Bob? *(Spoiler for next week's session on trustworthiness: you do.)*

Requirements: Python 3.8+. Run the script with:

```bash
python3 grades.py            # macOS / Linux
py grades.py                 # Windows
```

| File | What it is |
|---|---|
| `grades.py` | The legacy script (don't read the code yourself first, let Bob explain it!) |
| `students.csv` | Points of 15 students |
| `README.md` | This file, including **the official grading rules** (below) |

> ✍️ **How to use this page:** each level has a goal and a *"done when"*. **Write your own prompts first.** If you're stuck, open the 💡 example.

---

## 📜 The official grading rules (the "specification")

These rules come from the examination regulations. **They are the truth.** If the code does something different, the code is wrong.

**Input:** `students.csv` with the columns `id, name, exam, assignments, bonus`

| # | Rule |
|---|---|
| R1 | **Exam** points range from 0–100. **Assignment** points range from 0–50. **Bonus** points range from 0–10. A missing or empty value counts as **0**. |
| R2 | Bonus points are added to the exam points. **Exam + bonus can never exceed 100.** |
| R3 | Exam % = (exam + bonus, capped at 100) / 100 × 100. Assignments % = assignments / 50 × 100. |
| R4 | **Total score** = 60 % × exam % + 40 % × assignments %, **rounded to one decimal**. |
| R5 | **Exam requirement:** if exam % (including bonus) is **below 50**, the grade is **5.0** (fail), no matter how high the total score is. |
| R6 | Grade table. The thresholds are **inclusive**, so a total of exactly 80.0 gets a 2.0. |
| R7 | Output: one line per student, **sorted by name**, then: number of students, **pass rate** (grade ≤ 4.0), **average grade of the students who passed** (rounded to 2 decimals), and the **best student** (on a tie: the first by name). |

**R6 grade table:**

| Total score ≥ | 95 | 90 | 85 | 80 | 75 | 70 | 65 | 60 | 55 | 50 | below 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Grade** | 1.0 | 1.3 | 1.7 | 2.0 | 2.3 | 2.7 | 3.0 | 3.3 | 3.7 | 4.0 | 5.0 |

---

## 🔎 Level 1: Understand (≈ 5 min), Ask mode → Plan mode

**Goal:** understand what `grades.py` does without reading it line by line yourself. Then let Bob document it in `CODE_OVERVIEW.md`, including a Mermaid flowchart. Plan mode can write Markdown.

✅ **Done when:** you can explain in two sentences what `calc`, `g` and `doit` do.

<details>
<summary>💡 Stuck? Example prompts</summary>

Ask mode:
```
Explain @/grades.py to me like I'm a new developer on the team:
what does it do, step by step, and what are the inputs and outputs?
Then list everything about the code quality that would worry you.
```
Plan mode:
```
Write a file CODE_OVERVIEW.md that documents how @/grades.py works,
including a Mermaid flowchart of the main steps.
```
</details>

## 🛡️ Level 2: Safety net (≈ 10 min), Agent mode

**Goal:** write unit tests with Python's built-in `unittest` (no pip installs). Write **at least one test per rule R1–R7**, including edge cases such as scores exactly on a grade threshold. The tests must check the **specification, not what the code currently does.** **Don't fix anything yet!**

> 🤔 Bob may need to change something small so that `grades.py` can be imported in tests. Ask it to explain why before you approve.

✅ **Done when:** you have tests, and some of them **fail**. Every failing test is a suspect.

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Write unit tests with Python's built-in unittest module (no pip installs)
in a new file test_grades.py. Write at least one test per rule R1–R7 from @/README.md,
including edge cases like scores exactly on a grade threshold.
The tests must check the SPECIFICATION, not what the code currently does.
Do not change grades.py yet. Then run the tests and summarize which ones fail.
```
</details>

## 🐛 Level 3: Bug hunt (≈ 10 min), Agent mode

**There are several bugs in this script.** Fix them **one at a time**: understand the root cause first, then fix, then re-run all tests.

🕵️ **Verify like a professional:** pick one affected student from `students.csv` and **calculate their grade by hand** using the rules. Does it match the new output? Don't just trust Bob, and don't just trust the tests either. Bob wrote them too!

**Bug scoreboard** (post your count in the chat, e.g. `B3 ✅ 3 bugs`):

| # | Bug (which rule is violated?) | Which student was affected? |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Look at the first failing test. Explain the root cause in grades.py,
then fix only that bug and run all tests again.
```
</details>

## ✨ Level 4: Modernize (≈ 5 min), Agent mode

**Goal:** turn `grades.py` into clean, modern Python: descriptive names, small functions, type hints, docstrings, constants instead of magic numbers, no global variables, proper error handling, and an `if __name__ == "__main__"` block. **The output format stays exactly the same.**

✅ **Done when:** the code is readable **and all tests are still green**.

<details>
<summary>💡 Stuck? Example prompt</summary>

```
Refactor grades.py into clean, modern Python: descriptive names, small functions,
type hints, docstrings, constants instead of magic numbers, no global variables,
proper error handling and an if __name__ == "__main__" block.
The output format must stay exactly the same. Run the tests after refactoring.
```
</details>

## ⭐ Level 5: Bonus, "Who tests the tester?"

Your tests were written by an AI. Are they any good? Run a small **mutation test**:

1. Start a **new chat** in Agent mode. Ask Bob to introduce **one subtle bug** into `grades.py` that violates one of the rules, **without telling you where**.
2. Run your tests. **Do they catch it?** If they don't, your safety net has a hole. Let Bob add the missing test.
3. Undo the planted bug with **Rollback**.

Other options:
- Add a `--csv results.csv` export option (with `argparse`).
- Go to [`../bonus-make-bob-yours`](../bonus-make-bob-yours/) and build a "Strict Reviewer" mode that may only *read*.

---

## 🎤 Show & tell (if you volunteer: share your screen, 60 seconds)

- How many bugs did you find? Which one was the sneakiest?
- Show a test that caught a bug, or a bug your tests missed.
- Did Bob ever claim something that wasn't true? How did you notice?
