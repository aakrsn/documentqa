---
name: coding-guidelines
description: Coding guidelines for writing simple, readable code that matches the request. Use whenever writing, editing, reviewing or refactoring code, to avoid over-engineering, scope creep, unclear names, noisy comments and silent assumptions.
---

# Coding Guidelines

**Tradeoff:** These guidelines bias toward caution and simplicity over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them. Don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features, options or configurability beyond what was asked.
- No abstractions for single-use code: no base classes, factories, registries, wrappers, compatibility shims or helpers with one caller.
- No error handling for impossible scenarios. Handle real failures, with an error message that says what went wrong.
- Don't create new files when an existing one is the natural place.
- Functions do one thing and read top to bottom.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

- Don't "improve" adjacent code, comments or formatting, and don't refactor what isn't broken.
- Match existing style, even if you'd do it differently. Flag it when you need to use a different style.
- If you notice unrelated dead code, mention it. Don't delete it unless the task is a cleanup.
- Remove imports, variables and functions that your changes made unused.
- Never comment out code. Delete it; version control keeps the history.

The test: Every changed line should trace directly to the user's request.

## 4. Naming

**A name says what the thing is in this use case.**

- Variables and functions: `snake_case`. Classes: `PascalCase`.
- Functions are verbs (`extract_text`), classes are nouns (`PdfHandler`).
- Use names from the problem domain: `routing_number`, `invoice_total`. Avoid vague names: `data`, `info`, `temp`, `obj`, `manager`, `helper`, `util`. No type prefixes (`str_name`) and no abbreviations a reader has to decode.
- No name may start or end with an underscore. This applies to every name: variables, functions, methods, classes, modules and loop variables. Even a value you don't use gets a real name that says what it is. The only exceptions are names the language requires, such as `__init__`, `__name__` and `__init__.py`.

  | Bad | Good |
  |---|---|
  | `for _ in rows:` | `for row in rows:` |
  | `code, _ = pair` | `code, description = pair` |
  | `def _table_lines(self):` | `def table_lines(self):` |
  | `_cache = {}` | `cache = {}` |
  | `class_ = "A"` | `class_name = "A"` |

## 5. Comments

**A comment says what the code does now, in one short line. Never its history.**

- Prefer clear names over comments. Add a comment only where the code alone doesn't say why.
- Comments and docstrings are one line.
- No history, dates, measurements or "changed from X", and no comments that restate the code.

```python
# Bad
# Changed on 2026-09-24 after the run showed 2,769 false hits; we now also check the cell.
# Loop over the rows

# Good
# A lone ".0" is how spreadsheets print whole numbers.
```

## 6. House Rules

- Imports at the top of the file.
- Python: no relative imports (`from .base import X`). Use bare module names; if needed, add the directory to `sys.path` once, in the package `__init__.py` or the test file.
- Program inputs: plain constants in a `config.py` next to the script, not an `argparse` CLI. `.env` holds secrets only.
- Tests live in separate test files, never inside the source code.

## 7. Goal-Driven Execution

**Define success criteria. Loop until verified.**

- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a short plan with a check for each step.
