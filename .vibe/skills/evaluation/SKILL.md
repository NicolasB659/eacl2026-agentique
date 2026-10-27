---
name: evaluation
description: Evaluate historical language lemmatization and POS-tagging against gold-standard annotations.
user-invocable: true
---

# Historical NLP Evaluation

## Objective
Measure the quality of predicted linguistic annotations.

## Procedure
1. Load predicted annotations and gold-standard data.
2. Verify that tokens are correctly aligned.
3. Calculate exact-match lemma accuracy.
4. Calculate POS-tagging accuracy.
5. Report results separately for each language.
6. Distinguish in-domain and out-of-domain results.
7. Compare zero-shot and few-shot settings when available.

## Constraints
- Never invent evaluation scores.
- Do not evaluate without reference annotations.
- Report alignment problems and missing data.
- Document the number of evaluated tokens.
