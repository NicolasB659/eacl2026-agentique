---
name: pos-tagging
description: Assign language-specific POS tags to historical texts using EACL 2026 tagsets and prompts.
---

# Historical Language POS Tagging

## Objective
Assign a part-of-speech tag to every input token using
the annotation conventions of the EACL 2026 project.

## Supported languages
- GRC: Ancient Greek
- HYE: Classical Armenian
- KAT: Old Georgian
- SYC: Syriac

## Tagsets
- `data/tagsets/GRC_tagset.txt`
- `data/tagsets/HYE_tagset.txt`
- `data/tagsets/KAT_tagset.txt`
- `data/tagsets/SYC_tagset.txt`

## Procedure
1. Identify the requested language.
2. Load the corresponding language-specific tagset.
3. Select the appropriate zero-shot or few-shot prompt.
4. Verify the TSV input structure.
5. Extract tokens from the `form` column.
6. Exclude gold-standard lemma and POS annotations.
7. Analyze each token in its linguistic context.
8. Assign only POS labels permitted by the tagset.
9. Preserve token order and Unicode characters.
10. Validate the output structure.

## Composite annotations
Some tokens may represent multiple linguistic units.

The EACL 2026 prompts use `@` to separate combined
lemmas and POS annotations.

Example:
token: ταὐτόν
lemma: ὁ@αὐτός
POS: DET@PRO+Dem

Preserve this convention when applicable.

## Scientific constraints
- Never invent POS labels.
- Never use test annotations as few-shot examples.
- Never silently remove tokens.
- Do not modify reference datasets.
- Report uncertain grammatical classifications.

## Output
Return a TSV-compatible table containing:
`token`, `lemma`, `POS tag`.

For POS-only tasks, do not invent lemma predictions.
