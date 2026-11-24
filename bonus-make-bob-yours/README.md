# ⭐ Bonus: Make Bob Yours

An AI agent's behaviour isn't magic, and you can configure it. In companies, teams use this to share coding standards and specialized "personas" through Git. You'll try two mechanisms:

| Mechanism | What it does | Where it lives |
|---|---|---|
| **Rules** | Instructions Bob follows in **every** mode | `.bob/rules/` in your project folder |
| **Custom modes** | New "personas" with their own role, instructions and **tool permissions** | `.bob/custom_modes.yaml` in your project folder |

Do this in the folder you're already working in (your Track A or B folder).

> ⚠️ `.bob` starts with a dot, so it's a hidden folder. In macOS Finder press **⌘ + Shift + .** to show hidden files. In Bob's file explorer it's always visible.

---

## 1️⃣ Rules (≈ 3 min)

1. In your project folder, create the file `.bob/rules/01-team-rules.md`. Or let Bob do it in Agent mode:
   ```
   Create the file .bob/rules/01-team-rules.md with the content of
   the file I paste below. [paste the content of examples/rules/01-team-rules.md]
   ```
2. Start a **new chat** and ask Bob for a small change. Does it follow the rules?
3. Experiment: add a rule like `Always answer in German.` or `End every answer with a fun fact about computer history.` and see what happens.

👉 Example: [`examples/rules/01-team-rules.md`](examples/rules/01-team-rules.md)

Good to know:
- Rules files are read in **alphabetical order**, which is why the filename starts with `01-`.
- Rules that only apply to one mode go to `.bob/rules-{mode-slug}/`, for example `.bob/rules-ask/`.
- A file named `AGENTS.md` in the root of your project is also loaded automatically.

## 2️⃣ Custom modes (≈ 5 min)

**Option A, with the UI:** open the mode dropdown → settings (gear icon) → create a new mode. Give it a name, a role definition, and choose which tools it may use.

**Option B, by copying a file:** copy [`examples/custom_modes.yaml`](examples/custom_modes.yaml) to `.bob/custom_modes.yaml` in your project folder. You can also open it via **Settings → Modes → Edit Project Modes**. If the new modes don't show up, reload the window: **⌘/Ctrl + Shift + P → "Reload Window"**.

The example file contains three modes:

| Mode | Personality | Tools |
|---|---|---|
| 🎓 **Socratic Tutor** | Never gives you the solution, only hints and questions | read only |
| 🔍 **Strict Reviewer** | Senior-engineer code review as a severity table | read only |
| 🧒 **ELI5 Explainer** | Explains code with everyday analogies | read only |

### Try it

- Switch to **🎓 Socratic Tutor** and say: `Just fix my bug for me!` Does it refuse? Does it help anyway?
- Switch to **🔍 Strict Reviewer** and say: `Review my project.`
- Ask the **same question** in *Ask* mode and in *ELI5 Explainer*. What's different?

### Build your own

Invent a mode. A few ideas:
- 🧪 **Test Writer**: may only edit files whose name starts with `test_`
- 📝 **Docs Writer**: may only edit Markdown files
- 🏴‍☠️ **Pirate Pair Programmer**: because why not

Tip: in YAML, the `edit` tool group can be limited to certain files with a `fileRegex`. Ask Bob how: in Ask mode, Bob looks up its own documentation:
```
How do I restrict a custom mode so it can only edit Markdown files?
```

---

## 🤔 Think about it

- Why does the Socratic Tutor only get the `read` tool group, and not just the instruction "don't edit files"?
- Rules and modes are plain files. What happens when a team commits them to Git?
