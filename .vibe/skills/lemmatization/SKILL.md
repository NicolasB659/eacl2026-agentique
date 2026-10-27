---
name: lemmatization
description: Lemmatize historical language tokens using available corpus data and prompt templates.
user-invocable: true
---

# Historical Language Lemmatization

## Objective
Identify the canonical dictionary form (lemma) of each token.

## Supported languages
- GRC: Ancient Greek
- HYE: Classical Armenian
- KAT: Old Georgian
- SYC: Syriac

## Procedure
1. Identify the language and corpus partition.
2. Load the relevant prompt template if available.
3. Preserve Unicode characters and token order.
4. Generate one lemma per input token.
5. Preserve the expected output format.
6. Report ambiguous or uncertain lemmas.

## Constraints
- Never invent missing corpus data.
- Never use test annotations as few-shot examples.
- Keep model predictions separate from reference annotations.
