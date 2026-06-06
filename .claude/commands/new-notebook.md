---
description: Create a new educational Jupyter notebook in docs/notebooks that teaches a topic — intuition, math, runnable examples, applications.
argument-hint: <topic> [optional: target subfolder, e.g. statistics | machine learning | finance | PDEs | LLM]
allowed-tools: Bash, Read, Write, Glob, Grep
---

# Create an educational notebook: $ARGUMENTS

You are building a self-contained teaching notebook that explains a topic to a smart reader who is new to it. The goal is **understanding**, not just code: intuition first, then the math, then runnable examples, then where it's used in the real world.

Work through these steps in order. Stop and ask the user only if a genuine choice can't be resolved from the repo or sensible defaults.

## 1. Pick the topic and location

- The topic is the user's argument. If it's empty, ask what to cover.
- Notebooks live under `docs/notebooks/<subfolder>/`. List existing subfolders with `ls docs/notebooks/` and choose the best fit (e.g. `statistics`, `machine learning`, `finance`, `PDEs`, `LLM`). If the user named a subfolder, use it. If none fits well, create a new clearly-named one.
- Choose a filename matching the existing convention in that folder (inspect a couple of neighbours first — names are typically lowercase with a `_00` / ` - 00` numeric suffix). Pick the next free number.

## 2. Match the house style

- Read one existing notebook in the chosen folder to copy its `metadata` block verbatim (kernelspec, language_info) and its markdown/LaTeX conventions.
- Note: LaTeX in markdown cells uses `$ ... $` / `$$ ... $$`. Tables, headings, and prose are GitHub-flavored markdown.

## 3. Design the content

A strong notebook has this arc — adapt the count to the topic, but cover every beat:

1. **Title + one-line hook** — the single question the topic answers.
2. **Intuition first, no equations** — an analogy or mental picture.
3. **Why it matters** — significance + a table of real-world applications/domains.
4. **The math, built up** — define symbols in a table; derive or state the key equations with `$$`. Explain *why*, don't just dump formulas.
5. **A minimal runnable example** — the simplest case, in NumPy/standard libs, with a plot. Use a fixed RNG seed for reproducibility.
6. **A richer, realistic example** — show the technique doing something genuinely useful; quantify the result (e.g. error reduction).
7. **A visualisation of the key internal quantity** — make the mechanism visible.
8. **The deeper view** — connect to broader theory (Bayesian, optimisation, etc.) and state any optimality/guarantees.
9. **Variants / extensions** — a table of how the idea generalises.
10. **Practical gotchas** — tuning, pitfalls, numerical issues.
11. **Takeaways** — a numbered summary + suggested next steps to explore.

Code must be **correct and runnable end to end**, self-contained (imports at the top), and use only libraries reasonably available (numpy, matplotlib, scipy, pandas). Prefer implementing the core idea from scratch over calling a black-box library — the point is to teach.

## 4. Write the notebook

- Generate valid `nbformat` v4 JSON. The robust way: write a small Python builder script to `/tmp` that assembles markdown/code cells and `json.dump`s the notebook, then run it. This avoids hand-writing fragile JSON.
- Code cells: `"outputs": []`, `"execution_count": null`. Markdown cells: split `source` into a list of strings keeping newlines.
- Save to the path chosen in step 1.

## 5. Verify before claiming done

- Confirm the file is valid JSON (`python -c "import json; json.load(open(PATH))"`), and if `nbformat` is importable, validate with it.
- **Execute the code** to prove it runs: either run the notebook headless if `jupyter`/`nbconvert` is available (`jupyter nbconvert --to notebook --execute --inplace PATH`), or extract and run the code cells' logic in a plain `python -` heredoc. Report the actual numeric results.
- If anything errors, fix it and re-verify. Report outcomes faithfully — never claim it runs if you didn't run it.

## 6. Report

Summarise: the file path (as a clickable link), the section arc, the key result the examples demonstrate, and 1–2 suggested follow-on notebooks.
