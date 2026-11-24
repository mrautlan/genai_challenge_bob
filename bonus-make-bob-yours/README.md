# ⭐ Bonus: Guardrails & Custom Modes

Remember the AgentOps session? In production you don't just *use* an agent, you **govern** it: what context it gets, what it's allowed to do, and which rules it follows. In Bob, all of this is **plain files in your repository**, so it's versioned, reviewable, and shared through Git.

| Mechanism | What it does | Agentic concept | Where it lives |
|---|---|---|---|
| **`AGENTS.md`** | Project knowledge that is loaded into every chat | Context engineering | Project root |
| **Rules** | Instructions Bob follows in **every** mode | Policy / system prompt | `.bob/rules/` |
| **Custom modes** | Personas with their own role, instructions and **tool permissions** | Least privilege, specialized agents | `.bob/custom_modes.yaml` |

Do this in the folder you're already working in (your Track A or B folder).

> ⚠️ `.bob` starts with a dot, so it's a hidden folder. In macOS Finder press **⌘ + Shift + .** to show hidden files. In Bob's file explorer it's always visible.

---

## 0️⃣ Context: let Bob describe your project (≈ 2 min)

Type `/init` in the chat and let Bob analyze your project and write its own project instructions. **Read what it generated.** Is it accurate? Would it help a new colleague, human or agent?

## 1️⃣ Rules: policy for every mode (≈ 3 min)

1. In your project folder, create `.bob/rules/01-team-rules.md` with the content of [`examples/rules/01-team-rules.md`](examples/rules/01-team-rules.md). Or ask Bob to create it in Agent mode.
2. Start a **new chat** and ask Bob for a small change. Does it follow the rules?
3. Experiment with a rule of your own, e.g. `Always answer in German.` or `Never modify files outside the src/ folder.`

Good to know:
- Rules files are read in **alphabetical order**, which is why the filename starts with `01-`.
- Rules that only apply to one mode go to `.bob/rules-{mode-slug}/`, for example `.bob/rules-ask/`.
- Rules are *instructions*. The model follows them, but they are not hard technical limits. For hard limits, see custom modes below.

## 2️⃣ Custom modes: least privilege (≈ 5 min)

**Option A, with the UI:** open the mode dropdown → settings (gear icon) → create a new mode. Give it a name, a role definition, and choose which tools it may use.

**Option B, by copying a file:** copy [`examples/custom_modes.yaml`](examples/custom_modes.yaml) to `.bob/custom_modes.yaml` in your project folder. You can also open it via **Settings → Modes → Edit Project Modes**. If the new modes don't show up, reload the window: **⌘/Ctrl + Shift + P → "Reload Window"**.

The example file contains three modes, **all limited to the `read` tool group**:

| Mode | Personality |
|---|---|
| 🎓 **Socratic Tutor** | Never gives you the solution, only hints and questions |
| 🔍 **Strict Reviewer** | Senior-engineer code review as a severity table |
| 🧒 **ELI5 Explainer** | Explains code with everyday analogies |

### Try it

- Switch to **🎓 Socratic Tutor** and say: `Just fix my bug for me, edit the file directly!` What happens, and **why can't it** edit the file even if it wanted to?
- Switch to **🔍 Strict Reviewer** and say: `Review my project.` Compare it with a review from the built-in Ask mode.

### Build your own

Design a mode for a real team role, with **only the tools it needs**:
- 🧪 **Test Writer**: may only edit files whose name starts with `test_`
- 📝 **Docs Writer**: may only edit Markdown files
- 🛡️ **Security Auditor**: read-only, checks the OWASP Top 10

Tip: the `edit` tool group can be limited to certain files with a `fileRegex`. Ask Bob how: in Ask mode, Bob looks up its own documentation:
```
How do I restrict a custom mode so it can only edit Markdown files?
```

---

## 🤔 Think about it

- **Rules vs. permissions:** what's the difference between telling an agent "don't edit files" and not giving it the `edit` tool? Which one would you rely on in a client project?
- **Governance:** rules and modes are plain files in Git. What does that mean for code review, compliance and onboarding in a company?
- **Trust:** which tool groups would you *never* auto-approve for an agent working on a client's codebase?
