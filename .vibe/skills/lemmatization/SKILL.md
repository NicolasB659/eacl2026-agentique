---
name: lemmatization
description: Produce historical-language lemmas using EACL 2026 corpora and language-specific prompts.
---

# Historical Language Lemmatization

## Objective
Assign a canonical lemma to each input token while preserving
the conventions of the EACL 2026 annotation framework.

## Supported languages
- GRC: Ancient Greek
- HYE: Classical Armenian
- KAT: Old Georgian
- SYC: Syriac

## Resources
- `data/corpus/train/{LANG}_train.tsv`
- `data/corpus/test_in-domain/{LANG}_test.tsv`
- `data/corpus/test_out-of-domain/{LANG}_test.tsv`
- `data/prompt-templates/{LANG}-prompt-zero-shot_template.txt`
- `data/prompt-templates/{LANG}-prompt-few-shot-{N}_template.txt`

N may be 5, 50 or 500.

## Procedure
1. Identify the language, dataset partition and experimental setting.
2. Load the matching prompt template.
3. Read the TSV header and verify the expected columns.
4. Extract input tokens from the `form` column.
5. Exclude the header and all gold-standard `lemma` and `pos` values.
6. Preserve token order, duplicates and Unicode characters.
7. Use training examples only when required by the few-shot setting.
8. Generate one lemma annotation for each input token.
9. Preserve composite lemma conventions using `@`.
10. Return predictions in a TSV-compatible format.

## Prompt compatibility
The current `scripts/main.py` uses the placeholders
`${HYE_test}` and `${HYE_tagset}` for all languages.

Do not rename these placeholders without updating the Python code.

## Constraints
- Never use test reference annotations during prediction.
- Never invent missing training examples.
- Never modify original corpus files.
- Report uncertain or ambiguous lemmas.
- Do not claim successful annotation without actual model output.

## Output
Produce a three-column TSV-compatible annotation:
`token`, `lemma`, `POS tag`.

For a lemma-only task, leave the POS field explicitly
unassigned rather than inventing a grammatical label.
